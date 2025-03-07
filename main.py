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
        print(lmrkArray)
    #set the header image
    img[0:125, 0:1280] = currHeader
    cv2.imshow("Feed", img)
    cv2.waitKey(1)





# RULES : 
# 1.Selection Mode  : Two Fingers point up
# 2.Drawing Mode : One Fingers point up
