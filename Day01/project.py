# A simple image editor to convert original
# image into gray one

# Improting library
import cv2 as cv

# Taking location input
path = input("Enter the path with file name : ")

# Reading the image
img = cv.imread(path,0) #taking input as grayscale
img = cv.resize(img,(500,700))
cv.imshow(img)

# adding wait time and keybindig
k = cv.waitKey(0) & 0xFF
if k==ord('q'):
    cv.destroyAllWindows()
elif k==ord('s'):
    dest = ("Enter destination location with file name to save : ")
    cv.imwrite(dest,img)
    cv.destroyAllWindows()