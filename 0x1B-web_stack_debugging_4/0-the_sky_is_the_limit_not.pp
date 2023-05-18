# increase amount of traffic on nginx 

exec { 'nginx-conf':
  command => 'sed -i "s/15/10000/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# reload nginx 
-> exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
