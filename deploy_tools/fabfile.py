from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run, sudo, put
import random
#run
#fab deploy:host=stri@192.168.56.101

REPO_URL = 'https://github.com/forestIn/tickets.git'  
NAME_APP = 'tickets'
SITENAME = "tickets.local"

def deploy():
    site_folder = '/home/%s/sites/%s' % (env.user, SITENAME)
    source_folder = site_folder + '/source'
    _create_directory_structure_if_necessary(site_folder)
    _get_latest_source(source_folder)
    _update_settings(source_folder, env.host)
    _update_virtualenv(source_folder)
    _update_static_files(source_folder)
    _update_database(source_folder)
    _install_nginx(source_folder)
    _add_upstart(source_folder)


def _create_directory_structure_if_necessary(site_folder):
    for subfolder in ('database', 'static', 'virtualenv', 'source'):
        run('mkdir -p %s/%s' % (site_folder, subfolder))

def _get_latest_source(source_folder):
    if exists(source_folder + '/.git'):
        run('cd %s && git fetch' % (source_folder,))
    else:
        run('git clone %s %s' % (REPO_URL, source_folder))
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run('cd %s && git reset --hard %s' % (source_folder, current_commit))

def _update_settings(source_folder, site_name):
    settings_path = source_folder + '/'+NAME_APP+'/settings.py'
    sed(settings_path, "DEBUG = True", "DEBUG = False")
    sed(settings_path,
        'ALLOWED_HOSTS =.+$',
        'ALLOWED_HOSTS = ["%s"]' % (site_name,)
    )
    secret_key_file = source_folder + '/'+NAME_APP+'/secret_key.py'
    if not exists(secret_key_file):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
        append(secret_key_file, "SECRET_KEY = '%s'" % (key,))
    append(settings_path, '\nfrom .secret_key import SECRET_KEY')

def _update_virtualenv(source_folder):
    virtualenv_folder = source_folder + '/../virtualenv'
    if not exists(virtualenv_folder + '/bin/pip'):
        run('virtualenv --python=python3 %s' % (virtualenv_folder,))
    run('%s/bin/pip install -r %s/requirements/production.txt' % (
            virtualenv_folder, source_folder
    ))


def _update_static_files(source_folder):
    run('cd %s && ../virtualenv/bin/python3 manage.py collectstatic --noinput' % (
        source_folder,
    ))


def _update_database(source_folder):
    run('cd %s && ../virtualenv/bin/python3 manage.py migrate --noinput' % (
        source_folder,
    ))
def _install_nginx(source_folder):
    """ Install nginx and copy over our config file """
    if not exists("/etc/nginx/sites-available/%s" % (SITENAME)):
        sudo('apt-get install -y nginx')
        sudo('rm -r /etc/nginx/sites-available/default')
        sudo('rm -r /etc/nginx/sites-enabled/default')
        sed('%s/deploy_tools/nginx.template.conf' % (source_folder), "SITENAME", SITENAME)
        
        sudo('mv %s/deploy_tools/nginx.template.conf /etc/nginx/sites-available/%s' % (source_folder,SITENAME))

        sudo("ln -s ../sites-available/%s /etc/nginx/sites-enabled/%s" % (SITENAME,SITENAME))        
        sudo('service nginx reload')

def _add_upstart(source_folder):    
    sed('%s/deploy_tools/gunicorn-upstart.template' % (source_folder), "SITENAME", SITENAME)
    sed('%s/deploy_tools/gunicorn-upstart.template' % (source_folder), "NAME_APP", NAME_APP)
    sudo('cp %s/deploy_tools/gunicorn-upstart.template /etc/init/%s.conf' % (source_folder,SITENAME))
    sudo('start %s' % (SITENAME))

