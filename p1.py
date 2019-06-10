#!/usr/bin/python3
from datetime import datetime
a=input("enter your name-->")
b=int(input("enter your age-->"))
n=datetime.now()
d=int(n.strftime("%Y"))
print("the year you will be 95")
c = d-b
e = c+95
print(e)
