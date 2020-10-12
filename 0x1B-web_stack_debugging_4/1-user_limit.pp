#login with the holberton user
exec { 'modify file':
command  => 'sudo echo "fs.file-max = 65536" >> /etc/sysctl.conf',
provider => shell,
}
exec { 'change limit':
command  => 'sudo sysctl -p',
provider => shell,
}