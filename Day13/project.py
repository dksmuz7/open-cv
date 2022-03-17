# Creating and Image blender using trackbars
import cv2 as cv
import numpy as np

img1 = cv.imread("/media/deepaksagar/Study Materials/Graphic Design/Assets/pngwing.com (2).png")
img1 = cv.resize(img1,(15*34,340))

img2 = cv.imread("/media/deepaksagar/Study Materials/Graphic Design/Assets/pngwing.com (4).png")
img2 = cv.resize(img2,(15*34,340))

def empty():
    pass

img = np.zeros((400,400,3),np.uint8)
cv.namedWindow("Trackbar")
cv.createTrackbar("alpha","Trackbar",1,100,empty)
switch = "0 : OFF \n 1 : ON"
cv.createTrackbar(switch,"Trackbar",0,1,empty)

while True:
    s = cv.getTrackbarPos(switch,"Trackbar")
    a = cv.getTrackbarPos("alpha","Trackbar")
    n = float(a/100)
    print(n)

    if s==0:
        dst = img[:]
    else:
        dst = cv.addWeighted(img1,1-n,img2,n,0)
        cv.putText(dst,str(a),(20,20),cv.FONT_ITALIC,0.5,(0,255,255),1,cv.LINE_AA)

    cv.imshow("DST",dst)
    if cv.waitKey(1) & 0xFF == 27:
        break

cv.destroyAllWindows()