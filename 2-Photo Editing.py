#--BASIC FUNCTIONS---#

import cv2
import numpy as np

img = cv2.imread("sources/tiat.jpg")
kernel = np.ones((5,5),np.uint8) #Defining the kernel we're gon' use

#--EDITING and DETECTING--#
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #BGR equals to RGB in OpenCV and with this we convert the colors to gray scale
imgBlur = cv2.GaussianBlur(img, (7,7),0) #Blur, Add kernel value
imgEdge = cv2.Canny(img,100,100) #Two threshold values, detect the edges in pic
imgDilation = cv2.dilate(imgEdge,kernel,iterations=1) #Kernel and the iterations just makes edges thicker
imgEroded = cv2.erode(imgDilation,kernel,iterations=1) #Thinning the dilated image

cv2.imshow("Gray", imgGray)
cv2.imshow("Blur", imgBlur)
cv2.imshow("Edge", imgEdge)
cv2.imshow("Dilation", imgDilation)
cv2.imshow("Erode", imgEroded)
cv2.waitKey(0)