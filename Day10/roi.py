# Finding and working on ROI (region of interest)

import cv2 as cv
import numpy as np

# Reading image
img = cv.imread("/media/deepaksagar/Study Materials/Graphic Design/Assets/pngwing.com (2).png")
img = cv.resize(img,(15*34,340))

# ROI
# (324,6) (386,6) (386,60) (324,60)
#[(y1:y2),(x1:x2)]
y1=6
x1=324
y2=60
x2=386
roi = img[y1:y2,x1:x2]
cv.imshow("ROI",roi)

# showing roi in different location of same image
img[50:50+y2-y1,400:400+x2-x1] = roi

# in the same way we can manupulate other image to but main thing
# is to be kept in mind that the resolution of both the image should
# should be same. Otherwise ROI will not be mapped properly

cv.imshow("Image",img)
if cv.waitKey(0) & 0xFF == 27:
    exit

cv.destroyAllWindows()