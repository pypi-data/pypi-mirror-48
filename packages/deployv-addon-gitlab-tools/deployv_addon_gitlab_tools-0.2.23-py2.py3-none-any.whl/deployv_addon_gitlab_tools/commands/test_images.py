# coding: utf-8

from deployv_addon_gitlab_tools.common import check_env_vars, get_main_app
from deployv_addon_gitlab_tools.commands.check_keys import check_credentials, is_docker_login
from deployv.helpers import utils
from docker import errors, APIClient as Client
from os import environ
import re
import subprocess
import time
import shlex
import sys
import click
import logging
import json
import requests
import signal
from urllib3.exceptions import ReadTimeoutError


logger = logging.getLogger('deployv.' + __name__)  # pylint: disable=C0103
_cli = Client(timeout=7200)

def reciveSignal(signalNumber, frame):
    clean_containers()
    clear_images()
    sys.exit(0)


signal.signal(signal.SIGTERM, reciveSignal)
signal.signal(signal.SIGINT, reciveSignal)


def generate_image_name(name):
    """ Generate the base image name usig the ref name but cleaning it before,
    ATM only removes "." and "#" from the title to avoid issues with docker naming
    convention """
    res = re.sub(r'[\.#\$\=\+\;\>\,\<,\&\%]', '', name)
    res = re.sub(r'-_', '_', res)
    return res.lower()


def build_image():
    logger.info('Building image')
    cmd = ('deployvcmd build -b {branch} -u {url} -v {version} -i {image} -O {repo}#{odoo_branch} -T {tag}'
           .format(branch=environ['CI_COMMIT_REF_NAME'], url=environ['CI_REPOSITORY_URL'], repo=environ['ODOO_REPO'],
                   odoo_branch=environ['ODOO_BRANCH'], version=environ['VERSION'], image=environ['BASE_IMAGE'],
                   tag=environ['_INSTANCE_IMAGE']))
    try:
        subprocess.check_call(shlex.split(cmd))
    except subprocess.CalledProcessError:
        logger.exception('Could not build the image, please read the log above')
        sys.exit(1)
    images = _cli.images(environ['_INSTANCE_IMAGE'])
    image_sha = images[0].get('Id')
    short_id = image_sha.split(':')[1][:10]
    environ.update({
        '_IMAGE_TAG': short_id,
    })


def pull_images():
    """ Pulls images needed for the build and test process """
    images = [environ['BASE_IMAGE'],
              environ['_POSTGRES_IMAGE']]
    for image in images:
        logger.info('Pulling: %s', image)
        _cli.pull(image)
    return images


def postgres_container():
    return 'postgres{0}_{1}'.format(environ['_BASE_NAME'], environ['CI_PIPELINE_ID'])


def clean_containers():
    """ Cleans any running container related to the same build to avoid any conflicts """
    containers = _cli.containers(all=True, filters={'name': environ['_BASE_NAME']})
    for container in containers:
        try:
            logger.info('Removing container %s', container.get('Name', container.get('Names')[0]))
            _cli.remove_container(container['Id'], force=True)
        except errors.NotFound:
            logger.info('Container %s does not exist', container.get('Name', container.get('Names')[0]))


def clear_images():
    logger.info('Removing image %s', environ['_INSTANCE_IMAGE'])
    try:
        _cli.remove_image(environ['_INSTANCE_IMAGE'])
    except errors.APIError as error:
        if 'No such image' in error.explanation:
            pass
    logger.info('Image %s deleted', environ['_INSTANCE_IMAGE'])


def start_postgres():
    logger.info('Starting container %s', postgres_container())
    container = _cli.create_container(image=environ['_POSTGRES_IMAGE'],
                                      name=postgres_container(),
                                      environment={'POSTGRES_PASSWORD': 'postgres'})
    _cli.start(container=container.get('Id'))
    logger.info(container)


def create_postgres_user():
    cmd = "psql -c \"create user odoo with password 'odoo' createdb\""
    res = exec_cmd(postgres_container(), cmd, 'postgres')
    return res


def start_instance():
    env = {
        "DB_USER": "odoo",
        "DB_PASSWORD": "odoo",
        "DB_HOST": postgres_container(),
        "ODOO_CONFIG_FILE": "/home/odoo/.openerp_serverrc"
    }
    for env_var in ['COUNTRY', 'LANGUAGE']:
        env.update({env_var: environ.get(env_var, "")})
    links = {
        postgres_container(): postgres_container()
    }
    host_config = _cli.create_host_config(links=links)
    logger.info('Starting container %s', environ['_INSTANCE_IMAGE'])
    logger.debug('Env vars %s', json.dumps(env, sort_keys=True, indent=4))
    container = _cli.create_container(image=environ['_INSTANCE_IMAGE'],
                                      name=environ['_INSTANCE_IMAGE'],
                                      environment=env,
                                      host_config=host_config)
    _cli.start(container=container.get('Id'))
    logger.info(container)


def install_module():
    module = get_main_app()
    extra = ''
    if environ.get('LANGUAGE'):
        extra += ' --load-language={lang}'.format(lang=environ.get('LANGUAGE'))
    install_wdemo = (
        "/home/odoo/instance/odoo/odoo-bin -d wdemo -i {mod}"
        "{extra} --stop-after-init".format(mod=module, extra=extra)
    )
    install_wodemo = (
        "/home/odoo/instance/odoo/odoo-bin -d wodemo -i {mod}"
        "{extra} --stop-after-init --without-demo=all".format(mod=module, extra=extra)
    )
    logger.info('Verifying supervisorctl')
    is_running()
    logger.info('Stopping odoo')
    exec_cmd(environ['_INSTANCE_IMAGE'], 'supervisorctl stop odoo')
    logger.info('\nInstalling %s with demo', module)
    logger.debug('Command : %s', install_wdemo)
    wdemo_res = exec_cmd(environ['_INSTANCE_IMAGE'], install_wdemo, 'odoo', stream=True)
    wdemo_log = resume_log(wdemo_res)
    logger.info('\nInstalling %s without demo', module)
    logger.debug('Command : %s', install_wodemo)
    wodemo_res = exec_cmd(environ['_INSTANCE_IMAGE'], install_wodemo, 'odoo', stream=True)
    wodemo_log = resume_log(wodemo_res)
    show_log(wdemo_log[1], 'Installation with demo')
    show_log(wodemo_log[1], 'Installation without demo')
    if not wdemo_log[0] or not wodemo_log[0]:
        return False
    return True


def exec_cmd(container, cmd, user=None, stream=False):
    lines = []
    container_id = _cli.inspect_container(container).get('Id')
    logger.debug('Executing command "{cmd}" in container "{con}".'.format(cmd=cmd, con=container))
    try:
        exec_id = _cli.exec_create(container_id, cmd, user=user)
    except errors.APIError as error:
        logger.error('Error: %s', error.explanation)
        raise
    res = _cli.exec_start(exec_id.get('Id'), stream=stream)
    if stream:
        for line in res:
            line = utils.decode(line)
            logger.info(line.strip('\n'))
            lines.append(line)
        return lines
    return utils.decode(res)


def show_log(log, title):
    logger.info('\n%s', title)
    logger.info('='*20)
    logger.info('+-- Critical errors %s', len(log.get('critical')))
    logger.info('+-- Errors %s', len(log.get('errors')))
    logger.info('+-- Import errors %s', len(log.get('import_errors')))
    logger.info('+-- Warnings %s', len(log.get('warnings')))
    logger.info('+-- Translation Warnings %s', len(log.get('warnings_trans')))
    logger.info('='*20)


def resume_log(log_lines):
    """Gets the log lines from -u (modules or all) and parse them to get the totals
    according to the filters dict

    :param log_lines: each element of the list is a log line
    :return: dict with key filters as keys and a list with all matched lines
    """
    def critical(line):
        criteria = re.compile(r'.*\d\sCRITICAL\s.*')
        return criteria.match(line)

    def errors(line):
        criteria = re.compile(r'.*\d\sERROR\s.*')
        return criteria.match(line)

    def warnings_trans(line):
        criteria = re.compile(
            r'.*\d\sWARNING\s.*no translation for language.*')
        return criteria.match(line)

    def import_errors(line):
        criteria = re.compile(r'^ImportError.*')
        return criteria.match(line)

    def warnings(line):
        criteria = re.compile(r'.*\d\sWARNING\s.*')
        return criteria.match(line) and 'no translation for language' not in line

    filters = {
        'critical': critical,
        'errors': errors,
        'warnings': warnings,
        'warnings_trans': warnings_trans,
        'import_errors': import_errors
    }
    success = True
    res = {name: [] for name in filters}
    for line in log_lines:
        stripped_line = line.strip()
        for name, criteria in filters.items():
            if criteria(stripped_line):
                if name in ['critical', 'errors']:
                    success = False
                elif name == 'warnings' and 'Deprecated' in stripped_line:
                    success = False
                res.get(name).append(stripped_line)
                break
    return (success, res)


def is_running():
    retry = True
    retries = 0
    while retry and retries <= 10:
        try:
            res = exec_cmd(environ['_INSTANCE_IMAGE'], 'supervisorctl status odoo')
        except errors.APIError:
            retries += 1
            logger.warn('Container error, retrying %s', retries)
            time.sleep(5)
            continue
        logger.info('is_running: %s', res.strip())
        if 'STARTING' in res or 'STOPPING' in res:
            logger.warn('The Odoo process is in an intermediate state, retrying')
            time.sleep(5)
        elif 'RUNNING' in res:
            return True
        elif 'STOPPED' in res:
            return False
        elif res == '' or 'no such file' in res:
            retries += 1
            logger.warn('Supervisor returned empty or not running yet, retrying %s', retries)
            time.sleep(5)
        else:
            retries += 1
            logger.warn('Unknown state: %s', res)
            time.sleep(5)


def push_image(image_name, image_tag):
    logger.info('Pushing image %s to %s:%s', image_name, environ['_IMAGE_REPO'], image_tag)
    _cli.tag(image_name, environ['_IMAGE_REPO'], tag=image_tag)
    if is_docker_login():
        _cli.login(environ['DOCKER_USER'], environ['DOCKER_PASSWORD'], registry='quay.io')
    for attempt in range(4):
        try:
            for result in _cli.push(environ['_IMAGE_REPO'], tag=image_tag, stream=True):
                result = json.loads(utils.decode(result))
                if result.get('error'):
                    logger.error(result.get('error'))
                    sys.exit(1)
            else:
                break
        except ReadTimeoutError as error:
            if 'Read timed out' in error.message and attempt < 3:
                logger.warn('An error raised while pushing the image, retrying (%s / 3)', attempt+1)
            else:
                raise

    logger.info('Image pushed correctly')


def notify_orchest(tag, customer, is_latest=False):
    image_name = '{image}:{tag}'.format(image=environ['_IMAGE_REPO'], tag=tag)
    res = requests.post(
        environ['ORCHEST_REGISTRY'], data=json.dumps({
            'image_name': image_name, 'is_latest': is_latest, 'branch_name': environ['CI_COMMIT_REF_NAME'],
            'job_id': environ['CI_JOB_ID'], 'project_id': environ['CI_PROJECT_ID'],
            'commit': environ['CI_COMMIT_SHA'][:7], 'customer_id': customer}),
        headers={'Content-Type': 'application/json', 'Orchest-Token': environ['ORCHEST_TOKEN']})
    if res.status_code != 200:
        logger.error('Failed to notify orchest about the new image: %s', res.text)
        sys.exit(1)
    data = res.json()
    if data.get('error'):
        logger.error('Failed to notify orchest about the new image: %s',
                     data.get('error').get('data', {}).get('name'))
        sys.exit(1)
    logger.info('Successfully notified orchest about the new image: %s', image_name)


@click.command()
@click.option('--ci_commit_ref_name', default=environ.get('CI_COMMIT_REF_NAME'),
              help=("The branch or tag name for which project is built."
                    " Env var: CI_COMMIT_REF_NAME."))
@click.option('--ci_pipeline_id', default=environ.get('CI_PIPELINE_ID'),
              help=("The unique id of the current pipeline that GitLab CI"
                    " uses internally. Env var: CI_PIPELINE_ID."))
@click.option('--ci_repository_url', default=environ.get('CI_REPOSITORY_URL'),
              help=("The URL to clone the Git repository."
                    " Env var: CI_REPOSITORY_URL."))
@click.option('--base_image', default=environ.get('BASE_IMAGE'),
              help=("Env var: BASE_IMAGE."))
@click.option('--odoo_repo', default=environ.get('ODOO_REPO'),
              help=("Env var: ODOO_REPO."))
@click.option('--odoo_branch', default=environ.get('ODOO_BRANCH'),
              help=("Env var: ODOO_BRANCH."))
@click.option('--version', default=environ.get('VERSION'),
              help=("Env var: VERSION."))
@click.option('--install', default=get_main_app(),
              help=("Env var: MAIN_APP."))
@click.option('--ci_job_id', default=environ.get('CI_JOB_ID'),
              help=("The unique id of the current job that GitLab CI uses internally."
                    " Env var: CI_JOB_ID."))
@click.option('--psql_image', default=False,
              help=("Override the default postgresql image to use for the tests"
                    "(Notice that this will override the PSQL_VERSION too)"))
@click.option('--image_repo_url', default=environ.get('IMAGE_REPO_URL', "quay.io/vauxoo"),
              help=("The URL where the image repository is located."
                    " Env var: IMAGE_REPO_URL."))
@click.option('--push_image', is_flag=True,
              help="If set it will push the image when on the main branch after the tests")
def test_images(**kwargs):
    check_env_vars(**kwargs)
    check_credentials(environ.get('PRIVATE_DEPLOY_KEY', False))
    base_name = generate_image_name('{0}_{1}'.format(
        kwargs.get('ci_commit_ref_name'), kwargs.get('ci_job_id')))
    if kwargs.get('psql_image'):
        postgres_image = kwargs.get('psql_image')
    else:
        postgres_image = 'vauxoo/docker-postgresql:{0}-ci'.format(environ.get('PSQL_VERSION', '9.5'))
    instance_image = generate_image_name('instance{0}_{1}'.format(
        base_name, kwargs.get('ci_pipeline_id')))

    customer = environ.get('CUSTOMER', environ.get('CI_PROJECT_NAME'))
    version_tag = environ.get('VERSION').replace('.', '')

    environ.update({
        '_BASE_NAME': base_name,
        '_POSTGRES_IMAGE': postgres_image,
        '_INSTANCE_IMAGE': instance_image,
    })
    if kwargs.get('push_image'):
        if not environ.get('ORCHEST_REGISTRY', False) or not environ.get('ORCHEST_TOKEN', False):
            logger.error('To push the image you need to set ORCHEST_REGISTRY and ORCHEST_TOKEN env vars')
            sys.exit(1)

    clean_containers()
    pull_images()
    start_postgres()
    build_image()
    create_postgres_user()
    start_instance()
    res = install_module()
    clean_containers()
    if not res:
        clear_images()
        sys.exit(1)
    is_latest = False
    if kwargs.get('push_image'):
        customer_img = '{customer}{ver}'.format(customer=customer.strip(),
                                                ver=version_tag)
        image_repo = '{url}/{image}'.format(url=environ.get('IMAGE_REPO_URL'),
                                            image=customer_img)
        environ.update({'_IMAGE_REPO': image_repo})
        # TODO: if we decide to build and push every image, just move the _IMAGE_TAG outside the if
        if environ.get('CI_COMMIT_REF_NAME') == environ.get('VERSION'):
            push_image(instance_image, 'latest')
            is_latest = True
        push_image(instance_image, environ['_IMAGE_TAG'])
        notify_orchest(environ['_IMAGE_TAG'], customer_img, is_latest=is_latest)
    clear_images()
    sys.exit(0)
