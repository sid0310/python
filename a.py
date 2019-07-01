#!/usr/bin/python3
import cv2
import numpy as np
import sys
data1=sys.argv[1]
data2=sys.argv[2]
img1=cv2.imread(data1)
img2=cv2.imread(data2)
img3=np.append(img1,img2,axis=1)
print(img3.shape)
img4=np.append(img3,img3,axis=0)
cv2.imshow('a.jpg',img4)
cv2.waitKey(0)