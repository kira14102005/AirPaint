#STarting to make a HandTracking Module using CV2 and MediaPipe
import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
handObj = mp.solutions.hands
hands = handObj.Hands()
while True:
    success, img = cap.read()
    imRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imshow("Image", img) 
    cv2.waitKey(1)