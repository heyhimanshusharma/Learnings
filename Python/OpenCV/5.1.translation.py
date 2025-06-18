import cv2 as cv
import numpy as np

img = cv.imread('D:/Python/OpenCV/Photos/park.jpg')
cv.imshow('Park', img)

# Translation
def translate(img, x, y):
    translateMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, translateMat, dimensions)

# -x ---> Left
# -y ---> Up
# +x ---> Right
# +y ---> Down

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

cv.waitKey(0)