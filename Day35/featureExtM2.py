# Method 2 for corner detection
# Shi Tomasi corner detection technique
# It is more effective compared to Harris
# Corner method
# In this we can limit the no of corners and its quality

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("/media/techio/Study Materials/Python Projects/shapes.png")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Syntax (img,maxCorner,quality,maxDistance)
corners = cv.goodFeaturesToTrack(gray,50,0.01,20)
corners = np.int64(corners)

for corner in corners:
    x,y = corner.ravel()
    cv.circle(img,(x,y),3,255,-1)

cv.imshow("Result",img)

cv.waitKey(0)
cv.destroyAllWindows()
