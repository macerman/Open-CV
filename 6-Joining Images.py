#--JOINING IMAGES--#

import cv2
import numpy as np

img = cv2.imread("sources/tiat.jpg")

#the two images must have the same number of channels
hr = np.hstack((img,img)) #stacking our image on horizontal axis
vr = np.vstack((img,img)) #vertical axis stacking

cv2.imshow("Horizontal", hr)
cv2.imshow("Vertical", vr)

cv2.waitKey(0)