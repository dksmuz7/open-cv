# Image contour finding and drawing

import cv2 as cv
import numpy as np

img = cv.imread("/media/techio/Study Materials/Python Projects/logo.png")
img = cv.resize(img,(300,400))
img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Finding threshold
ret,thres = cv.threshold(img_gray,20,255,0)

# find contour
cnts,h = cv.findContours(thres,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

# draw contours
img = cv.drawContours(img,cnts,-1,(176,0,0),4)

# Output
cv.imshow("Original image",img)
cv.imshow('Gray',img_gray)
cv.imshow("Thresh",thres)


cv.waitKey(0)
cv.destroyAllWindows()