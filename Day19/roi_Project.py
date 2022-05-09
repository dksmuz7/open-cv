import cv2 as cv
import numpy as np

# Image path (locations)
path1 = "" # paste location of image 1
path2 = "" # paste location of image 2

# Load two different images
img1 = cv.imread(path1)
img2 = cv.imread(path2)

# Resizing the image
img1 = cv.resize(img1,(1024,650))
img2 = cv.resize(img2,(600,650))

# extracting rows columns and channel from the image 2
r,c,ch = img2.shape

# Finding ROI from image 1 (y,x)
roi = img1[0:r,0:c]

# Creating mask for image 1
img_gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)

# Now creating mask using thresholding technique
th_val = 50 # threshold value
_,mask = cv.threshold(img_gray,th_val,255,cv.THRESH_BINARY)

# Now removing background from the image
mask_inv = cv.bitwise_not(mask)

# Now placing the mask on the ROI
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)

# Extracting onlu required part of the image from image 2
img2_fg = cv.bitwise_and(img2,img2,mask = mask)

# Now placing final colored extracted image to the image 1
res = cv.add(img1_bg,img2_fg)

final_img = img1
final_img[0:r,0:c] = res # roi of image 1 replaced with result

# Now displaying all the image
cv.imshow("Image 1",img1)
cv.imshow("Image 2",img2)
cv.imshow("Step - 1, Gray Image",img_gray)
cv.imshow("Step - 2, Mask",mask)
cv.imshow("Step - 3, Inverse Mask",mask_inv)
cv.imshow("Step - 4, Bg Mask",img1_bg)
cv.imshow("Step - 5, Fg Mask",img2_fg)
cv.imshow("Step - 6, Resulted ROI",res)
cv.imshow("Step - 7, Final Image",final_img)

cv.waitKey(0)
cv.destroyAllWindows()