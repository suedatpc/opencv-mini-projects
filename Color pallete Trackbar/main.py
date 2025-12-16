import cv2 as cv
import numpy as np

def emptyFunc():
    pass

image = np.zeros((512,512,3), dtype='uint8')
windowName = "Open Cv Color Palette"

cv.namedWindow(windowName)

cv.createTrackbar('Blue', windowName, 0, 255, emptyFunc)
cv.createTrackbar('Green', windowName, 0, 255, emptyFunc)
cv.createTrackbar('Red', windowName, 0, 255, emptyFunc)


while True:
    cv.imshow(windowName, image)
    if cv.waitKey(1) == 27: #27 -> Esc key
        break

    blue = cv.getTrackbarPos('Blue', windowName)
    green = cv.getTrackbarPos('Green', windowName)
    red = cv.getTrackbarPos('Red', windowName)

    image[:] = [blue, green, red]