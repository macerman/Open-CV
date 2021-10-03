#--RESIZING and CROPPING--#

import cv2

img = cv2.imread("sources/lambo.jpg")
print("Image:", img.shape) # (height, width, channel) 3 channel is BGR

imgResize = cv2.resize(img,(300,300)) # (width, height)
print("Resized:", imgResize.shape)

imgCropped = imgResize[50:150,100:300] # [heightStart:heightEnd,widthStart:widthEnd]

cv2.imshow("Lamborghini", img)
cv2.imshow("Resized", imgResize)
cv2.imshow("Cropped", imgCropped)
cv2.waitKey(0)