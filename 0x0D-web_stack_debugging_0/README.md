# Script README

This script is designed to add a server name to the `apache2.conf` file and start the Apache web server.

## Usage

1. Make sure you have the necessary permissions to modify the `apache2.conf` file.
2. Run the script using the following command:

```bash
./script.sh
```

## Script Details

The script starts by appending the line `ServerName localhost` to the `apache2.conf` file located at `/etc/apache2.conf`. This line specifies the server name for the Apache web server.
After that, it starts the Apache web server using the command `service apache2 start`.

Please note that this script assumes that the Apache web server is already installed on your system.
