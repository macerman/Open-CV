#--SHAPES and TEXTS--#

import cv2
import numpy as np

#We are going to use the numpy library to create our matrix
#0 stands for black and 1 stands for white

img = np.zeros((512,512,3),np.uint8) # (height,width) and the channel, it gives us value range 0-255
#print(img)
#img[200:300,100:300] = 255,0,0 #whole image is img[:]

#the origin of the image is top left corner in OpenCV
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) #img.shape[1] is width and img.shape[0] is height. Now we got a diagonal line
cv2.line(img,(0,0),(300,300),(200,255,200),3) #image,start,end,color,thickness
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2) #start,end,color,thickness etc. Write cv2.FILLED instead of thickness if you want to fill ur shape
cv2.circle(img,(450,50),30,(255,255,0),5) #center,radius,color,thickness
cv2.putText(img," OPENCV ", (300,100),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,150,0),3) #text,position,font,scale,color,thickness etc. Scale=bigness

cv2.imshow("Matrix", img)

cv2.waitKey(0)