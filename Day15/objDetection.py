# Object detection based on color
from multiprocessing.connection import wait
import cv2 as cv
from cv2 import ROTATE_90_CLOCKWISE
from cv2 import waitKey
import numpy as np

path = "/media/deepaksagar/Study Materials/Python Projects/coloured_balls.jpg"

img = cv.imread(path)
img = cv.rotate(img,ROTATE_90_CLOCKWISE)

hsvImg = cv.cvtColor(img,cv.COLOR_BGR2HSV)
upper = np.array([130,235,255])
lower = np.array([110,47,47])

mask = cv.inRange(hsvImg,lower,upper);
res = cv.bitwise_and(img,img,mask=mask)

cv.imshow("Original Image",img)
cv.imshow("Masked Image",mask)
cv.imshow("Colored detected image",res)

if waitKey(0) & 0xFF == 27:
    exit

cv.destroyAllWindows()