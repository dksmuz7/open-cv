import cv2 as cv
import numpy as np

img = cv.imread("/media/techio/Study Materials/Arduino/iot_gsm/schematic.jpg")
img = cv.resize(img,(300,520))
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
_, th1 = cv.threshold(img,130,255,cv.THRESH_BINARY)
cv.imshow("Normal thresholding",th1)

th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
cv.imshow("Adaptive thres 1",th2)

th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2);
cv.imshow("Gaussian thresholding",th3)

cv.waitKey(0)
cv.destroyAllWindows()