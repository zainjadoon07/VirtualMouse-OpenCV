import cv2
import mediapipe as mp
import pyautogui
import time

# Setup
cap = cv2.VideoCapture(0)
hands = mp.solutions.hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
screen_w, screen_h = pyautogui.size()
clicking = False
last_scroll_time = time.time()

def is_finger_up(tip, pip):
    return tip.y < pip.y

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        hand = result.multi_hand_landmarks[0]
        landmarks = hand.landmark

        # Cursor movement using index finger
        index_tip = landmarks[8]
        index_x = int(index_tip.x * screen_w)
        index_y = int(index_tip.y * screen_h)
        pyautogui.moveTo(index_x, index_y)

        # Finger tips and pips
        tips = [landmarks[i] for i in [4, 8, 12, 16, 20]]
        pips = [landmarks[i] for i in [3, 6, 10, 14, 18]]

        fingers_up = [is_finger_up(tips[i], pips[i]) for i in range(5)]

        # CLICK: Victory sign (Index + Middle up)
        if fingers_up[1] and fingers_up[2] and not any(fingers_up[i] for i in [0, 3, 4]):
            if not clicking:
                clicking = True
                pyautogui.click()
                print("Click")
        else:
            clicking = False

        # SCROLL UP: Fist (all fingers down)
        if all(not up for up in fingers_up):
            if time.time() - last_scroll_time > 0.3:
                pyautogui.scroll(30)
                print("Scroll Up (Fist)")
                last_scroll_time = time.time()

        # SCROLL DOWN: Open Palm (all fingers up)
        if all(fingers_up):
            if time.time() - last_scroll_time > 0.3:
                pyautogui.scroll(-30)
                print("Scroll Down (Palm)")
                last_scroll_time = time.time()

    cv2.imshow("Virtual Mouse with Punch & Palm Scroll", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
