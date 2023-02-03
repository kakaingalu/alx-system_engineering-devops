# Regular expression

## Description
Introduction to Regular expression

## Background Context
<li> For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties. </li>

<li> Because the focus of this exercise is to play with regular expressions <code> (regex) </code> , here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //: </li>

<code> 
sylvain@ubuntu$ cat example.rb
<code> #!/usr/bin/env ruby </code>
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
Resources 
</code>

## Read or watch:

<li> Regular expressions - basics </li>
<li> Regular expressions - advanced </li>
<li> Rubular is your best friend </li>
<li> Use a regular expression against a problem: now you have 2 problems </li>
<li> Learn Regular Expressions with simple, interactive exercises </li>

## Requirements
## General
<li> Allowed editors: vi, vim, emacs </li>
<li> All your files will be interpreted on Ubuntu 20.04 LTS </li>
<li> All your files should end with a new line </li>
<li> A README.md file, at the root of the folder of the project, is mandatory </li>
<li> All your Bash script files must be executable </li>
<li> The first line of all your Bash scripts should be exactly <code> #!/usr/bin/env ruby </code> </li>
<li> All your regex must be built for the Oniguruma library </li>

## Table of contents
Files | Description
------|------------
[0-simply_match_school.rb](./0-simply_match_school.rb) | The regular expression must match School, Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method.
[1-repetition_token_0.rb](./1-repetition_token_0.rb) | Find the regular expression that will match the above cases, Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method.
[2-repetition_token_1.rb](./2-repetition_token_1.rb) |Find the regular expression that will match the above cases, Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method.
[3-repetition_token_2.rb](./3-repetition_token_2.rb) |Find the regular expression that will match the above cases, Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method.
[4-repetition_token_3.rb](./4-repetition_token_3.rb) | Find the regular expression that will match the above cases, Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method, Your regex should not contain square brackets.
[5-beginning_and_end.rb](./5-beginning_and_end.rb) | The regular expression must be exactly matching a string that starts with h ends with n and can have any single character in between, Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method.

