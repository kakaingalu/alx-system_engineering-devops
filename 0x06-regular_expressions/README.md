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
Use a regular expression against a problem: now you have 2 problems
Learn Regular Expressions with simple, interactive exercises
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 20.04 LTS
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
All your Bash script files must be executable
The first line of all your Bash scripts should be exactly #!/usr/bin/env ruby
All your regex must be built for the Oniguruma library
