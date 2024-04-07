#!/usr/bin/python3
"""
This module containe a Fabric script that
"""


from fabric.api import *
import datetime
from os.path import exists


env.hosts = ["100.26.168.20", "100.25.141.186"]


def do_pack():
    """
    This script that generates a .tgz archive
    from the contents of the web_stati
    """
    local("mkdir -p versions")
    filename = "versions/web_static_{}.tgz".format(
            datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            )
    result = local("tar -cvzf {} web_static".format(filename))
    if result.failed:
        return None
    return result


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if not exists(archive_path):
        return False
    # web_static_20170315003959.tgz
    try:
        filename = archive_path.split('/')[-1]
        filenamePathwithNoExtension = '/data/web_static/releases/{}'.format(
            filename.split(".")[0]
            )
        temp = "/tmp/{}".format(filename)
        put(archive_path, "/tmp")
        run("sudo mkdir -p {}".format(filenamePathwithNoExtension))
        run("sudo tar -xvzf {} -C {}/".format(
            temp, filenamePathwithNoExtension
            ))
        run("sudo mv {}/web_static/* {}".format(
            filenamePathwithNoExtension, filenamePathwithNoExtension)
            )
        run("sudo rm {}".format(temp))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {}/ /data/web_static/current".format(
            filenamePathwithNoExtension)
            )
        return True
    except Exception as e:
        return False


def deploy():
    """
    Creates and distributes an archive if exists to the web servers.
    """
    arch_path = do_pack()
    if not exists(arch_path):
        return False
    return do_deploy(arch_path)
