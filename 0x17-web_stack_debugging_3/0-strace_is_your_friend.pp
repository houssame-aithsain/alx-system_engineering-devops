# This manifest fixes a typo in the WordPress settings file by replacing 'phpp' with 'php'

exec { 'fix-wordpress':
  command => '/bin/sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => ['/usr/local/bin', '/bin']
}
