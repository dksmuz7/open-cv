# Image pyramid
# It is used to increase or decrease the resolution of the
# image, this can be used in face, eye detection we use diff
# sized pyramid

import cv2 as cv 
import numpy as np

# Two types of pyramid - gaussian & laplacian
# 1. Gaussian Pyramid
img = cv.imread("/media/techio/Study Materials/Python Projects/arman.jpg",0)
img = cv.resize(img,(400,300))

# Pyramid down
pd1 = cv.pyrDown(img)
pd2 = cv.pyrDown(img)

# Pyramid up
pu1 = cv.pyrUp(img)
pu2 = cv.pyrUp(pd1)

# Displaying all the images
cv.imshow("Original image",img)
cv.imshow("pd1 ",pd1)
cv.imshow("pd2",pd2)
cv.imshow("PU1",pu1)
cv.imshow("PU2",pu2)


cv.waitKey(0)
cv.destroyAllWindows()