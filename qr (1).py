#!/usr/bin/python3
import webbrowser
from googlesearch import search
import qrcode
q=input()
lix=[]
b=0
for j in search(q, tld="com", num=3, start=0, stop=3, pause=2.0):
	lix.append(j)
for i in lix:
	b=b+1
	a="qr"+str(b)+".jpeg"
	qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)
	qr.add_data(i)
	qr.make(fit=True)
	img=qr.make_image()
	img.save(str(a))
