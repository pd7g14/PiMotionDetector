import nmap
import csv
import time

def scanNetwork():
	print "Network Scan Started"
	#Create nmap instanse and ping scan network
	nm = nmap.PortScanner()
	nm.scan(hosts='192.168.1.254/24', arguments='-sP')
	#Define the list where mac addresses will be stored
	macAddresses = []
	for host in nm.all_hosts():
		#Get all hosts that are up but ignore this pi
		if nm[host]['status']['state']  == 'up' and nm[host]['addresses']['ipv4'] != '192.168.1.104':
			#Print the pi and fallback to all addresses if does not exist 
			#try: print nm[host]['addresses']['mac'] #Get device name for debugging , nm[host]['hostnames'][0]['name']
			#except: print nm[host]['addresses']
			try: macAddresses.append(nm[host]['addresses']['mac'])
			except: print "something has broken"
	return macAddresses
#Scan the network
scan1 = scanNetwork();
while True:
	print "Network Scan Ended"
	scan2 = scanNetwork();
	print "Items still in network" , set(scan1) & set(scan2)
	print "Items no longer in network", set(scan1) - set(scan2)
	print "Items that are now in network", set(scan2) - set(scan1)
	scan1 = scan2
	time.sleep(30)



#Write the current mac addresses to a file 
#with open("currentmac.csv", "w") as file:
#	writer = csv.writer(file)
#	writer.writerows([macAddresses])


	


