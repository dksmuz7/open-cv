# All morphological operations (to observe shapes in images)

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# opening - errosion followed by dilation
img = cv.imread("/media/techio/Study Materials/Python Projects/arman.jpg",0)
img = cv.resize(img,(400,300))

# creating simple mask
_,mask = cv.threshold(img,90,255,cv.THRESH_BINARY_INV)

# Creating kernal(mask)
kernel = np.ones((1,1),np.uint8)

opening = cv.morphologyEx(mask,cv.MORPH_OPEN,kernel)

kernel = np.ones((1,1),np.uint8)
closing = cv.morphologyEx(mask,cv.MORPH_CLOSE,kernel)

kernel = np.ones((2,2),np.uint8)
x1 = cv.morphologyEx(mask,cv.MORPH_TOPHAT,kernel) # diff b/w mask and opening
x2 = cv.morphologyEx(mask,cv.MORPH_GRADIENT,kernel) # diff b/w dilation and erosion
x3 = cv.morphologyEx(mask,cv.MORPH_BLACKHAT,kernel) # diff b/w closing and input image

images = [img,kernel,mask,opening,closing,x1,x2,x3]
titles = ["Original image","kernel","mask","opening","closing","x1","x2","x3"]

for i in range (8):
    plt.subplot(2,4,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

# cv.imshow("Original Image",img)
# cv.imshow("Kernal",kernel)
# cv.imshow("mask",mask)
# cv.imshow("Opening ",opening)
# cv.imshow("closing",closing)
# cv.imshow("X1",x1)

if cv.waitKey(0) & 0xFF == ord('q'):
    exit()
cv.destroyAllWindows()