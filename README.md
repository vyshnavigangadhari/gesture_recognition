🖐️ Hand Gesture Recognition

This project uses OpenCV and MediaPipe to detect and recognize basic hand gestures in real time via webcam.

✨ Features

Detects and tracks hands using MediaPipe Hands

Recognizes gestures:

👍 Thumbs Up

👎 Thumbs Down

✋ Open Palm

✊ Fist

✌ Peace Sign

👉 Pointing

Real-time display with landmarks and gesture labels

🛠️ Installation

Clone this repository:

git clone https://github.com/vyshnavigangadhari/gesture_recognition.git
cd gesture_recognition


Create and activate a virtual environment (optional but recommended):

conda create -n gesture python=3.11 -y
conda activate gesture


Install dependencies:

pip install opencv-python opencv-contrib-python mediapipe numpy


If mediapipe fails with pip, use:

conda install -c conda-forge mediapipe

▶️ Usage

Run the script:

python gesture_recognition.py


Press ESC to exit the webcam window.

📷 Example Gestures

✋ Open Palm → “Open Palm”

👍 Thumbs Up → “Thumbs Up”

✊ Fist → “Fist”

📂 Project Structure
gesture_recognition/
│── gesture_recognition.py   # Main script
│── README.md                # Documentation
