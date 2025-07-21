🖐️ Gesture-Based Scroll Control
A Python-powered application for touchless scrolling and clicking using hand gestures captured via webcam, leveraging MediaPipe for hand tracking and OpenCV for video processing.
📖 Overview
Transform your webcam into a gesture-based controller! This project uses MediaPipe for real-time hand landmark detection and OpenCV to process video streams, mapping intuitive gestures to actions:

Scroll Up 🖐️ ➡️ Fist (Punch)
Scroll Down ✋ ➡️ Open Palm
Click 👉 ➡️ Index Finger Pinch (Tip close to thumb)


✨ Features

Real-Time Hand Tracking: Accurate detection using MediaPipe.
Gesture Recognition: Classifies Open Palm, Fist, and Pinch gestures.
Mouse Control: Seamlessly scroll up/down with mouse wheel emulation.
Simulated Clicks: Perform left-clicks via gestures.
Low Latency: Optimized for CPU-based processing with minimal delay.


🛠️ Technologies Used

Python 3.x 🐍
MediaPipe 🤲
OpenCV 📸
pyautogui 🖱️
numpy 🔢


🚀 Getting Started
✅ Prerequisites
Ensure you have Python 3.x installed, then install the required libraries:
pip install mediapipe opencv-python pyautogui numpy

▶️ Running the Application

Clone the repository:
git clone https://github.com/yourusername/gesture-scroll.git
cd gesture-scroll


Run the main script:
python gesture_scroll_control.py


Note: Ensure your webcam is connected and accessible.



✋ Supported Gestures



Gesture
Action
Description



Open Palm ✋
Scroll Down ⬇️
All fingers extended


Fist (Punch) 🖐️
Scroll Up ⬆️
All fingers curled or closed


Pinch (Index) 👉
Click 🖱️
Index finger tip close to thumb tip



📂 Project Structure
gesture-scroll/
├── gesture_scroll_control.py     # **Main Python script** for gesture control
├── README.md                     # **Project documentation**


🎯 Future Improvements

Enhance Stability: Implement smoothing algorithms for gesture detection.
Visual Feedback: Add an overlay to display detected gestures.
Extended Controls: Support right-click and drag functionalities.
Holistic Gestures: Integrate MediaPipe Holistic for hand, face, and pose combinations.


📜 License
This project is licensed under the MIT License 📄.

🙌 Author
Zain Jadoon 👨‍💻
