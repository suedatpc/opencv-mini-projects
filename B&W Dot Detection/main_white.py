#White dot detection
import cv2 as cv
path = "B&W Dot Detection/white-dot.png"

gray = cv.imread(path, 0)

thresh, threshed = cv.threshold(gray, 100, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

contours = cv.findContours(threshed, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)[-2]

#filter by area
s1 = 3
s2 = 20
xcontours = []

for contour in contours:
    if s1 < cv.contourArea(contour) < s2:
        xcontours.append(contour)


print(f"Total number of white dot is {len(xcontours)}")