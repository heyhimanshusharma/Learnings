import cv2 as cv
import numpy as np

img = cv.imread('D:/Python/OpenCV/Photos/park.jpg')
cv.imshow('Image', img)

# Bilateral Blur
bilateral = cv.bilateralFilter(img, 20, 35, 15)
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)