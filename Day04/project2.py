# 2nd project
# Break video into frames for the analysis purposes

# improting modules
import cv2 as cv

# Path of the video file
path = input("Enter video file name followed by location : ")
vidCap = cv.VideoCapture(path)
ret, image = vidCap.read()
count = 0

while True:
    if ret == True:
        cv.imwrite("frames/img%d.jpg" %count,image)
        vidCap.set(cv.CAP_PROP_POS_MSEC,(count**100))
        ret,image = vidCap.read()
        cv.imshow("res",image)

        count += 1
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
            cv.destroyAllWindows()

vidCap.release()
cv.destroyAllWindows()
