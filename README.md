# ✨ MotionInk - Hand Tracking Paint App
A **gesture-based drawing application** that lets you paint in the air using **hand tracking** powered by **OpenCV & MediaPipe**. MotionInk provides a **seamless and interactive drawing experience** without needing a physical touch interface.

📌 **GitHub Repo**: [MotionInk](https://github.com/kira14102005/AirPaint)

---

## 🚀 Features

✅ **Draw with hand gestures**  
✅ **Select colors using two-finger selection mode**  
✅ **Erase using an eraser gesture**  
✅ **Smooth brush strokes with dynamic thickness**  
✅ **Real-time hand tracking with OpenCV & MediaPipe**  
✅ **Standalone `.exe` file for easy use**  

---

## 🖥️ Installation & Setup

### **1️⃣ Download the `.exe` File (Windows)**
No need to install Python or dependencies! Simply download the **MotionInk `.exe` file** from the **GitHub Releases** or from the `dist/` folder if you built it yourself.

### **2️⃣ Run MotionInk**
- Double-click `tkinterApp.exe` to launch the application.
- If Windows warns about an unknown publisher, click **"More Info" → "Run Anyway"**.

---

## 🖌️ How to Use MotionInk

1️⃣ **Start the application**  
   - Click the **"Start"** button to launch the webcam.  

2️⃣ **Select a mode:**  
   - **Raise One Finger** → **Start Drawing**  
   - **Raise Two Fingers** → **Selection Mode**  

3️⃣ **Change Colors:**  
   - Move your hand over the **color bar at the top** while in **selection mode**.  

4️⃣ **Erase:**  
   - Select **Black** color to erase.  

5️⃣ **Exit MotionInk:**  
   - Click the **"Exit"** button or press **`q`** to close the app.  

---

## 🔧 Building the `.exe` File Yourself (Optional)

If you want to modify or rebuild MotionInk, follow these steps:

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/kira14102005/AirPaint.git
cd AirPaint
```

### **2️⃣ Install Dependencies**
Ensure **Python 3.8+** is installed, then run:
```bash
pip install opencv-python mediapipe numpy pillow
```

### **3️⃣ Create the `.exe` File**
Use **PyInstaller** to package the app:
```bash
pyinstaller --onefile --windowed tkinterApp.py
```
The final **tkinterApp.exe** will be inside the `dist/` folder.

---

## ❌ Troubleshooting

**🛑 `.exe` Not Opening?**  
- Run it from Command Prompt:  
  ```bash
  cd path\to\MotionInk\dist
  tkinterApp.exe
  ```
- Ensure your **webcam is connected** and accessible.

**🛑 Hand Not Detected?**  
- Make sure you have **good lighting**.  
- Avoid **background distractions**.

**🛑 Colors Not Changing?**  
- Ensure your **hand is in selection mode (two fingers up)**.

---

## 📜 License
MotionInk is **open-source** and free to use.

---

## 📬 Contact & Contributions
- **GitHub Issues**: Report bugs & request features [here](https://github.com/kira14102005/AirPaint/issues).
- Created by **Harshit Rai**.
