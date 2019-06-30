#!/usr/bin/python
import cv2
#strarting camera
cap=cv2.VideoCapture(0)
plugin=cv2.VideoWriter_fourcc(*'XVID')
output=cv2.VideoWriter('class.avi',plugin,20,(640,480))

while cap.isOpened() :
	status,frame=cap.read()
	cv2.imshow('live',frame)
	output.write(frame)# sending data to VideoWriter
	if cv2.waitKey(10) & 0xff == ord('q') :
		break
	
cv2.destroyAllWindows()
# to close camera
cap.release()