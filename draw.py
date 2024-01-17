import cv2
import numpy as np
import matplotlib.pyplot as plt
import keyboard
Kernal = np.ones((5, 5), np.uint8)
cap=cv2.VideoCapture(0)
y1=[]
x1=[]
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
im = np.zeros((h,w, 3), dtype = "uint8")+255
f=0
while(1):
    ret,frame=cap.read()
    frame = cv2.flip(frame, +1)
    frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lb = np.array([27, 100, 120])               
    ub = np.array([62, 255, 255])
    mask = cv2.inRange(frame2, lb, ub)
    mas = cv2.morphologyEx(mask, cv2.MORPH_OPEN, Kernal)
    #cv2.imshow('mask',mas)
    res = cv2.bitwise_and(frame, frame, mask = mas)
    #cv2.imshow('res',res)
    if not (keyboard.is_pressed('ctrl')):
        contours, hierarchy = cv2.findContours(mas, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) != 0:
            cnt = contours[0]
            (x, y), radius = cv2.minEnclosingCircle(cnt)
            x = int(x)
            y = int(y)
            x1.append(x)
            y1.append(y)
    for i in range(len(x1)):
        cv2.circle(frame, (x1[i], y1[i]), 0, (0, 0, 255), 6)
        cv2.circle(im, (x1[i], y1[i]), 0, (0,0, 0), 6)        
    cv2.imshow('frame',frame)
    cv2.imshow('im', im)
    if cv2.waitKey(1)  == ord('q'):
        break
    cv2.imwrite('a2.jpg',im)
cv2.destroyAllWindows()
cap.release()
    
