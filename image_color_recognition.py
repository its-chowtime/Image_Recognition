import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('preview.png',cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([0,180,160]) # Red 0 73 67
upper_red = np.array([150,190,180])

lower_green = np.array([0,255,60]) # Green 146 100 28
upper_green = np.array([180,255,80])

mask_red = cv2.inRange(hsv, lower_red, upper_red)
mask_green = cv2.inRange(hsv, lower_green, upper_green)

res_red = cv2.bitwise_and(img,img, mask= mask_red)
res_green = cv2.bitwise_and(img,img, mask= mask_green)

cv2.imshow('img',img)
# cv2.imshow('mask',mask_red)
# cv2.imshow('mask',mask_green)
cv2.imshow('res_red',res_red)
cv2.imshow('res_green',res_green)

cv2.waitKey(0)
cv2.destroyAllWindows()
