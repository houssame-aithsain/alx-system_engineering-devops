# This Puppet manifest changes the limitations on the 'holberton' user.
# It modifies the /etc/security/limits.conf file, which configures limits for user sessions.
# The 'nofile' limit specifies the maximum number of open file descriptors.
# The 'hard' limit is the absolute maximum limit, and the 'soft' limit is the default limit.
# This manifest increases both the 'hard' and 'soft' 'nofile' limits for the 'holberton' user to 88888.
# This can help to prevent 'Too many open files' errors if the 'holberton' user needs to open many files simultaneously.

exec { 'change-os-configuration-for-holberton-user':
  command => "bash -c \"sed -iE 's/^holberton hard nofile 5/holberton hard nofile 88888/' /etc/security/limits.conf; sed -iE 's/^holberton soft nofile 4/holberton soft nofile 88888/' /etc/security/limits.conf\"",
  path    => '/usr/bin:/usr/sbin:/bin'
}
