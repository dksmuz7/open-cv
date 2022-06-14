# Feature detection and Description
# Feature - edge,wdth,height,corner

# Corner Detection
# this method works as jigsaw puzzle

import cv2 as cv 
import numpy as np

img = cv.imread("/media/techio/Study Materials/Python Projects/shapes.png")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray = np.float32(gray) # Harris function taked 32bit image

# Methode 1 
# Harris corner detection
# Input Image, blocksize,ksize,k
res = cv.cornerHarris(gray,2,3,0.04)
print(res)

res = cv.dilate(res,None)

img[res>0.01*res.max()] = [0,0,0] #marked Color

cv.imshow("Image",img)

cv.waitKey(0)
cv.destroyAllWindows()