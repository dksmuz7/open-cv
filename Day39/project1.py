# Face and eye detection in image

# Face detection using haarcascade file
import cv2 as cv 
import numpy as np

# File location
path = "/media/techio/Study Materials/Python Projects/arman.jpg"
image = cv.imread(path)
gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

# Classifier file location
classifier = "Day39/haarcascade_frontalface_default.xml"
face = cv.CascadeClassifier(classifier)
eye = cv.CascadeClassifier("Day39/haarcascade_eye.xml")

faces = face.detectMultiScale(gray,4,4)

for(x,y,w,h) in faces:
    image = cv.rectangle(image,(x,y),(x+w,h+y),(127,0,255),2)
    
    # Now detect eye
    roi_gray = gray[y:y+h,x:x+w]
    roi_color = image[y:y+h,x:x+w]
    eyes = eye.detectMultiScale(roi_gray,2.8,3)
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,255),2)

image = cv.resize(image,(800,600))
cv.imshow("Face Detected",image)
cv.waitKey(0)
cv.destroyAllWindows()
