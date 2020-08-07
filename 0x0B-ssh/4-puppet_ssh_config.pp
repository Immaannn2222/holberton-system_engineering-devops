# Connect to a server without typing a password(Puppet)

file_line { 'Create_identity_file':
ensure => 'present',
path   => '/etc/ssh/ssh_config',
line   => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'Turn_off_passwd_auth':
ensure => 'presnet'
path   => '/etc/ssh/ssh_config',
line   => 'PasswordAuthentication no',
}
