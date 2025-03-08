import cv2
import mediapipe as mp
import time
import HandTrackingModule as hm
import os
import math
#########
brushWeight = 15
prev_x, prev_y = 0, 0
#########

directory = "CanvaImage\Header"
myList  = os.listdir(directory)
print(myList)
headerImages = []
for imgPath in myList:
    img = cv2.imread(f'{directory}/{imgPath}')
    headerImages.append(img)
currHeader = headerImages[0]
drawColor = (255, 0, 0) #By default Red COlor
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
            cv2.rectangle(img, (x1,y1-25), (x2,y2+25), drawColor, cv2.FILLED)

            print("Selection Mode")
            if y1 < 125:
                if 200 < x1 < 280:
                    currHeader = headerImages[0]
                    drawColor = (255, 0, 0) #Red
                elif 435 < x1 < 510:
                    currHeader = headerImages[1]
                    drawColor = (0, 255, 0) #Green
                elif 635 < x1 < 715:
                    currHeader = headerImages[2]
                    drawColor = (255, 255, 0) #yellow
                elif 850 < x1 < 975:
                    currHeader = headerImages[3]
                    drawColor = (0, 0 ,255) #blue
                elif 1050 < x1 < 1160:
                    currHeader = headerImages[4]
        
        if(fingers[1] and fingers[2] == False):
            cv2.circle(img, (x1,y1), 15, drawColor, cv2.FILLED)
            print("Drawing Mode")
            if(prev_x == 0 and prev_y == 0):
                prev_x, prev_y = x1, y1
            cv2.line(img, (prev_x,prev_y), (x1,y1), drawColor, brushWeight)
            prev_x, prev_y = x1, y1
    #set the header image
    img[0:125, 0:1280] = currHeader
    cv2.imshow("Feed", img)
    cv2.waitKey(1)





# RULES : 
# 1.Selection Mode  : Two Fingers point up
# 2.Drawing Mode : One Fingers point up
