# Puppet manifest to add a custom HTTP header 'X-Served-By' with the hostname of the server to Nginx configuration

class nginx_custom_header {
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure     => running,
    enable     => true,
    require    => Package['nginx'],
    subscribe  => File['/etc/nginx/sites-available/default'],
  }

  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => template('nginx/default.erb'),
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  file_line { 'custom_http_header':
    path  => '/etc/nginx/sites-available/default',
    line  => 'add_header X-Served-By $hostname;',
    match => '^[\s]*add_header X-Served-By',
    require => File['/etc/nginx/sites-available/default'],
  }
}

include nginx_custom_header
