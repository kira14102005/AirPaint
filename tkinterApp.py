import cv2
import mediapipe as mp
import time
import HandTrackingModule as hm
import os
import numpy as np
import math
import threading
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk

######### PARAMETERS #########
brushWeight = 15
prev_x, prev_y = 0, 0
eraseThickness = 50
running = False  # Control flag for OpenCV loop

######### LOAD HEADER IMAGES #########
directory = "CanvaImage/Header"
myList = os.listdir(directory)
headerImages = [cv2.imread(f'{directory}/{imgPath}') for imgPath in myList]
currHeader = headerImages[0]
drawColor = (0, 0, 255)  # Default Red Color

######### SETUP IRIUN WEBCAM #########
cap = cv2.VideoCapture(0)  # Iriun Webcam as default camera
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # Force resolution to 1280x720
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

######### CREATE TKINTER WINDOW #########
root = tk.Tk()
root.title("Hand Tracking Paint App")
root.geometry("1300x800")

# Label to display OpenCV feed
label = Label(root)
label.pack()

def start_opencv():
    global running, prev_x, prev_y, imgCanvas
    if running:
        return  # Prevent multiple instances
    running = True
    imgCanvas = np.zeros((720, 1280, 3), np.uint8)  # Reset canvas

    def opencv_loop():
        global running, prev_x, prev_y, currHeader, drawColor, imgCanvas
        while running:
            success, img = cap.read()
            if not success:
                print("Failed to capture video. Ensure Iriun Webcam is running.")
                continue

            img = cv2.flip(img, 1)  # Flip image for mirror effect
            detector = hm.handDetectorObj()
            img = detector.detectHands(img)
            lmrkArray = detector.findHandPosition(img, toDraw=False)

            if len(lmrkArray) != 0:
                # Tip of index & middle finger
                x1, y1 = lmrkArray[8][1], lmrkArray[8][2]
                x2, y2 = lmrkArray[12][1], lmrkArray[12][2]
                fingers = detector.noOfFingersUp()

                if fingers[1] and fingers[2]:  # Selection Mode
                    prev_x, prev_y = 0, 0
                    cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)
                    if y1 < 125:
                        if 200 < x1 < 280:
                            currHeader = headerImages[0]
                            drawColor = (0, 0, 255)  # Red
                        elif 435 < x1 < 510:
                            currHeader = headerImages[1]
                            drawColor = (0, 255, 0)  # Green
                        elif 635 < x1 < 715:
                            currHeader = headerImages[2]
                            drawColor = (0, 255, 255)  # Yellow
                        elif 850 < x1 < 975:
                            currHeader = headerImages[3]
                            drawColor = (255, 0, 0)  # Blue
                        elif 1050 < x1 < 1160:
                            currHeader = headerImages[4]
                            drawColor = (0, 0, 0)  # Black (Eraser)

                if fingers[1] and not fingers[2]:  # Drawing Mode
                    cv2.circle(img, (x1, y1), 15, drawColor, cv2.FILLED)
                    if prev_x == 0 and prev_y == 0:
                        prev_x, prev_y = x1, y1
                    thickness = eraseThickness if drawColor == (0, 0, 0) else brushWeight
                    cv2.line(img, (prev_x, prev_y), (x1, y1), drawColor, thickness)
                    cv2.line(imgCanvas, (prev_x, prev_y), (x1, y1), drawColor, thickness)
                    prev_x, prev_y = x1, y1

            # Overlay canvas on image
            gray_img = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
            _, imgInv = cv2.threshold(gray_img, 50, 255, cv2.THRESH_BINARY_INV)
            imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
            img = cv2.bitwise_and(img, imgInv)
            img = cv2.bitwise_or(img, imgCanvas)

            # Set header
            img[0:125, 0:1280] = currHeader

            # Convert frame for Tkinter display
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imgPIL = Image.fromarray(imgRGB)
            imgtk = ImageTk.PhotoImage(image=imgPIL)
            label.imgtk = imgtk
            label.configure(image=imgtk)

            # Update the GUI
            root.update_idletasks()
            root.update()

    threading.Thread(target=opencv_loop, daemon=True).start()

def stop_opencv():
    global running
    running = False
    cap.release()
    root.quit()  # Close Tkinter window

# Buttons to Start/Exit
start_button = tk.Button(root, text="Start", command=start_opencv, font=("Arial", 14), bg="green", fg="white")
start_button.pack()

exit_button = tk.Button(root, text="Exit", command=stop_opencv, font=("Arial", 14), bg="red", fg="white")
exit_button.pack()

# Run the Tkinter GUI
root.mainloop()
