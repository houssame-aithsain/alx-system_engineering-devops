# Install the necessary package
file_line { 'Turn off passwd auth':
    ensure => 'present',
    path  => '/etc/ssh/sshd_config',
    line  => 'PasswordAuthentication no',
}

# Declare identity file
file_line { 'Declare identity file':
    ensure => 'present',
    path  => '/etc/ssh/ssh_config',
    line  => 'IdentityFile ~/.ssh/school',
}
