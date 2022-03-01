# Operations on video
# importing library
import cv2 as cv

# path of file with filename
# path = input("Enter video file path : ")
path = "/media/deepaksagar/Study Materials/Learn Photoshop in Hindi, Photo Cutout, Background Change.mp4"

cap = cv.VideoCapture(path)
print("Cap",cap)

while True:
    ret, frame = cap.read()
    frame = cv.resize(frame,(16*50,9*50)) # Resizing frame
    grayFrame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY) # Converting frame to gray
    cv.imshow("Frame",frame)
    cv.imshow("Grayscale video",grayFrame)
    k = cv.waitKey(25) # 25 -> Frame rate
    if k== ord('q'):
        break

cap.release()
cv.destroyAllWindows()