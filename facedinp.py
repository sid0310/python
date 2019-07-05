#!/usr/bin/python
import cv2 
import sys
import numpy as np
n=0
lx=[]
ly=[]
lh=[]
lw=[]
casclf=cv2.CascadeClassifier('face.xml')
data=sys.argv[1]

cap=cv2.VideoCapture(data)
status,frame=cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
face=casclf.detectMultiScale(gray,1.3,5)
	#print(face)
for x,y,h,w in face:
	lx.append(x)
	ly.append(y)
	lh.append(h)
	lw.append(w)
	facedata=gray[ly[n]:ly[n]+lw[n],lx[n]:lx[n]+lh[n]]
	cv2.imwrite('faceffff'+str(n)+'.jpeg',facedata)
	n=n+1
	cv2.rectangle(gray,(x,y),(x+h,y+w),(0,0,255),2)
cv2.imshow('face',gray)
	#break
	#if cv2.waitKey(0) & 0xff == ord('q'):
		#break
cv2.waitKey(0)
cv2.destroyAllWindows()
cap.release()