# Hough line probability method

import cv2 as cv
import numpy as np

img = cv.imread("/media/techio/Study Materials/Python Projects/chess.jpg")
img = cv.resize(img,(400,400))
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray,30,100)

# Line detection using hough line p methode (P- probability)
lines = cv.HoughLinesP(edges,1,np.pi/180,100,minLineLength=8,maxLineGap=100)

for line in lines:
    x1,y1,x2,y2 = line[0]
    cv.line(img,(x1,y1),(x2,y2),(255,0,255),2)


cv.imshow("Edges",edges)
cv.imshow("lines",img)

cv.waitKey(0)
cv.destroyAllWindows()