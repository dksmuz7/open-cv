# Bitwise operation performing on a image
import cv2 as cv
import numpy as np

img1 = np.zeros((250,500,3),np.uint8)
img1 = cv.rectangle(img1,(150,100),(200,250),(255,255,255),-1)

img2 = np.zeros((250,500,3),np.uint8)
img2 = cv.rectangle(img2,(10,10),(170,190),(255,255,255),-1)

# Bitwise And
bitAnd = cv.bitwise_and(img1,img2)

# Bitwise OR
bitOr = cv.bitwise_or(img2,img1)

# Bitwise Not
bitNot = cv.bitwise_not(bitAnd)

# Bitwise Xor
bitXor = cv.bitwise_xor(img1,img2)

cv.imshow("win1",img1)
cv.imshow("win2",img2)
cv.imshow("Bitwise AND",bitAnd)
cv.imshow("Bitwise OR",bitOr)
cv.imshow("Bitwise NOT",bitNot)
cv.imshow("Bitwise XOR",bitXor)

if cv.waitKey(0) & 0xFF == 27:
    exit
cv.destroyAllWindows()