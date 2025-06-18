import cv2 as cv

capture = cv.VideoCapture('D:/Python/openCV/Videos/dog.mp4')
# Provide integer values as arguments if webcam is being used

while True:
    isTrue, frame = capture.read()

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xff == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
