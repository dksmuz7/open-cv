# Image smoothing or bluring is most common used operation in image ProcessingInstruction
# Remove noise,filters, LPF, HPF

# Homogeneous,blur,gaussian,median,bilateral

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("/media/techio/Study Materials/Python Projects/noisy.jpg")
img = cv.resize(img,(400,400))
# cv.imshow("Original",img)

# kernel for homogenous function
kernel = np.ones((5,5),np.float32)/25

# First filter operator (Homogeneous filter)
h_filter = cv.filter2D(img,-1,kernel) # -1 is desired depth
# cv.imshow("Homogeneous",h_filter)

# Second filter (averaging method)
blur = cv.blur(img,(8,8)) # kernel = 8x8
# cv.imshow("Blur",blur)

# Third filte - Gaussian filter
gaussian = cv.GaussianBlur(img,(5,5),0)
# cv.imshow("Gaussian Blur", gaussian)

# Fourth filter - Median Filter
med = cv.medianBlur(img,5)
# cv.imshow("Median Filter",med)

# Fifth - Bilateral filter
bilateral = cv.bilateralFilter(img,9,75,75)
# cv.imshow("Bilateral Filter",bilateral)

images = [img,h_filter,blur,gaussian,med,bilateral]
titles = ["Original Image","Homogeneous Filter","Blur","Gaussian Filter","Median Filter","Bilateral Filter"]

for i in range(6):
    plt.subplot(2,3,i+1),
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

if cv.waitKey(0) & 0xFF == ord('q'):
    exit()

cv.destroyAllWindows()