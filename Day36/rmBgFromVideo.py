# Removing background from video for that we need to 
# extract the foreground moving object from the static 
# background. 

import numpy as np
import cv2 as cv

cap =  cv.VideoCapture(0)

algo1 = cv.createBackgroundSubtractorKNN()
algo2 = cv.createBackgroundSubtractorMOG2(detectShadows=True)

while True:
    ret,frame = cap.read()
    frame = cv.resize(frame,(480,320))
    res1 = algo1.apply(frame)
    res2 = algo2.apply(frame)

    cv.imshow("Original",frame)
    cv.imshow("Result 1",res1)
    cv.imshow("Result 2",res2)

    k = cv.waitKey(60)
    if k == 'q' or k==27:
        break

cap.release()
cv.destroyAllWindows()
