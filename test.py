from fabric.api import *

env.hosts = ["100.26.168.20", "100.25.141.186"]

def test_ssh():
    run("echo 'Hello, Fabric!'")
