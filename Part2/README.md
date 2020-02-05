# Security-Suite >> P2_PwdCracker
##### Author: Michael Meisinger
##### Language: Python 3.7.4
##### Date Created: December 2018
##### Date Last Updated: February 2020

<br/>

### Description:
    Your standard MD5 password cracker. Uses a pre-generated rainbow table as well as a dictionary file.
    Read on for more detailed information.

<br/>

### Files included:
1. cracker.py
1. hash.txt
1. dictionary.txt
1. rainbow.txt

<br/>

### How to *run*:
    Type "python cracker.py" to start the program.
    Example: ~$ python cracker.py

<br/>

### How to *use*:

**cracker.py**
* Terminal-based menu that attempts to crack the password of "hash.txt" or quits.
* You can edit the password to be cracked in "hash.txt" in between attempts. See below.
* When cracking, cracker.py will...
  1. Compare hash against the pre-generated hashes stored in "rainbow.txt".
  1. Try every permutation of 1-3 special chars/numbers before/after every word stored in "dictionary.txt".
  1. Upon success, display password and the time it took to crack.
  1. Upon failure, display failure message and the time it took trying.
  * ** Brute Force takes so long to run, since implementing in my code it has not run to completion. **
* If there is no "hash.txt" file, cracker.py will exit with proper error message.
* If there is no "rainbow.txt" file, cracker.py will exit with proper error message.
* When brute forcing if there is no "dictionary.txt" file, cracker.py will exit with proper error message.
  * This error ("dictionary.txt") will only trigger if the program begins to brute force type2 passwords.
  * cracker.py will still crack regular dictionary words in its rainbow table even if there is no "dictionary.txt" file.
		
<br/>

### How to crack a different hash:
#### Option1
* Open "hash.txt".
* Replace current hash with desired hash.
* Run program again.
#### Option2
* Open "cracker.py" in text editor.
* Locate line 55.
* Change "hash.txt" to desired file name.
* Desired file should still abide by the structure of hash.txt, as described below.

<br/>
		
### Structure of "hash.txt":
* One line holding the hash to be cracked.
* A bad hash or blank file will result in extremely long run time, as the program will still check every permutation of every word in "dictionary.txt".

<br/>

### Structure of "rainbow.txt":
* First line is plain text dictionary word.
* Next line is the corresponding md5 password hash.
* And so on.

<br/>

### Structure of "dictionary.txt":
* Used to brute force the type2 passwords.
* List of dictionary words.
* Should be one word per line.

<br/>

### Other:
* *You will need Python on the local machine to run.*
* *Make sure you are in the correct directory AKA P2_PwdCracker.*
