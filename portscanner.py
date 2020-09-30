#!/bin/python3	
import sys
import socket
from datetime import datetime as dt
#Define _ targate
if len(syrgv)==2:
	target = sockthostbyname(sys.argv[1])
else:
	print ("Invalid Ammount of arguments: ")
	print ("Syntax: python3 scanner.py <ip>")
#Add a preety banner

print ("-"*50)
print ("Scanning Target " +targ)
print ("Time Stated: " +str(dtow()))
print ("-*50)

try: 
	for port in range (1,65535):
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(0.0000000000000001)
		result = s.connect_ex((target,port))
		#print ("cheaking port {}" rmat(port))
		if result ==0:
			print ("pt {} is open".format(port))
		s.close()
except keyboardInterrupt:
	print ("\n Exiting Prog)
	sys.exit()
except socket.error:
	print ("Couldn't connect tthe server.")
	syexit()
