import mediapipe as mp
import cv2
import sys

s=0
if len(sys.argv)>1:
    s=sys.argv[1]

source=cv2.VideoCapture(s)
win_name="Camera Preview"
cv2.namedWindow(win_name,cv2.WINDOW_NORMAL)
m-pHands=mp.solutions.hands
hands=mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

while cv2.waitKey(1)!=27:
    has_frame,frame=source.read()
    if not has_frame:
        break
    x , y, c = frame.shape
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(framergb)
    if result.multi_hand_landmarks:
        for handslms in result.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)
    cv2.imshow(win_name,frame)

source.release()
cv2.destroyWindow(win_name)
