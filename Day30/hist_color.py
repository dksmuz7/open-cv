# Finding histogram of colored image

from cv2 import imshow
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# Loading colored image
img = cv.imread("/media/techio/Study Materials/Python Projects/arman.jpg")
img = cv.resize(img,(400,300))
b,g,r = cv.split(img)

grayed_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
hist = cv.calcHist([grayed_img],[0],None,[256],[0,256])

plt.plot(hist)
plt.title("Gray Image")
plt.show()

# Displaying all the images
cv.imshow("Img ",img)
cv.imshow("B",b)
cv.imshow("G",g)
cv.imshow("R",r)

# Plotting all the histogram
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.title("Colorful image")
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
