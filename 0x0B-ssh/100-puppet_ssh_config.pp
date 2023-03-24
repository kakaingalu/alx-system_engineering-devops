# set up your client SSH configuration file so that so as to connect to a server without typing a password.

file_line {'Turn off passwd auth':
  ensure => 'present'
  path   => '/etc/ssh/sshd_config',
  line   => 'PasswordAuthentication no',
}

file_line {'Declare identify file':
  ensure => 'present'
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentifyFile ~/.ssh/school',
}
