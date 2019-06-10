#!/usr/bin/python3
from datetime import datetime
n=datetime.now()
a=input("enter your name--->:")
d=n.strftime("%H")
if d>='06' and d<='11':
	print("good morning")
elif d>='12' and d<='3':
	print("good afternoon")
elif d>='4' and d<='7':
	print("good evening")
else:
	print("good night")


