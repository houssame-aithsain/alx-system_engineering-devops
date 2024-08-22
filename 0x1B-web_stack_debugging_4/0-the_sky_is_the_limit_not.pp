# This Puppet manifest fixes an issue with an Nginx site that can't handle multiple concurrent requests.
# It does this by increasing the limit on the number of file descriptors that can be opened by the Nginx process.
# The limit is set in the /etc/default/nginx file, and this manifest modifies that file to set the limit to 8192.
# After modifying the file, it restarts the Nginx service to apply the changes.

# Check if the file exists before trying to fix it
if File.exists?('/etc/default/nginx') {
  exec { 'fix-for-nginx':
    command     => "bash -c \"sed -iE 's/^ULIMIT=.*/ULIMIT=\\\"-n 8192\\\"/' /etc/default/nginx; service nginx restart\"",
    path        => '/usr/bin:/usr/sbin:/bin',
    onlyif      => "bash -c \"grep -q '^ULIMIT=' /etc/default/nginx && ! grep -q '^ULIMIT=\\\"-n 8192\\\"' /etc/default/nginx\"",
    logoutput   => true,
  }
} else {
  notice('File /etc/default/nginx does not exist')
}
