import cv2
import numpy as np
import csv
import time

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    for x in range (330,340,1):
        for y in range(220,260,1):
            color = img[x,y]
            colorB = img[x,y,0]
            colorG = img[x,y,1]
            colorR = img[x,y,2]
        print('B G R = ',color)
        cv2.imshow('Pengambilan Database', img)

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

cap.release()
cv2.destoryAllWindows()
