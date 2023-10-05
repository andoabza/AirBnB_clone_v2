#!/usr/bin/python3
""" import modules """
from fabric.api import put, run, env
from os.path import exists

env.hosts = ['54.174.170.168', '54.90.32.242']
#env.key_filename = '~/.ssh/school'
#env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    Deploys the archive to the web servers.
    Returns True if all operations have been done correctly, otherwise returns False.
    """
    if not exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        archive_filename = archive_path.split('/')[-1]
        archive_folder = '/data/web_static/releases/{}'.format(archive_filename[:-4])
        run('mkdir -p {}'.format(archive_folder))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, archive_folder))
        run('mv {}/web_static/* {}/'.format(archive_folder, archive_folder))
        run('rm -rf {}/web_static'.format(archive_folder))

        run('rm /tmp/{}'.format(archive_filename))

        run('rm -rf /data/web_static/current')

        run('ln -s {} /data/web_static/current'.format(archive_folder))

        return True

    except Exception as e:
        print(e)
        return False

