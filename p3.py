#!/usr/bin/python3
adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
a1=[]
a2=[]
for i in adhoc:
	if i>5:
		print(i)
		a1.append(i)
for i in adhoc:
	if i<=2:
		print(i)
		a2.append(i)

