import cv2 as cv 
path = "images/Cat2.jpg"
img = cv.imread(path, 1)

def draw_circle(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img, (x,y), 20, (0,0,255), -1)
        cv.imshow('Image', img)

cv.imshow('Image', img)
cv.setMouseCallback('Image', draw_circle)

cv.waitKey(0)
cv.destroyAllWindows()