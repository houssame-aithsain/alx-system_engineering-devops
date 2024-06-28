# This manifest will execute a command
exec { 'killmenow':
    command => 'pkill killmenow',
    path    => '/usr/bin:/usr/sbin:/bin:/sbin',
}
