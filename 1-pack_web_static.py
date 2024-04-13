#!/usr/bin/python3
"""
packs web_static into to versions folder
"""
from fabric.api import local


def do_pack():
    """paking webstatic to webst_atic_<date>.tgz archive"""
    date = local('date +"%Y%m%d%H%M%S"', capture=True)
    store = f"versions/web_static_{date}.tgz"
    local("if [! -d versions ];then mkdir versions; fi")
    local(f"echo Packing web_static to {store}")
    local(f"tar -cvzf {store} web_static")
