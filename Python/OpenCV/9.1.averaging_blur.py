import cv2 as cv
import numpy as np

img = cv.imread('D:/Python/OpenCV/Photos/park.jpg')
cv.imshow('Image', img)

# Averaging
average = cv.blur(img, (7,7))
cv.imshow('Avg blur', average)

cv.waitKey(0)