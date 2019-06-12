#!/usr/bin/python3
import re
import os
f=open("a.txt","r")
s=input("enter the command---->")
a=s+'\n'
l=[]
for i in f:
	l.append(i) 
for i in l:
	if a==i:
		flag=0	
		break
	else:
		flag=1		
if flag==0:
	os.system(" "+s)
	os.system("echo "+s+" >>w.txt")
else:
	print("no")
	os.system("echo "+s+" >>w.txt")
f.close()
f=open("w.txt","r")
f.seek(0)
for i in f:
	if a==i:
		b=0
		break
	else:
		b=1
if b==0:
	os.system("festival --tts q.txt")

