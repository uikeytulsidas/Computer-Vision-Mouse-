# 🖱️ Computer Vision Mouse

Control your mouse using **hand gestures** via webcam!  
This project uses **OpenCV**, **MediaPipe**, and **PyAutoGUI** to track your hand in real time and map finger movements to cursor control.

---

##  Features
- Move the mouse with your **index fingertip**.
- **Pinch (thumb + index)** to click.
- Smooth movement for more natural control.
- Works on **Windows, macOS, and Linux**.


---

## 🛠 Requirements

- Python **3.8 – 3.11**
- Webcam
- OS permissions for **Camera** and **Accessibility** (mouse control)

---

## 📦 Installation

1. **Clone this repository**
```bash
git clone https://github.com/yourusername/computer-vision-mouse.git
cd computer-vision-mouse
Create a virtual environment

Terminal:
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
Install dependencies

Terminal:
pip install --upgrade pip
pip install -r requirements.txt
requirements.txt

Terminal:
opencv-python
mediapipe==0.10.9
pyautogui
numpy
▶️ Usage

Run the program
Terminal:
python main.py