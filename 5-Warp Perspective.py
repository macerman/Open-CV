#--WARP PERSPECTIVE--#

import cv2
import numpy as np

img = cv2.imread("sources/cards.jpg")

#finding and defining our card's corners' point cordinates
width,height = 250,350 #a normal playing card is probably 2.5-3.5 inches
points1 = np.float32([[117,57],[201,106],[51,164],[132,215]]) #to find the coordinates of corners you can use mspaint
points2 = np.float32([[0,0],[width,0],[0,height],[width,height]]) #assigning corners
matrix = cv2.getPerspectiveTransform(points1,points2) #making our img with these points
imgOutput = cv2.warpPerspective(img,matrix,(width,height)) #warp image is ready

cv2.imshow("Image", img)
cv2.imshow("Warp Output", imgOutput)

cv2.waitKey(0)