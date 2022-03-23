import cv2 as cv

img = cv.imread("/media/deepaksagar/Study Materials/Python Projects/black_white.png")
img = cv.resize(img,(300,300))

cv.imshow("Original image",img)

_,th1 = cv.threshold(img,100,200,cv.THRESH_BINARY)
_,th2 = cv.threshold(img,100,200,cv.THRESH_BINARY_INV)
_,th3 = cv.threshold(img,100,200,cv.THRESH_TRUNC)
_,th4 = cv.threshold(img,100,200,cv.THRESH_TOZERO)

cv.imshow("Binary Thres",th1)
cv.imshow("Binary Inverse Thres",th2)
cv.imshow("Trunc Thres",th3)
cv.imshow("To zero",th4)

if cv.waitKey(0) & 0xFF == 27:
    exit

cv.destroyAllWindows()