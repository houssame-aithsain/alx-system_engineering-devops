Shell Permissions Tasks

This repository contains a collection of shell scripts that demonstrate various tasks related to shell permissions. Each script performs a specific action, as described below:
Task 0: My name is Betty

This script switches the current user to the user betty.

Usage:

shell

$ ./0-iam_betty

Task 1: Who am I

This script prints the effective username of the current user.

Usage:

shell

$ ./1-who_am_i

Task 2: Groups

This script prints all the groups the current user is part of.

Usage:

shell

$ ./2-groups

Note: The output may vary depending on the user.
Task 3: New owner

This script changes the owner of the file hello to the user betty.

Usage:

shell

$ sudo ./3-new_owner

Task 4: Empty!

This script creates an empty file called hello.

Usage:

shell

$ ./4-empty

Task 5: Execute

This script adds execute permission to the owner of the file hello.

Usage:

shell

$ ./5-execute

Task 6: Multiple permissions

This script adds execute permission to the owner and the group owner, and read permission to other users, to the file hello.

Usage:

shell

$ ./6-multiple_permissions

Task 7: Everybody!

This script adds execution permission to the owner, the group owner, and other users, for the file hello.

Usage:

shell

$ ./7-everybody

Task 8: James Bond

This script sets the permissions for the file hello as follows:

    Owner: no permission at all
    Group: no permission at all
    Other users: all permissions

Usage:

shell

$ ./8-James_Bond

Task 9: John Doe

This script sets the mode of the file hello to -rwxr-x-wx.

Usage:

shell

$ ./9-John_Doe

Task 10: Look in the mirror

This script sets the mode of the file hello the same as the mode of olleh.

Usage:

shell

$ ./10-mirror_permissions

Note: The mode of olleh can vary, and the script handles any mode.
Task 11: Directories

This script adds execute permission to all subdirectories of the current directory for the owner, the group owner, and all other users. Regular files are not changed.

Usage:

shell

$ ./11-directories_permissions

Task 12: More directories

This script creates a directory called my_dir with permissions 751 in the working directory.

Usage:

shell

$ ./12-directory_permissions

Task 13: Change group

This script changes the group owner of the file hello to school.

Usage:

shell

$ sudo ./13-change_group

Note: The file hello should be present in the working directory.

Repository Information:

    GitHub Repository: alx-system_engineering-devops
    Directory: 0x01-shell_permissions
    Files:
        0-iam_betty
        1-who_am_i
        2-groups
        3-new_owner
        4-empty
        5-execute
        6-multiple_permissions
        7-everybody
        8-James_Bond
        9-John
