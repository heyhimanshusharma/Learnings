import cv2 as cv

img = cv.imread("D:/Python/OpenCV/Photos/park.jpg")
cv.imshow('Park', img)

# BGR to Grayscale (Practice)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB
LAB = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', LAB)

# BGR to RGB
RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', RGB)

# HSV to BGR
LAB_BGR = cv.cvtColor(LAB, cv.COLOR_LAB2BGR)
cv.imshow('LAB ---> BGR', LAB_BGR)

cv.waitKey(0)