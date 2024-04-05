#!/usr/bin/env bash
# This script sets up your web servers for the deployment of web_static.

# Install Nginx if it not already installed
if [ -z "$(command -v nginx)" ]
then
        apt-get update
        apt-get -y install nginx
fi

sudo mkdir -p /data/web_static/{releases/test,shared}

# Create a fake HTML file /data/web_static/releases/test/index.html
if [ ! -f "/data/web_static/releases/test/index.html" ]
then
        echo '
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
' | sudo tee "/data/web_static/releases/test/index.html"
fi

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/
sudo ln -sf "/data/web_static/releases/test/" "/data/web_static/current"


# Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

line_num=$(($(grep -n "^}" /etc/nginx/sites-available/default | cut -d ':' -f 1) - 1))
config="\tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}"

find=$(grep "location /hbnb_static" /etc/nginx/sites-available/default)
if [ -z "$find" ]
then
        sudo sed -i "${line_num}a\\$config" /etc/nginx/sites-available/default
fi

# Restart Nginx to apply change
sudo service nginx restart
