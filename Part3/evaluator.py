# Part 3 - Password evaluator
# Final Project - Computer Security
# Author: Michael Meisinger



#-- Functions --#

def weakCheck(pwd, ptList):					# Takes a plain text password and compares it to the plain text dictionary words.
	for x in ptList:
		if (x.strip() == pwd):
			return True
	
def modCheck (pwd, ptList):					# Takes a plain text password and looks for dictionary words (3 letters or more only)
											# 	that are a substring of that password.
	for y in ptList:
		y = y.strip()
		if (len(y) > 2):
			if (y in pwd):
				return True
	return False
	

def pwdEvaluator():
	try:
		fh = open("dictionary.txt", "r")
		ptList = []
		ptList = fh.readlines()
		fh.close()
		pwd = input("Enter password: ")
		pwd = pwd.strip()
		if (" " in pwd) or (pwd == ""):
			print("Error. Password must be all one word.\nPlease try again.")
			return
		isWeak = weakCheck(pwd, ptList)
		if (isWeak):
			print(pwd + " is weak to a dictionary attack.")
			return
		else:
			isMod = modCheck(pwd, ptList)
			if (isMod):
				print(pwd + " is moderate at best.")
				return
			else:
				print(pwd + " is a strong choice against a dictionary attack.")
		
	except IOError:
		print("No \"dictionary.txt\" file in directory.\nCheck \"README.TXT\" for instructions.\nSystem Exit.")
		quit()


#-- Main Sequence --#

keepGoing = True
choice = 0

while(keepGoing):
	print("What would you like to do? \n [0] Evaluate a password. \n [1] Quit.")
	try:
		choice = int(input("Enter number: "))
	# Incorrect Data type
	except ValueError:
		print("That's not a number!")
		choice = 5

	# Quit
	if choice == 1:
		print("Have a nice day!\nSystem exit.")
		keepGoing = False
		quit()
	
	# Run Password Evaluator!!!!	
	elif choice == 0:
		pwdEvaluator()
		
	# Incorrect number
	else:
		print("Incorrect input detected, please read instructions carefully. \n")
		
	
quit()
