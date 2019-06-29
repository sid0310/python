#!/usr/bin/python3

import cgi
import cgitb
import subprocess
from googlesearch import search
# to show common error in browser
cgitb.enable()

print("Content-type:text/html")
print("")

#this will collect all the html code with data
webdata=cgi.FieldStorage()
#now extracting value of x
data=webdata.getvalue('x')
#sending output to server
lix=[]
for j in search(data, tld="com", num=5, start=0, stop=5, pause=2.0):
	lix.append(j)
for i in lix:
	print("<a href=")
	print(i)
	print(">")
	print(i)
	print("</a>")
	print("<br>")

