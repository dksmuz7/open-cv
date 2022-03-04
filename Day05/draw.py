# Drawing on an image

# Importing library
import cv2 as cv
import numpy as np

'''
path = "/media/deepaksagar/Study Materials/Graphic Design/background.png"

# Loading image
img = cv.imread(path)
img = cv.resize(img,(9*40,16*40)) # Resizing the image
'''

# Or on a blank created image
# np.ones parameter([width,height,channel],dtype)
img = np.ones([600,700,3],np.uint8)*100 #grayed background (*100)

# Drawing line on a image
# Acceptin parameter (img,(starting_pt),(ending_pt),(bgr),thickness)
img = cv.line(img,(0,0),(100,100),(0,255,255),5)

# Drawing arrow line
img = cv.arrowedLine(img,(0,0+100),(100,100+100),(0,255,255),5)

# Drawing rectangle
img = cv.rectangle(img,(120,50),(120+100,50+100),(0,255,255),5)

# Drawing filled rectangle give thickness as negative
img = cv.rectangle(img,(120,200),(120+100,200+100),(0,255,0),-1)

# Drawing circle, parameter (img,center,radius,color,thickness)
img = cv.circle(img,(300,100),50,(0,0,255),5)

# Filled circle
img = cv.circle(img,(300,250),50,(0,0,0),-1)

# Text on image, parameter(image,text,start_pt,end_pt,font,font_size,color,thickness,line_type)
font = cv.FONT_HERSHEY_SCRIPT_COMPLEX
img = cv.putText(img,'Text',(20,350),font,2,(0,255,255),1,cv.LINE_AA)

# Drawing ellipse,Parameter(img,center,(a,b),angle,start_angle,end_angle,(b,g,r),thickness)
img = cv.ellipse(img,(120,450),(100,50),0,0,180,(0,255,255),5)


# Displaying image in a window named Final Image
cv.imshow("Final Image",img)

if cv.waitKey(0) & 0xFF == ord('q'):
    exit()
cv.destroyAllWindows()