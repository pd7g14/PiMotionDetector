def createUser():
	name = input("Please enter a username ")
	mac = input("Please enter a device MAC address ")
	writeLn = name + "|" + mac + "\n"
	with open("users.txt", "a") as userFile:
		userFile.write(writeLn)

def deleteUser():
	user = input("Which user would you like to delete? ")
	if checkUser(user):
		print("We found that user! Are you sure you wish to delete them?")
		confirm = input("Y/N? ")
		if confirm.lower() == "y":
			f = open("users.txt","r+")
			d = f.readlines()
			f.seek(0)
			for line in d:
				if user != line.split("|")[0]:
					f.write(line)
			f.truncate()
			f.close()
			print("Deleted!")
			return
		else:
			print("Not Deleted!")
			return
	else:
		print("Sorry we couldn't find that name")
		return

def checkUser(user):
	user = user.lower()
	with open("users.txt", "r") as userFile:
		for line in userFile:
			if user == line.split("|")[0]:
				return True
		return False




checkUser("Pip")
checkUser("mike")
deleteUser()
createUser()