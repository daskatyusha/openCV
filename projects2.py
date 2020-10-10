#DOCUMENT SCANNER
import cv2
import numpy as np

#IDEA: we are getting contours of biggest object in camera, sum all the locations of contours. 
#smallest sum is origin point which is like top left from your view.
#Biggest one is diagonal point which is bottom right.
#with this sum tactic we are understanding contours position shape.

#####################
img_width = 480
img_height = 640
#####################
cap = cv2.VideoCapture(1)  # fixed webcam bug, my webcam broke tho
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 150)

def preProcessing(img):
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
    biggestContours = np.array([]) #
    maxArea = 0
    contours,hierarchy = cv2.findContours(image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours: 
        area = cv2.contourArea(cnt)
        if area > 1500:
            #cv2.drawContours(imgContour,cnt,-1, (255,0,0), 2)
            perimeter = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.05*perimeter,True)

            if area > maxArea and len(approx) == 4:
                biggestContours = approx #setting biggest area corners as normal
                maxArea = area #setting biggest area as normal

            #if there is bigger thing exist, detect it.

    cv2.drawContours(imgContour,biggestContours,-1, (255,0,0), 15)
    return biggestContours #returning biggestContours objects approx locations

def reorder(myPoints):
    myPoints = myPoints.reshape((4,2))
    myPointsNew = np.zeros((4,1,2),np.int32) # this matrix should be the same with received parameter which is myPoints(biggestContours)
    add = myPoints.sum(1) #we are summing all the contours. 1 is axis.
    #print("add", add) #let's see what's going on with locations
    myPointsNew[0] = myPoints[np.argmin(add)] #find smallest one from add, get its index. 
    #Use this value as myPoints index value.
    myPointsNew[3] = myPoints[np.argmax(add)] #biggest of sum is bottom right

    diff = np.diff(myPoints,axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)] #top-right
    myPointsNew[2] = myPoints[np.argmax(diff)] #bottom-left
    return myPointsNew

def getWarp(image,biggestContours):
    biggestContours = reorder(biggestContours) #rearranged biggestContours points.
    pts1 = np.float32(biggestContours) #FLOAT32 ERROR IF OBJECT DOESN'T DETECT
    #4 corner locations. OUTPUT and these points sometimes doesn't
    #fit. We need to reorder them to fit shape of OUTPUT or INPUT. Their shapes must bu same.
    pts2 = np.float32([[0,0],[img_width,0],[0,img_height],[img_width,img_height]]) #OUTPUT
    matrix = cv2.getPerspectiveTransform(pts1,pts2)
    imgOutput = cv2.warpPerspective(image,matrix,(img_width,img_height))

    #QUALITY INCREASING
    imgCropped = imgOutput[20:imgOutput.shape[0]-20,20:imgOutput.shape[1]-20]
    imgCropped = cv2.resize(imgCropped,(img_width,img_height))
    return imgCropped


while True:
    success, img = cap.read()
    img = cv2.resize(img,(640,480))
    imgContour = img.copy()

    imgThresholdOutput = preProcessing(img)
    biggestContours = getContours(imgThresholdOutput)
    print(biggestContours.shape) #4,1,2 => 4 points with x,y each of them, we don't need 1 in here so we
    # are going to delete it in reorder
    
    cv2.imshow("Result", imgContour)

    try:
        imgWarped = getWarp(img,biggestContours)
        cv2.imshow("Warp", imgWarped)
    except:
        pass


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

