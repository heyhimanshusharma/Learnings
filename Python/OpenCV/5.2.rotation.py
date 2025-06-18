import cv2 as cv
import numpy as np

img = cv.imread('D:/Python/OpenCV/Photos/park.jpg')

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    
    return cv.warpAffine(img, rotMat, dimensions)
    
rotated = rotate(img, -45)
cv.imshow("Rotated", rotated)

rotated_rotated = rotate(rotated, -45)
cv.imshow('Rotated Rotated', rotated_rotated)

cv.waitKey(0)