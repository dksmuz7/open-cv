# Equalization histogram
import cv2 as cv 
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread("/media/techio/Study Materials/Python Projects/arman.jpg")
img = cv.resize(img,(400,300))
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

equalization = cv.equalizeHist(gray_img)
res = np.hstack((gray_img,equalization))
cv.imshow("Equalized",res)
hist1 = cv.calcHist([equalization],[0],None,[256],[0,256])
plt.plot(hist1)
plt.title("Equalization")
plt.show()

# Contrast limited adaptive histogram equalization
clahe = cv.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
cl1 = clahe.apply(gray_img)
cv.imshow("Clahe",cl1)
hist2 = cv.calcHist([cl1],[0],None,[256],[0,256])
plt.plot(hist2)
plt.title("CLAHE")
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
