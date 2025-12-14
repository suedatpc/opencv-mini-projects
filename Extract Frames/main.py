import cv2 as cv 

def FrameCapture(path):
    vid = cv.VideoCapture(path)

    count = 0
    success = 1 

    while success:
        success, frame = vid.read() #will return tuple. First value is a boolean indicating if the read was successful. Second value is the frame itself.
        cv.imwrite("Frame%d.jpg" % count, frame)
        count += 1



if __name__ == "__main__":
    FrameCapture("Extract Frames/video1.mp4")