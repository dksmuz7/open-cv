# Object detection using camshift algorithm.
# it works by applying continuously adaptive meanshift algorithm

import numpy as np
import cv2 as cv

cap = cv.VideoCapture("/media/techio/Study Materials/Python Projects/test2.mp4")

# Taking first frame of the video
ret,frame = cap.read()

# Initial location
x,y,width,height = 1040,320,150,350
track = (x,y,width,height)

# ROI for tracking
roi = frame[y:y+height,x:x+width]
hsvRoi = cv.cvtColor(roi,cv.COLOR_BGR2HSV)

lb = np.array((0,73,65))
ub = np.array((255,156,177))
mask = cv.inRange(hsvRoi,lb,ub)
roiHist = cv.calcHist([hsvRoi],[0],mask,[180],[0,180])
cv.normalize(roiHist,roiHist,0,255,cv.NORM_MINMAX)

# Termination 
term = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT , 10,1)
cv.imshow("Roi",roi)



while True:
    ret,frame = cap.read()
    frame = cv.resize(frame,(500,320))
    if ret==True:
        hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        dst = cv.calcBackProject([hsv],[0],roiHist,[0,180],1)

        # Applying minshift
        ret,track = cv.CamShift(dst,track,term)

        # Drawing rectangle
        # x,y,w,h = track
        # final = cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)

        # better way of Drawing rect
        pts = cv.boxPoints(ret)
        pts = np.int64(pts)
        final = cv.polylines(frame,[pts],True,(0,255,0),2)

        cv.imshow("Original",frame)
        k=cv.waitKey(10) & 0xFF

        if k==27 :
            break
    else:
        break

cap.release()
cv.destroyAllWindows()