#!/usr/bin/python
import cv2 
import sys
casclf=cv2.CascadeClassifier('face.xml')
data=sys.argv[1]
cap=cv2.VideoCapture(data)
while cap.isOpened() :
	status,frame=cap.read()
	face=casclf.detectMultiScale(frame,1.5,5)
	#print(face)
	for x,y,h,w in face:
		cv2.rectangle(frame,(x,y),(x+h,y+w),(0,0,255),2)
		facedata=frame[x:x+h,y:y+w]
		cv2.imwrite('face.jpeg',facedata)
	cv2.imshow('face',frame)
	#break
	if cv2.waitKey(2) & 0xff == ord('q'):
		break
cv2.destroyAllWindows()
cap.release()