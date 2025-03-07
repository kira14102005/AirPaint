import cv2
import mediapipe as mp
import time
import HandTrackingModule as hm
import os
import math

directory = "CanvaImage"
myList  = os.listdir(directory)
print(myList)
headerImages = []
for imgPath in myList:
    img = cv2.imread(f'{directory}/{imgPath}')
    headerImages.append(img)
 