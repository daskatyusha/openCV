import cv2
import numpy as np

#####################
img_width = 640
img_height = 480
#####################
cap = cv2.VideoCapture(1)  # fixed webcam bug, my webcam broke tho
cap.set(3, img_width)
cap.set(4, img_height)
cap.set(10, 150)

def preProcessing(image):
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),1) #5,5 for kernel value
    imgCanny = cv2.Canny(imgBlur,150,450)   
    kernel = np.ones((5,5)) 
    imgDialation = cv2.dilate(imgCanny, kernel, iterations=2)
    #imgCanny has tiny lines which can be not useless sometimes, it can detect shadows etc. so we need to fix this
    imgDialation = cv2.dilate(imgCanny, kernel, iterations=2)
    imgThreshold = cv2.erode(imgDialation,kernel,iterations=1)

    return imgThreshold 

def getContours(image):
    biggest = np.array([])
    maxArea = 0
    contours,hierarchy = cv2.findContours(image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours: 
        area = cv2.contourArea(cnt)
        if area > 5000:
            #cv2.drawContours(imgContour,cnt,-1, (255,0,0), 2)
            perimeter = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*perimeter,True)
            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area
            #looking for biggest area loop

    cv2.drawContours(imgContour,biggest,-1, (255,0,0), 15)
    return biggest #returning biggest objects approx locations



while True:
    success, img = cap.read()
    img = cv2.resize(img,(img_width,img_height))
    imgContour = img.copy()
    imgThresholdOutput = preProcessing(img)
    biggest = getContours(imgThresholdOutput)
    cv2.imshow("Result", imgContour)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
