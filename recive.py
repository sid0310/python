#!/usr/bin/python2
import socket
r_ip="127.0.0.1"
r_port=4444
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((r_ip,r_port))
data=s.recvfrom(100)
print(data)
