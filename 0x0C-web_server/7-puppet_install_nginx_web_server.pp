# Ensure the system package list is updated
exec { 'update system':
  command     => '/usr/bin/apt-get update',
  path        => ['/bin', '/usr/bin'],
  before      => Package['nginx'],
  refreshonly => true,
}

# Ensure Nginx is installed
package { 'nginx':
  ensure => installed,
}

# Ensure the default page contains 'Hello World!'
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Configure Nginx to redirect /redirect_me
file_line { 'nginx_redirect':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  line    => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  match   => '^.*redirect_me.*$',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensure Nginx is running and enabled
service { 'nginx':
  ensure    => running,
  enable    => true,
  require   => Package['nginx'],
  subscribe => File['/var/www/html/index.html', '/etc/nginx/sites-available/default'],
}
