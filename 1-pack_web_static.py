#!/usr/bin/python3
"""
This module has the function do pach which generates a .tgz archive 
from the contents of the web_static folder of your AirBnB Clone repo.
"""

from fabric.api import *
import datetime

def do_pack():
    local("mkdir -p versions")
    filename = "versions/web_static_{}.tgz".format(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
    result = local("tar -cvzf {} web_static".format(filename))
    if result.failed:
        return None
    return result
