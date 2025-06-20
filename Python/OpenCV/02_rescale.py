# We resize images and movies to prevent computational strain
import cv2 as cv

img = cv.imread('d:/Python/openCV/Photos/cat.jpg')
cv.imshow('Cat', img)

def rescaleFrame(frame, scale=0.75):
    # Images, videos and live streams
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # Only for live videos
    capture.set(3, width)
    capture.set(4, height)

resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

capture = cv.VideoCapture('d:/Python/openCV/Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video Resize', frame_resized)

    if cv.waitKey(20) & 0xff==ord('d'):
        break

capture.release()
cv.destroyAllWindows