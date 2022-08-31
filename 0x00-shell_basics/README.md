#!/bin/bash

1. pwd -A script that prints the absolute path name of the current working directory.

2. ls - Displays the contents list of your current directory.

3. cd - Changes the working directory to the user’s home directory.

4. ls -l - Displays current directory contents in a long format.

5. ls -a -l - Displays current directory contents, including hidden files (starting with .). Use the long format.

6. ls -l -a -n or (ls -lan) - Display current directory contents: Long format, with user and group IDs displayed numerically, And hidden files (starting with .)

7. mkdir /tmp/my_first_directory - Creates a directory named my_first_directory in the /tmp/ directory.

8. mv /tmp/betty /tmp/my_first_directory - Move the file betty from /tmp/ to /tmp/my_first_directory.

9. rm -r /tmp/my_first_directory/betty - Delete the file betty.

10. rm -r /tmp/my_first_directory - Delete the directory my_first_directory that is in the /tmp directory.

11. "cd -" - Changes the working directory to the previous one.

12. ls -al . .. /boot -  Lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.

13. file /tmp/iamafile - Prints the type of the file named iamafile. The file iamafile will be in the /tmp director.ln -s /bin/ls _ls_ - Creates a symbolic link to /bin/ls, named __ls__.

14. "cp -rua *.html" -* Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.

15. mv [[:upper:]]* /tmp/u -*Creates a script that moves all files beginning with an uppercase letter.

16. rm *~ - *Create a script that deletes all files in the current working directory. 
