# Optical flow detection using Gunner Farenback's algo

import cv2 as cv
import numpy as np

cap = cv.VideoCapture("/media/techio/Study Materials/Python Projects/test2.mp4")

ret,frame = cap.read()
prvs = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame)
hsv[...,1] = 255

while(1):
    ret,frame2 = cap.read()
    next = cv.cvtColor(frame2,cv.COLOR_BGR2GRAY)

    # CalcOptical Flow
    flow = cv.calcOpticalFlowFarneback(prvs,next,None,0.5,3,15,3,5,1.2,0)
    mag,ang = cv.cartToPolar(flow[...,0],flow[...,1])
    hsv[...,0] = ang*180/np.pi/2
    hsv[...,2] = cv.normalize(mag,None,0,255,cv.NORM_MINMAX)
    rgb = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
    img1 = cv.add(frame2,rgb)
    img2 = cv.resize(img1,(700,400))

    cv.imshow("Frame 2 ",img1)
    k = cv.waitKey(10) & 0xFF
    if k==27:
        break
    elif k == ord('s'):
        cv.imwrite("OpticalFb.png",frame2)
        cv.imwrite("OKticalhsv.png",rgb)

cap.release()
cv.destroyAllWindows()

