# Define the file resource
file { '/tmp/school':
  ensure  => file,            # Ensure that it's a file
  mode    => '0744',          # File permission is 0744
  owner   => 'www-data',      # File owner is www-data
  group   => 'www-data',      # File group is www-data
  content => 'I love Puppet' # File content is 'I love Puppet'
}
