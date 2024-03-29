# Processes and signals

## Description
Introduction to processes and signals

## Resources
## Read or watch:

<li> Linux PID </li>
<li> Linux process </li>
<li> Linux signal </li>
<li> Process management in linux </li>

## man or help:
<li> ps </li>
<li> pgrep </li>
<li> pkill </li>
<li> kill </li>
<li> exit </li>
<li> trap </li>

## Learning Objectives
<li> At the end of this project, you are expected to be able to explain to anyone, without the help of Google: </li>

## General
<li> What is a PID </li>
<li> What is a process </li>
<li> How to find a process PID </li>
<li> How to kill a process </li>
<li> What is a signal </li>
<li> What are the 2 signals that cannot be ignored </li>
<li> Copyright - Plagiarism </li>
<li> You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives. </li>
<li> You will not be able to meet the objectives of this or any following project by copying and pasting someone elses work. </li>
<li> You are not allowed to publish any content of this project. </li>
<li> Any form of plagiarism is strictly forbidden and will result in removal from the program. </li>

## Requirements
## General
<li> Allowed editors: vi, vim, emacs </li>
<li> All your files will be interpreted on Ubuntu 20.04 LTS </li>
<li> All your files should end with a new line </li>
<li> A README.md file, at the root of the folder of the project, is mandatory </li>
<li> All your Bash script files must be executable </li>
<li> Your Bash script must pass Shellcheck (version 0.7.0 via apt-get) without any error </li>
<li> The first line of all your Bash scripts should be exactly #!/usr/bin/env bash </li>
<li> The second line of all your Bash scripts should be a comment explaining what is the script doing </li>

## More Info
<li> For those who want to know more and learn about all signals, check out this article. </li>

## Table of contents
Files |  | Description
------|--|-------------
[0-what-is-my-pid](./0-what-is-my-pid) | A Bash script that displays its own PID.
[1-list_your_processes](./1-list_your_processes) | A Bash script that displays a list of currently running processes.
[2-show_your_bash_pid](./2-show_your_bash_pid) | A Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.
[3-show_your_bash_pid_made_easy](./3-show_your_bash_pid_made_easy) |  A Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.
[4-to_infinity_and_beyond](./4-to_infinity_and_beyond) | A Bash script that displays To infinity and beyond indefinitely.
[5-dont_stop_me_now](./5-dont_stop_me_now) | A Bash script that stops 4-to_infinity_and_beyond process.
[6-stop_me_if_you_can](./6-stop_me_if_you_can) | A Bash script that stops 4-to_infinity_and_beyond process.
[7-highlander](./7-highlander) | A Bash script that displays.
[8-beheaded_process](./8-beheaded_process) | A Bash script that kills the process 7-highlander.
[100-process_and_pid_file](./100-process_and_pid_file) | A Bash script that; Creates the file <code> /var/run/myscript.pid  </code> containing its <code> PID </code> , Displays To infinity and beyond indefinitely, Displays I hate the kill command when receiving a <code> SIGTERM signal</code> , Displays <code> Y U no love me?! </code> when receiving a <code> SIGINT signal</code>, Deletes the file <code> /var/run/myscript.pid </code> and terminates itself when receiving a <code> SIGQUIT or SIGTERM signal </code>.
[101-manage_my_process](./101-manage_my_process) |  | [manage_my_process](./manage_my_process) | Bash script that; Indefinitely writes I am alive! to the file /tmp/my_process, In between every I am alive! message, the program should pause for 2 seconds.
[102-zombie.c](./102-zombie.c) | A C program that creates 5 zombie processes.

## Student name 
Joseph Kakai

## Cohort 
9
