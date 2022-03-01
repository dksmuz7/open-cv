# Accessing video from any url e.g. youtube.com
import cv2 as cv
import pafy
import youtube_dl


url = "https://youtu.be/ueeBT3zZtm0"
data = pafy.new(url)
data = data.getbest(preftype="mp4")
cap = cv.VideoCapture(0)
cap.open(data.url)
print("check==",cap.isOpened())

while cap.isOpened():
    ret,frame = cap.read()
    if ret == True:
        frame = cv.resize(frame,(16*50,9*50))
        grayFrame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY) # Converting frame to gray
        cv.imshow("Video from youtube",frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()