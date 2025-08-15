import cv2, numpy as np, pyautogui, math
import mediapipe as mp

pyautogui.FAILSAFE = False
screen_w, screen_h = pyautogui.size()

mp_hands = mp.solutions.hands
mp_draw  = mp.solutions.drawing_utils

def lerp(a, b, t):
    return a + (b - a) * t

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("Camera not available")

smooth_x, smooth_y = 0, 0
click_cooldown = 0

with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    model_complexity=1,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
) as hands:
    while True:
        ok, frame = cap.read()
        if not ok: break
        frame = cv2.flip(frame, 1)  # mirror for natural control
        h, w, _ = frame.shape

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        res = hands.process(rgb)

        if res.multi_hand_landmarks:
            lm = res.multi_hand_landmarks[0].landmark
            # Index fingertip (8) & thumb tip (4)
            ix, iy = int(lm[8].x * w), int(lm[8].y * h)
            tx, ty = int(lm[4].x * w), int(lm[4].y * h)

            # Map camera coords to screen coords
            target_x = np.interp(ix, [0, w], [0, screen_w])
            target_y = np.interp(iy, [0, h], [0, screen_h])

            # Smooth movement
            smooth_x = lerp(smooth_x, target_x, 0.35)
            smooth_y = lerp(smooth_y, target_y, 0.35)

            pyautogui.moveTo(smooth_x, smooth_y, _pause=False)

            # Pinch to click
            dist = math.hypot(ix - tx, iy - ty)
            cv2.putText(frame, f"Pinch dist: {int(dist)}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            if click_cooldown > 0: click_cooldown -= 1
            if dist < 35 and click_cooldown == 0:
                pyautogui.click()
                click_cooldown = 12  # brief cooldown to avoid rapid fire

            mp_draw.draw_landmarks(frame, res.multi_hand_landmarks[0], mp_hands.HAND_CONNECTIONS)

        cv2.imshow("CV Mouse - press q to quit", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
