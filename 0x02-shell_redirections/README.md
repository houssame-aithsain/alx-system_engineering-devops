This repository contains shell scripts that perform various tasks related to shell redirections.
0-hello_world

This script prints "Hello, World" followed by a new line to the standard output.

shell

$ ./0-hello_world
Hello, World
$ ./0-hello_world | cat -e
Hello, World$
$

1-confused_smiley

This script displays a confused smiley "(Ôo)'.

ruby

$ ./1-confused_smiley
"(Ôo)'

2-hellofile

This script displays the content of the /etc/passwd file.

bash

$ ./2-hellofile
<content of /etc/passwd>

3-twofiles

This script displays the content of both the /etc/passwd and /etc/hosts files.

bash

$ ./3-twofiles
<content of /etc/passwd>
<content of /etc/hosts>

4-lastlines

This script displays the last 10 lines of the /etc/passwd file.

bash

$ ./4-lastlines
<last 10 lines of /etc/passwd>

5-firstlines

This script displays the first 10 lines of the /etc/passwd file.

bash

$ ./5-firstlines
<first 10 lines of /etc/passwd>

6-third_line

This script displays the third line of the file iacta.

arduino

$ ./6-third_line
<third line of iacta>

7-file

This script creates a file named *\\"Best School\\"\\*$?*****:) containing the text "Best School" followed by a new line.

ruby

$ ./7-file
$ cat -e *\\"Best School\\"\\*$?*****:)*
Best School$

8-cwd_state

This script writes the result of the ls -la command into the file ls_cwd_content. If the file already exists, it is overwritten.

bash

$ ./8-cwd_state
$ cat ls_cwd_content
<output of ls -la command>

9-duplicate_last_line

This script duplicates the last line of the file iacta.

shell

$ ./9-duplicate_last_line
$ cat iacta
<content of iacta>
<last line of iacta>

10-no_more_js

This script deletes all the regular files with a .js extension in the current directory and its subfolders.

sql

$ ./10-no_more_js
<regular files with .js extension are deleted>

Note: Replace <content> and <output> with the actual content and output of the respective commands.

For each task, there is a corresponding file in the alx-system_engineering-devops/0x02-shell_redirections GitHub repository.
