# automated puppet fix (to find out why Apache is returning a 500 error)

exec { 'Fix WordPress site':
  command  => 'sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  path     => ['/bin', '/usr/bin'],  # Specify the PATH environment variable
  provider => shell,
  onlyif   => 'grep -q ".phpp" /var/www/html/wp-settings.php',  # Ensure the fix is only applied if necessary
}
