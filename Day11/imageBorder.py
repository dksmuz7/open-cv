# Creating image border
import cv2 as cv
import numpy as np

img = cv.imread("/media/deepaksagar/Study Materials/Graphic Design/Assets/pngwing.com (2).png")
img = cv.resize(img,(15*34,340))

# param (img,top_wid,bottom,left,right,type,val)
border = cv.copyMakeBorder(img,10,10,5,5,cv.BORDER_CONSTANT,value=[0,0,255])
cv.imshow("Constant Border",border)
border = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_DEFAULT,value=[0,0,255])
cv.imshow("Default Border",border)
border = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_ISOLATED,value=[0,0,255])
cv.imshow("Isolated Border",border)
border = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_WRAP,value=[0,0,255])
cv.imshow("Border wrap",border)

cv.imshow("Image",img)

if cv.waitKey(0) & 0xFF == 27:
    exit
cv.destroyAllWindows()