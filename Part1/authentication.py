# Part 2, Program 1 - ID & Pwd verifier
# Final Project - Computer Security
# Author: Michael Meisinger



import hashlib										# For md5 functionality

#-- Functions --#

def login():
	usrName = input("Enter user name: ")
	usrName = usrName.strip()
	pwd = input("Enter password for " + usrName + ": ")
	pwd = pwd.strip()
	h = hashlib.md5(pwd.encode())
	h = h.hexdigest()
	try:
		shadow = open("password.txt", "r")				# Open up password file
		usrAndHashList = shadow.readlines()				# Move to list variable
		i = 0
		legit = False
		for x in usrAndHashList:
			if (i%2 == 0):								# Check username first
				if (x.strip() == usrName.strip()):			# Compare names
					if (h.strip() == usrAndHashList[i+1].strip()):		
						shadow.close()
						return True							# Username and pwd hash match, RETURN true
					else:
						shadow.close()
						return False							# Username and pwd hash DO NOT match, RETURN false
			i+=1										# Iterate through list
		shadow.close()									# Close file
		return False									# username is not in password file, RETURN false
	except IOError:
		print("No \"password.txt\" file.\nCheck \"README.TXT\" for instructions.")
		return False									# No "password.txt" file, RETURN false

#-- Main Sequence --#

keepGoing = True

while (keepGoing):
	print("What would you like to do? \n [0] Login. \n [1] Quit.")
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
	
	# Login verification	
	elif choice == 0:
		verified = login()
		if (verified):
			print("Login successful!")
		else:
			print("Login failed!")
		
	# Incorrect number
	else:
		print("Incorrect input detected, please read instructions carefully. \n")
		
	
quit()
