import cv2
import numbers as np

img = cv2.imread("Resources/PP.png")
print(img.shape)

imgResize = cv2.resize(img,(200,500)) #openCV uses width as first parameter so width, height

imgCropped = img[0:200, 0:200] #normally we use height, width

cv2.imshow("Resized",imgResize)
cv2.imshow("Cropped", imgCropped)
cv2.waitKey(0)