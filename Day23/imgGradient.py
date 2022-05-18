# Image Gradient

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# loading image
img = cv.imread("/media/techio/Study Materials/Python Projects/balls.jpg")
img = cv.resize(img,(400,300));
img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Laplacian derivative
# for edge detection in image
lap = cv.Laplacian(img_gray,cv.CV_64F,ksize=3)
lap = np.uint8(np.absolute(lap))

# Using sobel operator
sobel_x = cv.Sobel(img_gray,cv.CV_64F,1,0,ksize=1) # 1 means x and 0 means y
sobel_y = cv.Sobel(img_gray,cv.CV_64F,0,1,ksize=1)
# For better result
sobel_y = np.uint8(np.absolute(sobel_y))
sobel_x = np.uint8(np.absolute(sobel_x))
# Combined
sobel = cv.bitwise_or(sobel_x,sobel_y)

# Displaying all images
# cv.imshow("Original image",img)
# cv.imshow("Grayed Image",img_gray)
# cv.imshow("laplacian image",lap)
# cv.imshow("Sobel x",sobel_x)
# cv.imshow("sobel y",sobel_y)
# cv.imshow("Sobel x  and  Sobel y combined",sobel)

titles = ["Original Image","Grayed Image","Laplacian Image","Sobel X","Sobel Y","Combined sobel x and y"]
imges = [img,img_gray,lap,sobel_x,sobel_y,sobel]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(imges[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
