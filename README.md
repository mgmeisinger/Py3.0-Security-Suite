# Py3.7-Security-Suite
### Author: Michael Meisinger
##### Language: Python 3.7.4
##### Date Created: December 2018
##### Date Last Updated: February 2020

<br/>

#### Description:
	Terminal-based system with three parts: User Authenticator, Pwd Cracker, Pwd Evaluator.
###### User Authenticator
* Users can create a username/password combo that will store both the username and the password's md5 hash in a txt file.
* Users can then attempt to login to the system using the same txt file.
* System converts password to md5 hash and compares; success or failure result displayed.
###### Password Cracker
* Program takes an md5 hash and returns the plaintext password.
* Cracker tries a rainbow table first then permutations of a dictionary file.
* Will display a success or failure and give the time it took to run.
* Brute forcing the entire dictionary file takes a long time to run.
###### Password Evaluator
* The system will prompt the user for a password and return a rating on that password's strength.
* System will check a dictionary file to see if any words are an exact match or a substring of the given password.
* The given password will be rated as strong, moderate (substring), or weak (exact match) against dictionary attacks.
#### How to use:

	Enter a directory and skim that part's README for further directions on commands and supporting files.

<br/>

*-You will need Python 3.7.4 on the local machine to run.* <br/>
*-Older versions of Python (2.\*) will result in errors due to syntax changes.* <br/>
*-Make sure you are in the correct directory.*
