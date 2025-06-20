import cv2 as cv

img = cv.imread("D:/Python/openCV/Photos/cat.jpg")

cv.imshow('cat', img)

cv.waitKey(0)
