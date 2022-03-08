# When we left click on image it will show cordinates
# and when we right click on image it will show color value

# importing library
import cv2 as cv
import numpy as np

def mouseEvent(event,x,y,flag,param):
    print("Event =",event)
    print("X =",x," Y =",y)
    print("Flag =",flag)
    print("Param =",param)
    print()

    font = cv.FONT_HERSHEY_COMPLEX
    # Left click event
    if event == cv.EVENT_LBUTTONDOWN:
        cord = ". ("+str(x)+","+str(y)+")"
        print(cord)
        cv.putText(img,cord,(x,y),font,0.5,(0,255,255),1,cv.LINE_AA)

    # Right click event
    if event == cv.EVENT_RBUTTONDOWN:

        b = img[y,x,0]
        g = img[y,x,1]
        r = img[y,x,2]
        colorBGR = ". ("+str(b)+","+str(g)+","+str(r)+")"
        cv.putText(img,colorBGR,(x,y),font,0.5,(0,255,255),1,cv.LINE_AA)
        
cv.namedWindow(winname = "Result")
# creating black image
img = np.zeros((600,800,3),np.uint8)
cv.setMouseCallback("Result",mouseEvent)

while True:
    cv.imshow("Result",img)
    if cv.waitKey(1) & 0xFF == 27: # Esc key
        break

cv.destroyAllWindows()
