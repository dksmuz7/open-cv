# Building color picker using trackbars

import cv2 as cv 
import numpy as np

def empty(x):
    pass

# blank image
img = np.zeros((300,512,3),np.uint8)
cv.namedWindow("Color Picker")

# Creating switch
s1 = "0:OFF\n1:ON\n"
cv.createTrackbar(s1,"Color Picker",0,1,empty)

# Creating trackbars for rgb (setting)
cv.createTrackbar("R","Color Picker",0,255,empty)
cv.createTrackbar("G","Color Picker",0,255,empty)
cv.createTrackbar("B","Color Picker",0,255,empty)


while True:
    cv.imshow("Color Picker",img)

    k = cv.waitKey(1) & 0xFF
    if k==27: # for exit press esc
        break

    # getting trackbar position
    s = cv.getTrackbarPos(s1,"Color Picker")
    r = cv.getTrackbarPos("R","Color Picker")
    g = cv.getTrackbarPos("G","Color Picker")
    b = cv.getTrackbarPos("B","Color Picker")

    if s == 0:
        img[:] = 0 # black screen
    else:
        img[:] = [b,g,r] # setting colors to all pixels

cv.destroyAllWindows()