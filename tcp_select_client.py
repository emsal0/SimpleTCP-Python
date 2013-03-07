#!/usr/bin/env python

import thread
import sys
import socket

def get_input(ssock):
	while True:
		msg = raw_input().strip()
		ssock.send(msg)

ssock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
	HOST=sys.argv[1]
	PORT=int(sys.argv[2])
except:
	raise IndexError("You have to supply a host and port number.")

ssock.connect((HOST,PORT))

thread.start_new_thread(get_input,(ssock,))
while True:
	data = ssock.recv(65536)
	if data != '':
		print data
a=open('a')
ssock.send(a.read())
ssock.close()
a.close()
		
