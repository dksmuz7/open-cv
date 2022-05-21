# Contour detection and moment finding
import cv2 as cv 
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("/media/techio/Study Materials/Python Projects/shapes.png")
img = cv.resize(img,(400,300))
img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# Finding threshold
ret,thresh = cv.threshold(img_gray,200,255,cv.THRESH_BINARY_INV)

# Find contours
cnts,h = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
print("Number of contours = ",cnts,"\ntotal contours = ",len(cnts))
print("Heirarchy = \n",h)

# Draw contrours
# img = cv.drawContours(img,cnts,-1,(0,100,0),2)
# Finding moments and drawing contours
areas = []
for cnt in cnts:
    M = cv.moments(cnt)
    print("M==\n",M)
    
    c_x = int(M["m10"]/M["m00"])
    c_y = int(M["m01"]/M["m00"])

    # Finding area
    area = cv.contourArea(cnt)
    areas.append(area)

    # contour approx
    epsilon = 0.01*cv.arcLength(cnt,True) #arc lenght
    data = cv.approxPolyDP(cnt,epsilon,True)

    # Convex Hull - Total area bounded used to provide convexity
    hull = cv.convexHull(data)

    # Bounding rectangel
    x,y,w,h = cv.boundingRect(hull)
    img = cv.rectangle(img,(x,y),(x+w,y+h),(125,10,10),3)

    cv.drawContours(img,cnts,-1,(0,100,0),2)
    cv.circle(img,(c_x,c_y),7,(255,255,255),-1)
    cv.putText(img,"center",(c_x-20,c_y-20),cv.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)

# Output
titles = ["Original Image","Grayed Image","Threshold"]
images = [img,img_gray,thresh]

for i in range(3):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()