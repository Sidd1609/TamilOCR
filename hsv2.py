import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
cv2.namedWindow('HSV Image')
cv2.createTrackbar('LH', 'HSV Image', 0, 255, nothing)      ##Create Trackbar
cv2.createTrackbar('LS', 'HSV Image', 0, 255, nothing)
cv2.createTrackbar('LV', 'HSV Image', 0, 255, nothing)
cv2.createTrackbar('UH', 'HSV Image', 255, 255, nothing)
cv2.createTrackbar('US', 'HSV Image', 255, 255, nothing)
cv2.createTrackbar('UV', 'HSV Image', 255, 255, nothing)

while(1):
    ret, frame = cap.read()         ##Read image frame
    if not ret:
        break
    frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)     ##BGR to HSV Conversion
    if cv2.waitKey(1) == ord('s'):
        break
    lh = cv2.getTrackbarPos('LH', 'HSV Image')          ##get the value of trackbar
    ls = cv2.getTrackbarPos('LS', 'HSV Image')
    lv = cv2.getTrackbarPos('LV', 'HSV Image')
    uh = cv2.getTrackbarPos('UH', 'HSV Image')
    us = cv2.getTrackbarPos('US', 'HSV Image')
    uv = cv2.getTrackbarPos('UV', 'HSV Image')

    lb = np.array([lh, ls, lv])                     ##Lower bound HSV values
    #print(lb)
    ub = np.array([uh, us, uv])                     ##Upper bound HSV values
    #print(ub)

    mask = cv2.inRange(frame2, lb, ub)              ##Create mask
    res = cv2.bitwise_and(frame, frame, mask = mask)        ##Apply mask on original image

    cv2.imshow('Original Image', frame)
    cv2.imshow('Masked Image', mask)
    cv2.imshow('Resuting Image', res)

cap.release()               ##Release memory
cv2.destroyAllWindows()     ##Close all windows
