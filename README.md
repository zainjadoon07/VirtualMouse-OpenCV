🖐️ Gesture-Based Scroll Control
A Python application that enables touchless scrolling and clicking using hand gestures captured via a webcam, powered by MediaPipe and OpenCV.
📖 Overview
This project allows users to control scrolling and clicking actions using hand gestures detected through a webcam. It leverages MediaPipe for real-time hand landmark detection and OpenCV for video stream processing, mapping gestures to intuitive actions:

Scroll Up 🖐️ ➡️ Fist (Punch)
Scroll Down ✋ ➡️ Open Palm
Click 👉 ➡️ Index Finger Pinch (Tip close to thumb)


✨ Features

Real-time Hand Tracking: Powered by MediaPipe for accurate gesture detection.
Gesture Classification: Recognizes Open Palm, Fist, and Pinch gestures.
Mouse Control: Scroll up/down using mouse wheel and simulate left-clicks.
Low Latency: Runs efficiently on CPU with minimal delay.
Cross-Platform: Compatible with Python 3.x environments.


🛠️ Technologies Used

Python 3.x
MediaPipe
OpenCV
pyautogui
numpy


🚀 Getting Started
✅ Prerequisites
Ensure you have Python 3.x installed, then install the required libraries:
pip install mediapipe opencv-python pyautogui numpy

▶️ Running the Application

Clone the repository:git clone https://github.com/yourusername/gesture-scroll.git
cd gesture-scroll


Run the main script:python gesture_scroll_control.py


Note: Ensure your webcam is connected and accessible to the application.


✋ Supported Gestures



Gesture
Action
Description



Open Palm
Scroll Down
All fingers extended


Fist (Punch)
Scroll Up
All fingers curled or closed


Pinch (Index)
Click
Index finger tip close to thumb tip



📂 Project Structure
gesture-scroll/
├── gesture_scroll_control.py     # Main Python script for gesture control
├── README.md                     # Project documentation


🎯 Future Improvements

Enhance gesture stability with smoothing algorithms.
Implement a visual feedback overlay for detected gestures.
Add support for right-click and drag functionalities.
Integrate MediaPipe Holistic for combined hand, face, and pose gestures.


🙌 Author
Zain Jadoon
