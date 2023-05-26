# Password Generator
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

## *Description*
This project allows you to create a random passwords based on user-specified criteria, such as length and character types. Includes practice using the random and string Python modules.
<br>
<br>

### ***Some notes about the Python String module:***<br>
 - string.ascii_lowercase: A string containing all lowercase letters of the English alphabet ("abcdefghijklmnopqrstuvwxyz").<br>
 - string.ascii_uppercase: A string containing all uppercase letters of the English alphabet ("ABCDEFGHIJKLMNOPQRSTUVWXYZ").<br>
 - string.digits: A string containing all decimal digits ("0123456789").<br>
 - string.punctuation: A string containing all ASCII punctuation characters (!"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~`).<br>
 - These will be used to create a string of all possible characters to choose from when generating the password based on the user's input.
<br>
<br>

## *Installation & Usage*
To install this app, simply clone the repository and run the `password-generator.py` file in your terminal.
<br>
<br>
When prompted:<br>
 - Choose the length of your password<br>
&emsp; - The limitations of the Random module limits the generator to be between 8 - 128 characters<br>
&emsp; - Due to using  `"".join(random.choice(character_pool) for _ in range(length))`, the password can be any `length` that the user specifies.<br>
 - Choose whether to include lowercase letters<br>
 - Choose whether to include uppercase letters<br>
 - Choose whether to include numbers<br>
 - Choose whether to include special characters<br>
<br>

![screenshot](images/screenshot.JPG)
<br>

## *Questions*
<h3>Portfolio:&emsp;<a href="https://jk377y.dev" target="_blank">https://jk377y.dev</a></h3>
<h3>Email:&emsp;<a href="mailto:jk377y@gmail.com" target="_blank">jk377y@gmail.com</a></h3>
<h3>LinkedIn:&emsp;<a href="https://www.linkedin.com/in/james-kelly-software-developer/" target="_blank">https://www.linkedin.com/in/james-kelly-software-developer/</a></h3>
<h3>GitHub:&emsp;<a href="https://github.com/jk377y" target="_blank">https://github.com/jk377y</a></h3>
<br>
<br>

## *License*
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
<br>Copyright (c) 2023 James Kelly
<br>Information on this license can be found at: (https://opensource.org/licenses/MIT)