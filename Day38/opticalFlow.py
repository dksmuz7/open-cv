# Optical Flow using lucas Kanade methode
# Pattern matching algorithm

# Pixel intensities of an object don;t change b/w consecutive
# from the neighbouring pixels have similar motion

from math import floor
import cv2 as cv
import numpy as np

cap = cv.VideoCapture("/media/techio/Study Materials/Python Projects/test2.mp4")

# parameters for shitomasi corner detection
featureParam = dict(maxCorners = 100,qualityLevel = 0.3,minDistance = 7,blockSize=7)

# Parameters for Lucas Kanade optical flow
lkParam = dict(winSize = (15,15),maxLevel = 2, criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT,10,0.03))

# Creating some random color
color = np.random.randint(0,255,(100,3))

# Take first frame and find corners in it
ret,oldFrame = cap.read()
oldGray = cv.cvtColor(oldFrame,cv.COLOR_BGR2GRAY)
p0 = cv.goodFeaturesToTrack(oldGray,mask=None,**featureParam)

# Creating mask image for drwaing purposes
mask = np.zeros_like(oldFrame)

while(1):
    ret,frame = cap.read()

    # frame = cv.resize(frame,(600,500))
    frameGray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)

    # Calculating optical flow
    p1,st,err = cv.calcOpticalFlowPyrLK(oldGray,frameGray,p0,None,**lkParam)

    # Selecting good points
    goodNew = p1[st==1]
    goodOld = p0[st==1]

    for i, (new,old) in enumerate(zip(goodNew,goodOld)):
        a,b = new.ravel()
        c,d = old.ravel()

        a=floor(a)
        b=floor(b)
        c=floor(c)
        d=floor(d)

        # print("a,b =",floor(a),b,"c,d =",c,d)
        mask = cv.line(mask,(a,b),(c,d),color[i].tolist(),2)
        frame = cv.circle(frame,(a,b),5,color[i].tolist(),-1)

    img = cv.add(frame,mask)
    img = cv.resize(img,(700,600))
    cv.imshow('frame',img)
    cv.imshow("Frame",frame)

    k = cv.waitKey(30) & 0xFF
    if k==27:
        break

    oldGray = frameGray.copy()
    p0 = goodNew.reshape(-1,1,2)

cv.destroyAllWindows
cap.relase()