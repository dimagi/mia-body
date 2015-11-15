from fabric.api import sudo, run, cd, env, task, execute
from fabric.colors import red, white, green

# the user to use for the remote commands
env.user = 'deploy'
# the servers where the commands are executed
env.hosts = ['192.168.7.228']
env.code_root = '/home/deploy/www/mia/src'


def update_code():
    with cd(env.code_root):
        run('git remote prune origin')
        run('git pull origin master')


def install_deps():
    with cd(env.code_root):
        run('npm install')


@task
def restart_services():
    sudo('supervisorctl restart mia', user='root')


@task
def deploy():
    print green('''
        ,---.    ,---..-./`)    ____
    |    \  /    |\ .-.') .'  __ `.
    |  ,  \/  ,  |/ `-' \/   '  \  \\
    |  |\_   /|  | `-'`"`|___|  /  |
    |  _( )_/ |  | .---.    _.-`   |
    | (_ o _) |  | |   | .'   _    |
    |  (_,_)  |  | |   | |  _( )_  |
    |  |      |  | |   | \ (_ o _) /
    '--'      '--' '---'  '.(_,_).'
    ''')
    print white('You are now deploying Mia!!')
    try:
        execute(update_code)
        execute(install_deps)
        execute(restart_services)
    except Exception:
        print red('Mia has failed to deploy')
