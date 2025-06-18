import cv2 as cv

img =  cv.imread('D:/Python/OpenCV/Photos/park.jpg')
cv.imshow('Image', img)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)