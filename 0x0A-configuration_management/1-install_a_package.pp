# Define the package resource to install Flask
package { 'Flask':
  ensure => '2.1.0',  # Ensure that Flask version 2.1.0 is installed
  provider => 'pip3',  # Use pip3 as the package provider
}
