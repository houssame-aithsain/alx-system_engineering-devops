# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure    => running,
  enable    => true,
  require   => Package['nginx'],
}

# Configure Nginx to serve 'Hello World!' at root
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Configure Nginx to perform a 301 redirect for /redirect_me
file_line { 'nginx_redirect':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  line    => 'rewrite ^/redirect_me$ http://example.com permanent;',
  match   => '^.*redirect_me.*$',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensure the Nginx configuration is reloaded to apply changes
exec { 'nginx_reload':
  command     => '/usr/sbin/nginx -s reload',
  refreshonly => true,
  subscribe   => File['/var/www/html/index.html', '/etc/nginx/sites-available/default'],
}
