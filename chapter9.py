#FACE DETECTION
import cv2 

faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
#we are using prepared cascade (trained data), you can train your own tho.

img = cv2.imread("Resources/faces.jpg")
imgResize = cv2.resize(img,(1080,720))
imgGray = cv2.cvtColor(imgResize,cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(imgGray, 1.2, 4)

for (x,y,w,h) in faces:
    cv2.rectangle(imgResize,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow("Face",imgResize)
cv2.waitKey(0)