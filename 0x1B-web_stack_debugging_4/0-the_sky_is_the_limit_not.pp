# auomate the fixation of 934 failed http requests

exec { 'Debug':
  command  => "echo 'ULIMIT=\"-n 4096\"' > /etc/default/nginx",
  provider => shell,
}

-> exec { 'restart nginx':
  command  => 'service nginx restart',
  provider => shell,
}
