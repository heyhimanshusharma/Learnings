import cv2 as cv
import numpy as np

img = cv.imread('D:/Python/OpenCV/Photos/park.jpg')
cv.imshow('Image', img)

# Medium Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

cv.waitKey(0)