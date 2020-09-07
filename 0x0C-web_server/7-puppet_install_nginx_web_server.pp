#!/usr/bin/env bash
#install nginx with puppet
exec {'install':
command  => 'sudo apt-get -y update;
sudo apt-get -y install nginx;
sudo chmod 777 /var/www/html/index.nginx-debian.html;
echo "Holberton School" > /var/www/html/index.nginx-debian.html;
sudo service nginx start',
provider => shell,
}
