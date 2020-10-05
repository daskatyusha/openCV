import cv2

img = cv2.imread("Resources\PP.png")

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #normally our img is RGB channeled(which is BGR in opencv)
#so this code simply turning BGR to GRAY
imgBlur = cv2.GaussianBlur(img,(7,7),0) #blurred image
imgCanny = cv2.Canny(img,125,175) #canny image

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.waitKey(0) #setting it to 0 means keep opened 