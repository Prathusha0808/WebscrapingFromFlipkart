import os
import sys
import numpy as np
import cv2
import mediapipe as mp
from tensorflow.keras.models import load_model

mpHands=mp.solutions.hands
hands=mpHands.Hands(max_num_hands=1, min_detection_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

model = load_model('trained_model_new')
gesture_classes=['five','one','two','thumb','closed palm']

s=0
if len(sys.argv)>1:
    s=sys.argv[1]

source=cv2.VideoCapture(s)
win_name="Camera Preview"
cv2.namedWindow(win_name,cv2.WINDOW_NORMAL)

while cv2.waitKey(5000)!=27:
    has_frame,frame=source.read()
    if not has_frame:
        break
    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(framergb)
    if result.multi_hand_landmarks:
        for handslms in result.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame, handslms, mpHands.HAND_CONNECTIONS)
            landmarks=[]
            for lm in handslms.landmark:
                landmarks.append(lm.x)
                landmarks.append(lm.y)
            prediction=model.predict([landmarks])
            print(prediction)
            index=np.argmax(prediction)
            gesture=gesture_classes[index]
            print(gesture)
            cv2.putText(frame, gesture, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)
            if index==0:
                os.system('start Chrome.exe')
            elif index==2:
                os.system('start wmplayer')
            elif index==4:
                os.system('shutdown /s')
            elif index==1:
                os.system('setvol +10')
            elif index==3:
                os.system('setvol -10')
    cv2.imshow(win_name,frame)
            
source.release()
cv2.destroyWindow(win_name)
