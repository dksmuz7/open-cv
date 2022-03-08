# drawing on video
# import required library
from tkinter import font
import cv2 as cv
import datetime as dt

from matplotlib.pyplot import gray, text

path = "/media/deepaksagar/Study Materials/Learn Photoshop in Hindi, Photo Cutout, Background Change.mp4"
cap = cv.VideoCapture(path)
print("Width =",cap.get(cv.CAP_PROP_FRAME_WIDTH))
print("Height =",cap.get(cv.CAP_PROP_FRAME_HEIGHT))

while cap.isOpened():
    ret,frame = cap.read()
    frame = cv.resize(frame,(40*16,40*9))
    if ret == True:
        font = cv.FONT_HERSHEY_COMPLEX
        text = ' Height: '+str(cap.get(4))+' Width: '+str(cap.get(3))
        frame = cv.putText(frame,text,(10,20),font,0.5,(0,0,0),1,cv.LINE_AA)

        # Printing date and time on video
        dateData = 'Date : '+str(dt.datetime.now())
        frame = cv.putText(frame,dateData,(20,40),font,0.5,(0,0,0),1,cv.LINE_AA)

        # Drawing rectangle on video
        frame = cv.rectangle(frame,(100,100),(200,200),(0,255,255),2)

        cv.imshow("Video",frame)

        if cv.waitKey(30) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()

