# 🖐️ Hand Gesture Recognition  

This project uses **OpenCV** and **MediaPipe** to detect and recognize basic hand gestures in real time via webcam.  

---

## ✨ Features
- Detects and tracks hands using **MediaPipe Hands**  
- Recognizes gestures:
  - 👍 Thumbs Up  
  - 👎 Thumbs Down  
  - ✋ Open Palm  
  - ✊ Fist  
  - ✌ Peace Sign  
  - 👉 Pointing  
- Real-time display with landmarks and gesture labels  

---

## 🛠️ Installation  

1. Clone this repository:  
   ```bash
   git clone https://github.com/vyshnavigangadhari/gesture_recognition.git
   cd gesture_recognition

   
2.Create and activate a virtual environment (optional but recommended):
conda create -n gesture python=3.11 -y
conda activate gesture


3.Install dependencies:
pip install -r requirements.txt
###If mediapipe fails with pip, use:
conda install -c conda-forge mediapipe

##Usage
python gesture_recognition.py
