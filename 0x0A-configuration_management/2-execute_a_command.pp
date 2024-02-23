# Define an exec resource to kill the process named "killmenow"
exec { 'killmenow':
  command     => 'pkill killmenow',  # Use pkill to kill the process
  path        => '/bin:/usr/bin',     # Set the PATH environment variable
  refreshonly => true,                # Only run when notified
  subscribe   => File['/path/to/killmenow'], # Ensure to subscribe to the file change
}
