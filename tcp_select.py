#!/usr/bin/env python

from select import select
import socket
import sys

def run(HOST=None,PORT=None):
	a=open('a')
	endp=a.read()
	a.close()
	global ssock
	ssock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		ssock.bind((HOST,PORT))
	except:	
		HOST=''
		PORT=int(sys.argv[1])
		ssock.bind((HOST,PORT))
	else:
		raise IndexError("You need to provide a port number from command line.")
	global inp
	inp = [ssock]
	addrs = {}
	while True:
		try:
			inputready,outputready,exceptready = select(inp, [], [])
			for i in inputready:
				if i == ssock:
					ssock.listen(1)
					conn,addr = ssock.accept()
					#print (conn,addr)
					inp.append(conn)
					#sette=None
									
					addrs[addr[0]] = conn
						
				else:
					data = i.recv(65536).strip()
					#print data
					for j in addrs.items():
						try:
							if data not in [endp, '']:
								msg=j[0]+" : "+data
								print msg
								j[1].send(msg)
							else:
								addrs[j[0]].close()
								inp.remove(addrs[j[0]])
								#addrs[j[0]]=None
								
						except:
							addrs[j[0]].close()
						#	addrs[j[0]]=None
		except: return

run()
ssock.close()
for i in inp:
	i.close()
