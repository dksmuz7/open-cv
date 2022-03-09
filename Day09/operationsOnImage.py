# Performing various operations on image

import cv2 as cv
import numpy as np

# Reading image
img = cv.imread("/media/deepaksagar/Study Materials/Graphic Design/desktop.png")

# Showing information for the observation
print("Shape =",img.shape)
print("No. of pixel values =",img.size)
print("Image data type =",img.dtype)
print("Image Type =",type(img))

# Spliting an image into its 3 channel
b,g,r = cv.split(img)

cv.imshow("Blue",b)
cv.imshow("Green",g)
cv.imshow("Red",r)
cv.imshow("Image",img)

# Merge operation on image
mr1 = cv.merge((r,g,b))
cv.imshow("RGB",mr1)

mr2 = cv.merge((g,b,r))
cv.imshow("GBR",mr2)

# Accessing pixel value by its row and column coordinates
px = img[100,100] # store coordinates in a variable
print("The pixel value of given coordinate =",px)

# Accessing only blue pixels
blue = img[100,100,0]
print("BLue =",blue)

if cv.waitKey(0) & 0xFF == 27:
    exit

cv.destroyAllWindows()