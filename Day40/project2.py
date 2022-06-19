# Face and Eye detection using webcam

import cv2 as cv 
import numpy as np

face = cv.CascadeClassifier("Day40/haarcascade_frontalface_default.xml")
eye = cv.CascadeClassifier("Day40/haarcascade_eye.xml")

def detector(img):
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(127,0,125),3)

        roi_gray = gray[y:y+h,x:x+w]
        roi_color = img[y:y+h,x:x+w]

        eyes = eye.detectMultiScale(roi_color,1.2,3)
        for (ex,ey,ew,eh) in eyes:
            cv.circle(roi_color,(ex+27,ey+27),20,(255,255,0),2)

    return img


cap = cv.VideoCapture("/media/techio/Study Materials/Python Projects/test2.mp4")

while True:
    ret, frame = cap.read()
    fram = cv.flip(frame,2)
    cv.imshow("face detect",detector(frame))
    if cv.waitKey(10)==13: #Enter key to terminate
        break

cap.release()
cv.destroyAllWindows()