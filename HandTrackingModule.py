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
        self.hands = self.handObj.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
        self.drawObj  = mp.solutions.drawing_utils
        self.handObj = mp.solutions.hands
        self.hands = self.handObj.Hands()
        self.drawObj  = mp.solutions.drawing_utils



# while True:
#     success, img = cap.read()
#     imRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     result = hands.process(imRGB)
#     # print(result.multi_hand_landmarks)  #To check if the hand is detected or not
#     if result.multi_hand_landmarks:
#         for hand in result.multi_hand_landmarks: #For each hand detected
#             for id, lm in enumerate(hand.landmark):
#             #    print(id, lm)
#                 h, w, c = img.shape
#                 landMark_x, landMark_y = int(lm.x*w), int(lm.y*h)
#                 print(id, landMark_x, landMark_y)
#                 if id == 0: #To draw a circle on the tip of the bottom of the hand palm
#                     cv2.circle(img, (landMark_x, landMark_y), 15, (255, 0, 255), cv2.FILLED)
                
#             drawObj.draw_landmarks(img, hand, handObj.HAND_CONNECTIONS)
#     curTime = time.time()
#     fps = 1/(curTime-prevTime)
#     prevTime = curTime
#     cv2.putText(img, f"FPS: {int(fps)}", (10,  70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (255, 0, 255), 3)
#     cv2.imshow("Image", img) 
#     cv2.waitKey(1)
def main():
    prevTime = 0
    curTime = 0
    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        curTime = time.time()
        fps = 1/(curTime-prevTime)
        prevTime = curTime
        cv2.putText(img, f"FPS: {int(fps)}", (10,  70), cv2.FONT_HERSHEY_COMPLEX_SMALL, 3, (255, 0, 255), 3)
        cv2.imshow("Image", img) 
        cv2.waitKey(1)

if __name__ == "__main__":
    main()