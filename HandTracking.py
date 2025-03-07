#STarting to make a HandTracking Module using CV2 and MediaPipe
import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
handObj = mp.solutions.hands
hands = handObj.Hands()
drawObj  = mp.solutions.drawing_utils

prevTime = 0
while True:
    success, img = cap.read()
    imRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imRGB)
    # print(result.multi_hand_landmarks)  #To check if the hand is detected or not
    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks: #For each hand detected
            drawObj.draw_landmarks(img, hand, handObj.HAND_CONNECTIONS)
    curTime = time.time()
    fps = 1/(curTime-prevTime)
    prevTime = curTime
    cv2.imshow("Image", img) 
    cv2.waitKey(1)