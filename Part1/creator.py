# Part 1, Program 1 - ID & Pwd creator
# Final Project - Computer Security
# Author: Michael Meisinger



import hashlib										# For md5 functionality

#-- Functions --#

def checkUsrName(usrName):
	try:
		shadow = open("password.txt", "r")				# Open up password file
		usrNameList = shadow.readlines()				# Move to list variable
		i = 0
		for x in usrNameList:
			if (i%2 == 0):								# Only the user names, ignore password hashes
				if (x.strip() == usrName.strip()):		# Compare names
					shadow.close()
					return False						# username is not unique, RETURN false
			i+=1
		shadow.close()									# Close file
		return True										# username is unique, RETURN true
		
	except IOError:
		madeFile = open("password.txt", "w+")			# Create "password.txt" file
		return True
	
	
def addAccount():
	valid = False
	while (not valid):
		usrName = input("Enter username: ")
		usrName = usrName.strip()
		valid = checkUsrName(usrName)
		if valid:
			pwd = input("Enter password for " + usrName + ": ")
			pwd = pwd.strip()
			h = hashlib.md5(pwd.encode())
			h = h.hexdigest()
			sf = open("password.txt", "a")
			sf.write(usrName + "\n")
			sf.write(h + "\n")
			sf.close()
			return
		elif not valid:
			print("Username is already taken. Please choose another.")
		else:
			print("What happened!?")
			return
	

#-- Main Sequence --#
keepGoing = True
choice = 0

while(keepGoing):
	print("What would you like to do? \n [0] Create a new account. \n [1] Quit.")
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
	
	# Add account	
	elif choice == 0:
		addAccount()
		
	# Incorrect number
	else:
		print("Incorrect input detected, please read instructions carefully. \n")
		
	
quit()
