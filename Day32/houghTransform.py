# Hough transform is used for detecting shapes,
# if we can represent the shape in mathematical form
# It can detect shape even if it is broken or distorted

import cv2 as cv
import numpy as np

img = cv.imread("/media/techio/Study Materials/Python Projects/chess.jpg")
img = cv.resize(img,(400,400))
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray,20,250)

# Detecting lines using Hough transform
lines = cv.HoughLines(edges,1,np.pi/180,100)

print(lines)

for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv.line(img,(x1,y1),(x2,y2),(255,0,255),2)

cv.imshow("Edges",edges)
cv.imshow("lines",img)

cv.waitKey(0)
cv.destroyAllWindows()