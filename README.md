
# 🖐️ Gesture-Based Scroll Control using MediaPipe & OpenCV

This project enables gesture-based control for scrolling and clicking using your webcam. It uses **MediaPipe** to detect hand landmarks and **OpenCV** to process the video stream and map gestures to actions like:

- **Scroll Up** 🖐️ ➡️ Fist (Punch)
- **Scroll Down** ✋ ➡️ Open Palm
- **Click** 👉 ➡️ Index Finger Pinch (Tip close to thumb)

---

## 📦 Features

- Real-time hand tracking with MediaPipe
- Gesture classification (Palm, Fist, Pinch)
- Scroll up/down using mouse wheel
- Simulated left-click using gesture
- Runs on CPU with minimal latency

---

## 🧰 Technologies Used

- Python 3.x
- MediaPipe
- OpenCV
- pyautogui
- numpy

---

## 🚀 Getting Started

### ✅ Prerequisites

Install the required Python libraries:

```bash
pip install mediapipe opencv-python pyautogui numpy
```

### ▶️ Run the App

```bash
python gesture_scroll_control.py
```

**Note**: Make sure your webcam is connected and visible to the app.

---

## ✋ Gestures

| Gesture          | Action       | Description                              |
|------------------|--------------|------------------------------------------|
| Open Palm        | Scroll Down  | All fingers extended                    |
| Fist (Punch)     | Scroll Up    | All fingers curled or closed            |
| Pinch (Index)    | Click        | Index finger tip close to thumb tip     |

---

## 📂 Project Structure

```plaintext
gesture-scroll/
├── gesture_scroll_control.py     # Main Python script
├── README.md                     # Project documentation
```

---

## 🎯 Future Improvements

- Improve gesture stability with smoothing
- Add visual feedback overlay
- Support for right-click and drag
- Combine hand + face + pose gestures using MediaPipe Holistic

---

## 📜 License

MIT License

---

## 🙌 Author

Zain Jadoon
```
