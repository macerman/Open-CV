#--CONTOURS and SHAPE DETECTION--#

import cv2
import numpy as np

#Function for detecting shapes and contouring
def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #creating our contours
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area) #detecting our area
        if area > 500:
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3) #drawing contours
            perimeter = cv2.arcLength(cnt,True)
            #print(perimeter)
            approx = cv2.approxPolyDP(cnt,0.02*perimeter,True)
            print(len(approx)) #detecting number of corners
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx) #we are rectangling around the shapes

            #detecting the shape name
            if objCor == 3: objectType = "Triangle"
            elif objCor == 4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio < 1.05: objectType = "Square"
                else: objectType = "Rectangle"
            elif objCor > 4: objectType = "Circle"
            else: objectType = "None"

            #showing shape names
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.4,(0,0,0),2)

path = "sources/shapes.png"
img = cv2.imread(path)

imgContour = img.copy() #our contour image

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #gray scale
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1) #higher sigma more blur
imgCanny = cv2.Canny(imgBlur,50,50) #edges
getContours(imgCanny) #contoured edge image

cv2.imshow("Original", img)
cv2.imshow("Gray", imgGray)
cv2.imshow("Blur", imgBlur)
cv2.imshow("Edges",imgCanny)
cv2.imshow("Contour", imgContour) #the result pic
cv2.waitKey(0)