#!/usr/bin/env python
import curses

def main(win):
	win.nodelay(True) # make getkey() not wait
	x = 0
	while True:
		#just to show that the loop runs, print a counter
		#win.clear()
		win.addstr(0,0,str(x))
		x += 1
		
		try:
			key = win.getkey()
		except: # in no delay mode getkey raise and exeption if no key is press 
			key = None
		if key == " ": # of we got a space then break
			break

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

curses.wrapper(main)