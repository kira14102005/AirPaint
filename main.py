import cv2
import mediapipe as mp
import time
import HandTrackingModule as hm
import os
import math

directory = "CanvaImage\Header"
myList  = os.listdir(directory)
print(myList)
headerImages = []
for imgPath in myList:
    img = cv2.imread(f'{directory}/{imgPath}')
    headerImages.append(img)
currHeader = headerImages[0]
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    #Detect the hands
    detector = hm.handDetectorObj()
    img = detector.detectHands(img)
    lmrkArray = detector.findHandPosition(img , toDraw=False)
    if(len(lmrkArray) != 0):
        # print(lmrkArray)

        #TIp of the index and middle finger
        x1, y1 = lmrkArray[8][1], lmrkArray[8][2]
        x2, y2 = lmrkArray[12][1], lmrkArray[12][2]
    
        fingers = detector.noOfFingersUp()
        print(fingers)

        if(fingers[1] and fingers[2]):
            cv2.rectangle(img, (x1,y1-25), (x2,y2+25), (255,0,255), cv2.FILLED)
            print("Selection Mode")
            if y1 < 125:
                if 200 < x1 < 280:
                    currHeader = headerImages[0]
                elif 435 < x1 < 510:
                    currHeader = headerImages[1]
                elif 635 < x1 < 715:
                    currHeader = headerImages[2]
                elif 850 < x1 < 975:
                    currHeader = headerImages[3]
                elif 1050 < x1 < 1160:
                    currHeader = headerImages[4]
            #Checking for the header change
        
        if(fingers[1] and fingers[2] == False):
            cv2.circle(img, (x1,y1), 15, (255,0,255), cv2.FILLED)
            print("Drawing Mode")
    #set the header image
    img[0:125, 0:1280] = currHeader
    cv2.imshow("Feed", img)
    cv2.waitKey(1)





# RULES : 
# 1.Selection Mode  : Two Fingers point up
# 2.Drawing Mode : One Fingers point up
