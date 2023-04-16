#!/usr/bin/python3

import socket
import sys

if len(sys.argv) != 2:
	print ("Usage: vrfy.py <username>")
	sys.exit(0)
	
# Create a Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the Server
connect = s.connect(('10.10.10.10',25))  # CHANGE THIS   

# Receive the banner
banner = s.recv(1024)
print (banner)

# verify a user
username = bytes(sys.argv[1], "UTF-8")
s.send(b'VRFY ' + username + b'\r\n')
result = s.recv(1024)
print (str(result))

# Close the socket
s.close()
