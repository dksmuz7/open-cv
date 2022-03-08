# Mouse event bindings
# importing library
import cv2 as cv
import numpy as np


def draw(event,x,y,flags,param):
    print("Flags =",flags) # unique for button clicked
    print("Param =",param) # process is going on

    # binding double left click to draw circle
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),75,(0,255,255),5)

    # binding middle button down to draw rectangle
    if event == cv.EVENT_MBUTTONDOWN:
        cv.rectangle(img,(x,y),(x+100,y+50),(0,255,255),5)

cv.namedWindow(winname = "Result")

# creating black image
img = np.zeros((600,800,3),np.uint8)
cv.setMouseCallback("Result",draw)

while True:
    cv.imshow("Result",img)
    if cv.waitKey(1) & 0xFF == 27: # 27= ESC key
        break

cv.destroyAllWindows()