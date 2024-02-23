# Define the package resource to install Flask
package { 'python3-pip':
  ensure => installed,  # Ensure that python3-pip is installed
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
  require => Package['python3-pip'],
}
