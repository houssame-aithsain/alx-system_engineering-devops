# Check if the file exists before trying to fix it
if File.exists?('/var/www/html/wp-settings.php') {
  exec { 'fix-wordpress':
    command     => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
    path        => '/usr/local/bin/:/bin/',
    onlyif      => 'grep -q phpp /var/www/html/wp-settings.php',
    notify      => 'Exec[restart-apache]',
    logoutput   => true,
  }

  # Restart Apache to apply the changes
  exec { 'restart-apache':
    command     => 'service apache2 restart',
    path        => '/usr/local/bin/:/bin/',
    refreshonly => true,
  }
} else {
  notice('File /var/www/html/wp-settings.php does not exist')
}
