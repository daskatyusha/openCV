#WARP PERSPECTIVE

import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

width, height=250, 250
pts1 = np.float32([[564,169],[646,280],[464,366],[387,245]])
pts2 = np.float32([[0,0],[width,0],[width,height],[0,height]]) #creating new perspective view which has sync values of points
matrix = cv2.getPerspectiveTransform(pts1,pts2)

matrix_print = np.array(matrix) #wanna see matrix?
print(matrix_print)

imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image", img)
cv2.imshow("Warp Perspective", imgOutput)

cv2.waitKey(0)