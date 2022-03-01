# Accessing webcam and saving video in hardisk
# importing library
import cv2 as cv

cap = cv.VideoCapture(0) # 0-> Internal webcam, 1-> External webcam
print("Cap is Opened",cap.isOpened())

# For saving the read video
# Video formats - DIVX, XVID, MJPG, X264,WMV1, WMV2
# Recommended - XVID - best quality
fourcc = cv.VideoWriter_fourcc(*"XVID") # Codec 4byte(video manager)
fps = 60
res = (16*50,9*50)
dest="output.mp4"
output = cv.VideoWriter(dest,fourcc,fps,res) # add more parameter 0 for gray scale image

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        # frame = cv.resize(frame,(16*50,9*50)) # Resizing frame
        frame = cv.flip(frame,1)
        grayFrame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY) # Converting frame to gray
        cv.imshow("Frame",frame)
        cv.imshow("Grayscale video",grayFrame)
        output.write(frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv.destroyAllWindows()