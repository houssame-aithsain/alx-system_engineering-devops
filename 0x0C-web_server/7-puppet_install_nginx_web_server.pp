# Ensure Nginx is installed

exec { 'update system':
        command => '/usr/bin/apt-get update',
}

package { 'nginx':
	ensure => 'installed',
	require => Exec['update system']
}

file {'/var/www/html/index.html':
	content => 'Hello World!'
}

# Add a comment here to explain the purpose of the code
exec {'redirect_me':
    command => 'sed -i "24i\    rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-sdfsdfsdf permanent;" /etc/nginx/sites-available/default',
    provider => 'shell'
}


# Ensure Nginx service is running
service {'nginx':
    ensure => 'running',
    require => Package['nginx']
}
