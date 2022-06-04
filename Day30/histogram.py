# Image analyzing using histogram technique
# Find, plot and analyze
# Intensity distribution of an image
# It can extract information about contrast brightness and intensity etc.

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Plotting with colhist method
img = np.zeros((200,200),np.uint8)
cv.rectangle(img,(0,100),(200,200),(255),-1)
cv.rectangle(img,(0,50),(50,100),(127),-1)

# calculating histogram
hist = cv.calcHist([img],[0],None,[256],[0,256])

# Plotting histogram data
plt.plot(hist)
plt.show()

cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()
