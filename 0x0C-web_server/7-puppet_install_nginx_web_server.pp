#!/usr/bin/env bash
#install nginx with puppet
exec {'install':
command  => 'sudo apt-get -y update;
sudo apt-get -y install nginx;
sudo chmod 777 /var/www/html/index.nginx-debian.html;
echo "Holberton School" > /var/www/html/index.nginx-debian.html;
printf %s "server {
    listen 80;
    listen [::]:80 default_server;
    root   /usr/share/nginx/html;
    index  index.html index.htm;
    location /redirect_me {
        return 301 http://youtube.com/watch?v=QH2-TGUlwu4;
    }
}" > /etc/nginx/sites-available/default;
sudo service nginx start',
provider => shell,
}
