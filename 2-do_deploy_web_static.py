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
    if exists(archive_path) is False:
        return False
    # -> path version/ 
    filename = archive_path.split('/')[-1]
    filenamePathwithNoExtension = '/data/web_static/releases/{}'.format(
            filename.split(".")[0]
            )
    temp = "/tmp/{}".format(filename)
    try:
        put(archive_path, "/tmp")
        run("mkdir -p {}".format(filenamePathwithNoExtension))
        print(filenamePathwithNoExtension)
        run("tar -xzf {} -C {}/".format(temp, filenamePathwithNoExtension))
        run("rm {}".format(temp))
        run("rm -r /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(
            filenamePathwithNoExtension)
            )
        return True
    except Exception:
        print("CComand failed")
        return False
