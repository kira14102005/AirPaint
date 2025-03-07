#STarting to make a HandTracking Module using CV2 and MediaPipe
import cv2
import mediapipe as mp
import time

class handDetectorObj():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        
        self.handObj = mp.solutions.hands
        self.hands = self.handObj.Hands()
        self.drawObj  = mp.solutions.drawing_utils
        self.handObj = mp.solutions.hands
        self.hands = self.handObj.Hands()
        self.drawObj  = mp.solutions.drawing_utils

    def detectHands(self, img, toDraw=True):
        imRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imRGB)
        if  self.results.multi_hand_landmarks:
            for hand in  self.results.multi_hand_landmarks: #For each hand detected
                if toDraw:
                    self.drawObj.draw_landmarks(img, hand, self.handObj.HAND_CONNECTIONS)
        return img

    def findHandPosition(self, img, handIdx=0, toDraw=True):
        self.lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handIdx]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                landMark_x, landMark_y = int(lm.x*w), int(lm.y*h)
                self.lmList.append([id, landMark_x, landMark_y])
                if toDraw:
                    cv2.circle(img, (landMark_x, landMark_y), 15, (255, 0, 255), cv2.FILLED)
        return self.lmList
    
    def noOfFingersUp(self):
        fingers = []
        #Thumb
        if self.lmList[4][1] < self.lmList[3][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        #4 Fingers
        for id in range(1, 5):
            if self.lmList[id*4][2] < self.lmList[id*4 - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        return fingers

def main():
    prevTime = 0
    curTime = 0
    cap = cv2.VideoCapture(0)
    detect = handDetectorObj()
    while True:
        success, img = cap.read()
        curTime = time.time()
        img = detect.detectHands(img)
        lmList = detect.findHandPosition(img)
        if len(lmList) != 0:
            print(lmList[4]) #print the fourth landmark of the hand which is the tip of the thumb
        fps = 1/(curTime-prevTime)    
        prevTime = curTime
        cv2.putText(img, f"FPS: {int(fps)}", (10,  70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (255, 0, 255), 3)
        cv2.imshow("Image", img) 
        cv2.waitKey(1)

if __name__ == "__main__":
    main()