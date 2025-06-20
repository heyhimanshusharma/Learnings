import cv2 as cv

img = cv.imread('D:/Python/OpenCV/Photos/park.jpg')
cv.imshow('Image', img)

# Flipping
flip_X = cv.flip(img, 0) # Vertically
cv.imshow("Flipped X", flip_X)

flip_Y = cv.flip(img, 1) # Horizontally
cv.imshow("Flipped Y", flip_Y)

flip_XY = cv.flip(img, -1) # Both (Vertically & Horizontally)
cv.imshow('Flipped XY', flip_XY)

cv.waitKey(0)
