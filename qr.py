#!/usr/bin/python3
import webbrowser
from googlesearch import search
import pyqrcode
q=input()
lix=[]
b=0
for j in search(q, tld="com", num=3, start=0, stop=3, pause=2.0):
	lix.append(j)
for i in lix:
	b=b+1
	a="qr"+str(b)+".svg"
	url=pyqrcode.create(str(lix))
	url.svg(a,scale=8)
	
