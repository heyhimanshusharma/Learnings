import cv2 as cv
import numpy as np

img = cv.imread('D:/Python/OpenCV/Photos/park.jpg')
cv.imshow('Image', img)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

cv.waitKey(0)
