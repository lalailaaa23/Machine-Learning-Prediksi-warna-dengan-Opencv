import cv2
import numpy as np
cap = cv2.VideoCapture (0)
while True:
    ret, frame = cap.read()
    frame = cv2.flip (frame,1 )
    cv2.imshow ("camera", frame)
    key = cv2.waitKey (1)
    if key == 27:
        break
cap.release ()
cv2.destoryAllWindows ()
