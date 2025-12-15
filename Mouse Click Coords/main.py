#Displaying the coordinates of the points clicked on the image
import cv2 as cv

def click_event(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img, str(x) + "," + str(y), (x,y), font, 0.5, (0,0,255), 2)
        cv.imshow('Image', img)



if __name__ == "__main__":
    path = "Mouse Click Coords/Cat2.jpg"
    img = cv.imread(path, 1)

    cv.imshow('Image', img)

    cv.setMouseCallback('Image', click_event)

    cv.waitKey(0)
    cv.destroyAllWindows()