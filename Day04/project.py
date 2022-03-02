# Screen recording project
import cv2 as cv
import pyautogui as ui
import numpy as np

res = ui.size()

# Filename with location to save recording files
fname = input("Enter file name with path : ")

# Frame rate
fps = 10.0

fourcc = cv.VideoWriter_fourcc(*'XVID')
output = cv.VideoWriter(fname,fourcc,fps,res)

# Creating recording module
cv.namedWindow("Live_Recording",cv.WINDOW_NORMAL)
cv.resizeWindow("Live_Recording",(600,400)) # resizing the window

while True:
    img = ui.screenshot() # it will take screenshot continuously
    frame = np.array(img)
    frame = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    output.write(frame)
    cv.imshow("Live_Recording",frame)
    if cv.waitKey(1) == ord('q'):
        break

output.release()
cv.destroyAllWindows()
