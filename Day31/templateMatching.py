# Template matching using open cv
# It is a method of searching and finding the location of
# a template image in larger image. matchTemplate function can
# be used for this purpose (2D convolution)

import cv2 as cv
from cv2 import imshow
import numpy as np

path = "/media/techio/Study Materials/Python Projects/team.jpg"
img = cv.imread(path)

# Target image (to match with)
img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Loading template (to match from)
template = cv.imread("/media/techio/Study Materials/Python Projects/temp.png",0) # reading image in grayscale
w,h = template.shape[::-1]

# Template matching method
res = cv.matchTemplate(img_gray,template,cv.TM_CCORR_NORMED)
print("Res ",res)

thres = 0.92466 # Threshold value
loc = np.where(res>=thres) # Finding brightest pixels
print("Bright pixels : ",loc)

count = 0
for i in zip(*loc[::-1]):
    print("i = ",i)
    cv.rectangle(img,i,(i[0]+w,i[1]+h),(0,0,255),3)
    count+=1

print("Total iterations = ",count)

res = cv.resize(res,(500,300))
img = cv.resize(img,(500,300))
cv.imshow("Original image",img)
cv.imshow("Template matched",res)

cv.waitKey(0)
cv.destroyAllWindows()
