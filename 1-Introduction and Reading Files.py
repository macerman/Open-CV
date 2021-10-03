#--READ IMAGES, VIDEOS and WEBCAM--#

import cv2
print("Package Imported.")

#-MAKING A WINDOW WITH AN IMAGE--#
'''img = cv2.imread("sources/tiat.jpg") #Assigning the picture

cv2.imshow("Fish", img) #Creating a window with the said title
cv2.waitKey(0) #0 means forever and other numbers are in ms type
'''

#--MAKING A WINDOW WITH A VIDEO--#

#capture = cv2.VideoCapture("sources/tiat.mp4") #Defining the video

capture = cv2.VideoCapture(0) #Defining a webcam
capture.set(3,640) #Width id is 3, and the value is 640
capture.set(4,480) #Height id is 4, and the value is 480
capture.set(10,100) #Brightness id is 10, and the value is 100

while True:
    success, img = capture.read() #Making the video a window
    cv2.imshow("Video", img) #Importing video window
    if cv2.waitKey(1) & 0xFF ==ord('q'): #Assign key q to exit
        break