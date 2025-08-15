import cv2

cap = cv2.VideoCapture(0)  # try 1 or 2 if 0 fails

if not cap.isOpened():
    raise RuntimeError("Camera not found")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Camera Test - press q to quit", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
