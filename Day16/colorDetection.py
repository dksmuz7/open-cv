# Color detection in live video 
import cv2 as cv
from cv2 import waitKey
import numpy as np

cap = cv.VideoCapture(0) # Accessing camera

def empty():
    pass

cv.namedWindow("Color Adjustments")
cv.createTrackbar("Min Hue","Color Adjustments",0,255,empty)
cv.createTrackbar("Max Hue","Color Adjustments",255,255,empty)
cv.createTrackbar("Min Sat","Color Adjustments",0,255,empty)
cv.createTrackbar("Max Sat","Color Adjustments",255,255,empty)
cv.createTrackbar("Min Val","Color Adjustments",0,255,empty)
cv.createTrackbar("Max Val","Color Adjustments",255,255,empty)

while True:
    ret,frame = cap.read()
    frame = cv.resize(frame,(16*34,9*34))
    frame = cv.flip(frame,1)
    hsvFrame = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    minHue = cv.getTrackbarPos("Min Hue","Color Adjustments")
    maxHue = cv.getTrackbarPos("Max Hue","Color Adjustments")
    minSat = cv.getTrackbarPos("Min Sat","Color Adjustments")
    maxSat = cv.getTrackbarPos("Max Sat","Color Adjustments")
    minVal = cv.getTrackbarPos("Min Val","Color Adjustments")
    maxVal = cv.getTrackbarPos("Max Val","Color Adjustments")

    lowerBound = np.array([minHue,minSat,minVal])
    upperBound = np.array([maxHue,maxSat,maxVal])

    # Creating mask
    mask = cv.inRange(hsvFrame,lowerBound,upperBound)

    # Filter mask with image
    filteredFrame = cv.bitwise_and(frame,frame,mask=mask)

    cv.imshow("Original Frame",frame)
    cv.imshow("Masked Frame",mask)
    cv.imshow("Filtered Frame",filteredFrame)

    if waitKey(25) & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()