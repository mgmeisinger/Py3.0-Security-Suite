# Security-Suite >> P3_PwdEvaluator
##### Author: Michael Meisinger
##### Language: Python 3.7.4
##### Date Created: December 2018
##### Date Last Updated: February 2020

<br/>

### Description:
    Terminal-based menu that either evaluates a prompted password or quits.
    The given password will be evaluated as strong, moderate, or weak against dictionary attacks.
    If any word in "dictionary.txt" is a match to the given password it is weak.
    If any word in "dictionary.txt" is a substring to the given password it is moderate.
    Read on for more detailed information.

<br/>

### Files included:
1. evaluator.py
1. dictionary.txt

<br/>

### How to *run*:
    Type "python evaluator.py" to start the program.
    Example: ~$ python evaluator.py

<br/>

### How to *use*:

**evaluator.py**
* Terminal-based menu that either evaluates a prompted password or quits.
* When When evaluating a password, evaluator.py will...
  1. Check to see if it is an exact match with any word in "dictionary.txt".
  1. Check to see if any dictionary word is substring of password.
      1. Excludes dictionary words of 1 or 2 letters.
  * If not weak or moderate then the password is strong.
  * ** If there is no "dictionary.txt" file, evaluator.py will exit with proper error message. **

<br/>

### Structure of "dictionary.txt":
* List of dictionary words.
* Should be one word per line.

<br/>

### Other:
* *You will need Python on the local machine to run.*
* *Make sure you are in the correct directory AKA P3_PwdEvaluator.*
