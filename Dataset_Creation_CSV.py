import os
from os import listdir
import cv2
import mediapipe as mp
import csv

mp_hands=mp.solutions.hands
hands=mp_hands.Hands(max_num_hands=1,min_detection_confidence=0.5)
file=open('gesture_dataset_other.csv', 'w', newline='')
writer=csv.writer(file)

def load_images_from_folder(folder,label):
    for imagename in os.listdir(folder):
        #print(imagename)
        image = cv2.imread(os.path.join(folder,imagename))
        result = hands.process(image)
        if result.multi_hand_landmarks:
            for handslms in result.multi_hand_landmarks:
                landmarks=[]
                for lm in handslms.landmark:
                    landmarks.append(lm.x)
                    landmarks.append(lm.y)
                landmarks.append(label)
                writer.writerow(landmarks)
    
gestures=["D:/majorproject1/Dataset/Gesture0/","D:/majorproject1/Dataset/Gesture1/","D:/majorproject1/Dataset/Gesture2/","D:/majorproject1/Dataset/Gesture3/","D:/majorproject1/Dataset/Gesture4/"]
g_c=0
for ges_class in gestures:
    load_images_from_folder(ges_class,g_c)
    g_c=g_c+1

file.close()
