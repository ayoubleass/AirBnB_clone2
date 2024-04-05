#!/usr/bin/python3
"""
This module contains the do_deploy
"""


from fabric.api import *
from os.path import exists


env.hosts = ["100.26.168.20", "100.25.141.186"]


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if not exists(archive_path):
        return False
    # web_static_20170315003959.tgz
    filename = archive_path.split('/')[-1]
    filenamePathwithNoExtension = '/data/web_static/releases/{}'.format(
            filename.split(".")[0]
            )
    temp = "/tmp/{}".format(filename)
    try:
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
        print("{}".format(e))
        return False
