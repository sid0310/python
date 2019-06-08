#!/usr/bin/python3
import webbrowser
from googlesearch import search
q=input()
lix=[]
lix1=[]
for j in search(q, tld="com", num=5, start=0, stop=5, pause=2.0):
	lix.append(j)
for i in lix:
	print(i)
for i in lix:
	q=lix
	for y in search('q', tld="com", num=5, start=0, stop=5, pause=2.0):
		lix1.append(y)
for i in lix1:
	print(i)