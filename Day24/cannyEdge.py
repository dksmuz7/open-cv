# Canny edge detection technique
# It can resuce noise
# It can perform gradient
# Non maximum suppression
# Double threshold
# Edge tracking hysteresis

import cv2 as cv
import numpy as np

# Load image into gray scale
img = cv.imread("/media/techio/Study Materials/Python Projects/balls.jpg")
img = cv.resize(img,(400,300));
img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Thresholding using trackbars
def empty():
    pass

cv.namedWindow("Threshold")
cv.createTrackbar("Thres1","Threshold",0,255,empty)
cv.createTrackbar("Thres2","Threshold",0,255,empty)

cv.imshow("Original image",img)
cv.imshow("Gray Image",img_gray)

while True:
    th1 = cv.getTrackbarPos("Thres1","Threshold")
    th2 = cv.getTrackbarPos("Thres2","Threshold")
    print(th1,th2)
    # Canny Image
    canny_img = cv.Canny(img_gray,th1,th2)

    cv.imshow("Threshold",canny_img)

    if cv.waitKey(1) & 0xFF == 27:
        break
    
cv.destroyAllWindows()