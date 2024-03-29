# Define a file resource for /tmp/school
file { '/tmp/school':
  # Ensure that the file exists and has the specified properties
  ensure  => 'file',
  # Set the file permission to 0744
  mode    => '0744',
  # Set the file owner to www-data
  owner   => 'www-data',
  # Set the file permission to 0744
  group   => 'www-data',
  # Set the file contents to "I love puppet"
  content => 'I love Puppet',
}
