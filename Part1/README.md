# Security-Suite >> P1_Authenticator
##### Author: Michael Meisinger
##### Language: Python 3.7.4
##### Date Created: December 2018
##### Date Last Updated: February 2020

<br/>

### Description:
	The user authenticator uses two programs to create user/password-hash combos as well as verify logins.
	Both programs use the file "password.txt" to achieve this. Read on for more detailed information.

<br/>

### Files included:
1. creator.py
1. authentication.py
1. password.txt

<br/>

### How to *run*:
	Type "python creator.py" or "python authentication.py" to start either program.
	Example: ~$ python creator.py
	Example: ~$ python authentication.py

<br/>

### How to *use*:

**creator.py**
* Terminal-based menu that either adds an account or quits.
* When adding account, checks to make sure username is unique.
* If username is unique, then md5 hash the password and store them in "password.txt".
* If there is no "password.txt" file, creator.py will create it.

**authentication.py**
* Terminal-based menu that either verifies a login or quits.
* When verifying the login, prompts user for username and password.
* First searches "password.txt" for a matching username, if none then authentication fails.
* If there is no "password.txt" file, authentication attempt will fail.
* If matching username, compares the password hashes, if match then login is successful.
		
<br/>
		
### Structure of "password.txt":
* First line is username.
* Next line is the corresponding password hash.
* And so on.
* **Leave a blank line at the end of file.**

<br/>

### Other:
* *You will need Python on the local machine to run.*
* *Make sure you are in the correct directory AKA P1_Authenticator.*
* **Leave a blank line at the end of "password.txt".**
