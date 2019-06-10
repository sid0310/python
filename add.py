import crypt
import os
import string
import re

l=[]
input_string = input("Enter a list element separated by space: ")
l=input_string.split()
h="hello"
for i in l:
	f=1
	for j in i:
		if j.isdigit():
			f=0
			continue
		
	if f == 1:	
		a=h+i
		encPass = crypt.crypt(a,"22")
		os.system("useradd -p "+encPass+" "+i)
	else:
		print(i+" useradd not possible")
	
