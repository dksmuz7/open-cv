# Change Background using Grabcut algorithm
# GrabCut algorithm helps to cutoff any foreground object
# from background object from image or video.
# It uses gaussian mixture model to achieve the target

import cv2 as cv
import numpy as np

img = cv.imread("/media/techio/Study Materials/Python Projects/arman.jpg")
img = cv.resize(img,(500,300))

# creating mask
mask = np.zeros(img.shape[:2],np.uint8)

# Creating model for foreground and background
bgModel = np.zeros((1,65),np.float64)*255
fgModel = np.zeros((1,65),np.float64)*255

rect = (139,0,318,299) # Foreground
# Findin foreGround using rectangle method
cv.grabCut(img,mask,rect,bgModel,fgModel,7,cv.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

cv.imshow("Result",img)

cv.waitKey(0)
cv.destroyAllWindows()