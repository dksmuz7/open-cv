# Circle detection using hough circle methode

import cv2 as cv 
import numpy as np

img = cv.imread("/media/techio/Study Materials/Python Projects/balls.jpg")
img2 = img.copy()
img2 = cv.resize(img2,(500,300))
gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray,5)

# HoughCircles method (img,circle_method,dp,minDist,param1,param2(p1<p2),min_radi,max_radi)
circles = cv.HoughCircles(gray,cv.HOUGH_GRADIENT,1,60,param1=50,param2=30,minRadius=0,maxRadius=160)

# Converting data received from HoughCircles 
data = np.uint16(np.around(circles)) # Converting circles data in int form
print(data)

for (x,y,r) in data[0, :]:
    # Drawing circle of of detected circle
    cv.circle(img2,(x,y),r,(50,10,50),2)
    # Drawing center of the detected circle
    cv.circle(img2,(x,y),2,(255,255,100),-1)

cv.imshow("Result",img2)
cv.imshow("gray",gray)

cv.waitKey(0)
cv.destroyAllWindows()

