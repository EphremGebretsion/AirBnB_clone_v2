from fabric.api import local
def do_pack():
    date = local('date +"%Y%m%d%H%M%S"', capture=True)
    store = f"versions/web_static_{date}.tgz"
    local("if [! -d versions ];then mkdir versions; fi")
    local(f"echo Packing web_static to {store}")
    local(f"tar -cvzf {store} web_static")
