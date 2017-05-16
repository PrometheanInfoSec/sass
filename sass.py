#!/usr/bin/env python

HOST = ''
PORT = 5566

import random
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)

while True:
	con, adr = s.accept()
	data = con.recv(1024)
	temp = []
	for i in xrange(len(data)):
		x = random.randint(0,10)
		if x > 4:
			temp.append(data[i].lower())
		else:
			temp.append(data[i].upper())

	data = "".join(temp)
	con.sendall(data)
	con.close()
	print data
