# Hand detection
import cv2 as cv
import numpy as np

img = cv.imread("/media/techio/Study Materials/Python Projects/hand.jpg")
img = cv.resize(img,(300,400))
img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

blur = cv.medianBlur(img_gray,5)
# Determining threshold value
ret,thres = cv.threshold(blur,235,255,cv.THRESH_BINARY_INV)

# Finding contours and drawing 
cnts,h = cv.findContours(thres,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
# cv.drawContours(img,cnts,-1,(50,50,150),2)
print("Total contours = ",len(cnts))

for cnt in cnts:
    epsilon = 0.0001*cv.arcLength(cnt,True)
    data = cv.approxPolyDP(cnt,epsilon,True)

    hull = cv.convexHull(data)
    cv.drawContours(img,[cnt],-1,(50,50,150),2)
    cv.drawContours(img,[hull],-1,(0,255,0),2)

# convexity defect
hull2 = cv.convexHull(cnts[0],returnPoints = False)
# defects return an array which contain value (start pt, end pt,farthest pt,approx)
defect = cv.convexityDefects(cnts[0],hull2)
for i in range(defect.shape[0]):
    s,e,f,d = defect[i,0]
    print(s,e,f,d)
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv.circle(img,far,5,[0,0,255],-1)

# Extreme pts
# topmost,bottommost, rightmost, leftmost
cmax = max(cnts,key=cv.contourArea)
extLeft = tuple(cmax[cmax[:,:,0].argmin()][0])
extRight = tuple(cmax[cmax[:,:,0].argmax()][0])
extTop = tuple(cmax[cmax[:,:,1].argmin()][0])
extBot = tuple(cmax[cmax[:,:,1].argmax()][0])

# drawing outline
cv.circle(img,extLeft,8,(255,0,255),-1) #pink
cv.circle(img,extRight,8,(0,125,255),-1) # brown
cv.circle(img,extTop,8,(255,10,0),-1) # blue
cv.circle(img,extBot,8,(19,152,152),-1) # green

cv.imshow("Original Image",img)
cv.imshow("Grayscale image",img_gray)
cv.imshow("Threshold",thres)
cv.waitKey(0)
cv.destroyAllWindows()