#!/usr/bin/env bash
# This script sets up web servers for web_static
if ! command -v nginx &> /dev/null
then
	sudo apt update &> /dev/null
	sudo apt install nginx -y &> /dev/null
fi
if [ ! -d /data/ ]
then
	sudo mkdir /data/
fi
if [ ! -d /data/web_static/ ]
then
	sudo mkdir /data/web_static/
fi
if [ ! -d /data/web_static/releases/ ]
then
	sudo mkdir /data/web_static/releases/
fi
if [ ! -d /data/web_static/shared/ ]
then
	sudo mkdir /data/web_static/shared/
fi
if [ ! -d /data/web_static/releases/test/ ]
then
	sudo mkdir /data/web_static/releases/test/
fi
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"> /data/web_static/releases/test/index.html
sudo ln -f -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R 'ubuntu':'ubuntu' /data/
mypath='/data/web_static/current'
myurl='location /hbnb_static'
if ! grep -q "$myurl" /etc/nginx/sites-available/default
then
	sudo sed -i "s-server_name _;-server_name _;\n\t$myurl {\n\t\t alias $mypath;\n\t}-" /etc/nginx/sites-available/default
fi
sudo service nginx restart &> /dev/null
exit 0
