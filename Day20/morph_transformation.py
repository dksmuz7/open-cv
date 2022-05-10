# Morphological transformation

# It is applicable only for the binary image (grayscale)
# It needs two inputs original image and structuring element (kernel)

# Two types are
# Erosion and Dilation

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("/media/techio/Study Materials/Python Projects/balls.jpg",0)
img = cv.resize(img,(400,300))
# cv.imshow("Origianl image",img)

# Erosion - erodes the boundary of the image with the help of kernel
_,mask = cv.threshold(img,150,255,cv.THRESH_BINARY_INV)
# cv.imshow("Mask",mask)
kernel = np.ones((5,5),np.uint8) # 5x5 kernel with all ones
erroded_img = cv.erode(mask,kernel=kernel)
# cv.imshow("Eroded image",erroded_img)

# Dilation opposite of errosion works forground of the image
kernel2 = np.ones((1,1),np.uint8)
dilated_img = cv.dilate(mask,kernel)
# cv.imshow("Dilated image",dilated_img)

title = ["Image","Masked Image","Eroded Image","Dilated Image"]
images = [img,mask,erroded_img,dilated_img]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(title[i])
    plt.xticks([]),plt.yticks([])

plt.show()

if cv.waitKey(0) & 0xFF == ord('q'):
    exit()
cv.destroyAllWindows()