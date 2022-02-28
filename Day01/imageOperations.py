# Image Read and Write operations
from importlib.resources import path
import cv2 as cv # importing open cv library

path = input("Enter path of file : ")
# path = "/media/deepaksagar/Study Materials/Graphic Design/Flyer/flyer-02.png"

# Reading image in Colored format for color - 1
img = cv.imread(path,1)
resolution = (9*50,11*50)
img = cv.resize(img,resolution)
print(img)
cv.imshow("Colored Image",img)

# Reading image unchanged
img = cv.imread(path,-1)
resolution = (9*50,11*50)
img = cv.resize(img,resolution)
print(img)
cv.imshow("Original Image",img)

# Reading image in gray format, for gray - 0
img = cv.imread(path,0) #second parameter decide way of reading
resolution = (9*50,11*50)
img = cv.resize(img,resolution)
print(img)
cv.imshow("Gray Image",img)

# Flipping the image about x-axis,y-axis, both
# For x->0,y->1,xy-> -1
img = cv.flip(img,0)
cv.imshow("Flipped image",img)

# wait for having delay in closing the window
cv.waitKey()
cv.destroyAllWindows()