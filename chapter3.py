import cv2
import numbers as np

img = cv2.imread("Resources/PP.png")
print(img.shape)

imgResize = cv2.resize(img,(200,500)) #width, height

imgCropped = img[0:200, 0:200] #height, width

cv2.imshow("Resized",imgResize)
cv2.imshow("Cropped", imgCropped)
cv2.waitKey(0)