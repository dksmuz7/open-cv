# Object detection using webcam
# Hand detection using webcam
# Contour detectio using color space

import cv2 as cv
import numpy as np
from sqlalchemy import true

cap = cv.VideoCapture(0)

def empty(e):
    pass

# window name creation
cv.namedWindow("Color Adjustments",cv.WINDOW_NORMAL)
cv.resizeWindow("Color Adjustments",(300,300))
cv.createTrackbar("Thres","Color Adjustments",0,255,empty)

# Color detection trackbar
cv.createTrackbar("H_MIN","Color Adjustments",0,255,empty)
cv.createTrackbar("S_MIN","Color Adjustments",0,255,empty)
cv.createTrackbar("V_MIN","Color Adjustments",0,255,empty)
cv.createTrackbar("H_MAX","Color Adjustments",255,255,empty)
cv.createTrackbar("S_MAX","Color Adjustments",255,255,empty)
cv.createTrackbar("V_MAX","Color Adjustments",255,255,empty)

while True:
    _,frame = cap.read()
    frame = cv.resize(frame,(400,400))
    # cv.imshow("Frame",frame)
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    h_min = cv.getTrackbarPos("H_MIN","Color Adjustments")
    s_min = cv.getTrackbarPos("S_MIN","Color Adjustments")
    v_min = cv.getTrackbarPos("V_MIN","Color Adjustments")
    h_max = cv.getTrackbarPos("H_MAX","Color Adjustments")
    s_max = cv.getTrackbarPos("S_MAX","Color Adjustments")
    v_max = cv.getTrackbarPos("V_MAX","Color Adjustments")

    lb = np.array([h_min,s_min,v_min])
    ub = np.array([h_max,s_max,v_max])

    print(lb)
    print(ub)

    # Creating mask
    mask = cv.inRange(hsv,lb,ub)
    filter = cv.bitwise_and(frame,frame,mask=mask)

    mask1 = cv.bitwise_not(mask)
    m_g = cv.getTrackbarPos("Thres","Color Adjustments")
    ret,thres = cv.threshold(mask1,m_g,255,cv.THRESH_BINARY)
    dilatation = cv.dilate(thres,(1,1),iterations = 6)

    # Finding contours
    cnts,h = cv.findContours(thres,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    frame = cv.drawContours(frame,cnts,-1,(176,10,15),4)

    for cnt in cnts:
        epsilon = 0.0001*cv.arcLength(cnt,True)
        data = cv.approxPolyDP(cnt,epsilon,True)

        hull = cv.convexHull(data)
        cv.drawContours(frame,[cnt],-1,(50,50,150),2)
        cv.drawContours(frame,[hull],-1,(0,255,0),2)



    cv.imshow("Thres",thres)
    cv.imshow("Mask",mask)
    cv.imshow("Filter",filter)
    cv.imshow("Result",frame)
     

    if cv.waitKey(1) & 0xFF==27:
        break

cv.destroyAllWindows()