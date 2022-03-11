# image blending
import cv2 as cv
import numpy as np

img1 = cv.imread("/media/deepaksagar/Study Materials/Graphic Design/Assets/pngwing.com (2).png")
img1 = cv.resize(img1,(15*34,340))

img2 = cv.imread("/media/deepaksagar/Study Materials/Graphic Design/Assets/pngwing.com (4).png")
img2 = cv.resize(img2,(15*34,340))

# simple blending or adding (Not to do)
result = img1 + img2 # numpy addition
cv.imshow("Simple adding operation",result)

# Recommended way
result = cv.add(img1,img2);
cv.imshow("Add blending",result)

# extented version param(src1,alpha,src2,beta,gamma)
result = cv.addWeighted(img1,0.7,img2,0.3,0)
cv.imshow("weighted blending",result)

if cv.waitKey(0) & 0xFF == 27 :
    exit

cv.destroyAllWindows()
