#!/usr/bin/python
import cv2 
import sys
casclf=cv2.CascadeClassifier('face.xml')
data=sys.argv[1]
n=0
n=0
lx=[]
ly=[]
lh=[]
lw=[]
cap=cv2.VideoCapture(0)
while cap.isOpened() :
	status,frame=cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	face=casclf.detectMultiScale(gray,1.5,5)
	for x,y,h,w in face:
		lx.append(x)
		ly.append(y)
		lh.append(h)
		lw.append(w)
		facedata=gray[ly[n]:ly[n]+lw[n],lx[n]:lx[n]+lh[n]]
		cv2.imwrite('facefffffgh'+str(n)+'.jpeg',facedata)
		n=n+1
		cv2.rectangle(frame,(x,y),(x+h,y+w),(0,0,255),2)
	cv2.imshow('face',frame)
	if cv2.waitKey(2) & 0xff == ord('q'):
		break
cv2.destroyAllWindows()
cap.release()