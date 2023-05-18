# increase amount of traffic on nginx

# edit the nginx file in etc/default directory
exec { 'edit-nginx-file':
  command => 'sed -i "s/15/10000/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# reload nginx 
exec { 'reload-nginx':
  command => '/usr/sbin/service nginx restart',
  path    => '/usr/sbin:/usr/bin:/sbin:/bin',
}
