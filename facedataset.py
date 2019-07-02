#!/usr/bin/python
import cv2 
casclf=cv2.CascadeClassifier('face.xml')
cap=cv2.VideoCapture(0)
plugin=cv2.VideoWriter_fourcc(*'XVID')
output=cv2.VideoWriter('class2.mp4',plugin,25,(640,480))
n=0
while True :
	status,frame=cap.read()
	face=casclf.detectMultiScale(frame,1.3,5)
	#print(face)
	for x,y,h,w in face:
		facedata=frame[x:x+h,y:y+w]
		cv2.imshow('face',frame)
		cv2.imwrite('facedata'+str(n)+'.jpeg',facedata)
	n=n+1
	if cv2.waitKey(10) & 0xff == ord('q'):
		break
cv2.destroyAllWindows()
cap.release()