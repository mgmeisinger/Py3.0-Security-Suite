# Part 2 - Password cracker
# Final Project - Computer Security
# Author: Michael Meisinger


import hashlib										# For md5 functionality
import time											# For program execution timing

#-- Functions --#

def permute(wordToPermute):					# Takes a string, gets all permutations, returns a list.
	possChars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
	permList = []
	for x in possChars:
		permList.append(wordToPermute + x)
		permList.append(x + wordToPermute)
		for y in possChars:
			permList.append(wordToPermute + x + y)
			permList.append(x + wordToPermute + y)
			permList.append(x + y + wordToPermute)
			for z in possChars:
				permList.append(wordToPermute + x + y + z)
				permList.append(x + wordToPermute + y + z)
				permList.append(x + y + wordToPermute + z)
				permList.append(x + y + z + wordToPermute)
	return permList


def brute(toBeCracked):				# Takes a hash, checks all type2 pwds, returns password upon success
											# returns Null upon no match.
	try:
		dh = open("dictionary.txt", "r")
		ptList = []
		ptList = dh.readlines()
		dh.close()
		for w in ptList:
			permList = permute(w.strip())
			for p in permList:
				hashed = hashlib.md5(p.strip().encode())
				hashed = hashed.hexdigest()
				if (hashed == toBeCracked):
					return p
		return None

	except IOError:
		print("No \"dictionary.txt\" file in directory.\nCheck \"README.TXT\" for instructions.\nSystem Exit.")
		quit()

def pwdCracker():
	try:
		fh = open("hash.txt", "r")
		start = time.time()
		pwdToBeCracked = fh.readline()
		pwdToBeCracked = pwdToBeCracked.strip()
		fh.close()
		try:
			sh = open("rainbow.txt", "r")
			print("Cracking: " + pwdToBeCracked)
			wholeList = []
			wholeList = sh.readlines()
			sh.close()
			li = 0
			ptList = []
			hashList = []
			for l in wholeList:
				if (li%2 == 0):
					ptList.append(l)
				else:
					hashList.append(l)
				li +=1
			sh.close()
			cracked = False
			i = 0
			for x in hashList:
				x = x.strip()
				if (x == pwdToBeCracked):
					cracked = True
					break
				i+=1
			if (cracked):
				end = time.time()
				print("\nPassword succesfully cracked: " + ptList[i])
				print("Time to crack: %s seconds\n" % (end - start))
				return
			else:
				bruteWord = brute(pwdToBeCracked)
				end = time.time()
				if bruteWord == None:
					print("\nPassword not found. Better luck next year.")
					print("Time wasted cracking: %s seconds\n" % (end - start))
					return
				else:
					print("\nPassword succesfully cracked: " + bruteWord)
					print("Time to crack: %s seconds\n" % (end - start))
					return
			
		except IOError:
			print("No \"rainbow.txt\" in directory.\nCheck \"README.TXT\" for instructions.\nSystem Exit.")
			quit()
			
	except IOError:
		print("No \"hash.txt\" file storing an md5 password hash found.\nCheck \"README.TXT\" for instructions.\nSystem Exit.")
		quit()


#-- Main Sequence --#

keepGoing = True
choice = 0

while(keepGoing):
	print("What would you like to do? \n [0] Crack the password in \"hash.txt\". \n [1] Quit.")
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
	
	# Run Password Cracker!!!!	
	elif choice == 0:
		pwdCracker()
		
	# Incorrect number
	else:
		print("Incorrect input detected, please read instructions carefully. \n")
		
	
quit()
