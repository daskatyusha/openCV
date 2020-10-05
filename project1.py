import cv2
import numpy as np

cap = cv2.VideoCapture(1)
cap.set(3, 640)
cap.set(4, 480)

myColours = [[27, 129, 110, 45, 255, 255], [
    45, 150, 87, 92, 255, 255]]  # YELLOW, GREEN (colour HSV values)

myColourValues = [[0, 255, 255], [0, 255, 0]]  # BGR

myPoints = []  # [x, y, colorIx] this list saving all point data


def findColour(image, colours, colourValues):
    imgHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in colours:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)  # mask generated
        # setting x and y locations as returning x and y
        x, y = getContours(mask)
        # let's create circle at top center location of pen
        cv2.circle(imgResult, (x, y), 10, colourValues[count], cv2.FILLED)
        if x != 0 and y != 0:  # on pen shown
            newPoints.append([x, y, count])
        count += 1
        # cv2.imshow(str(color[2]), mask) #shows our masks
    return newPoints


def getContours(image):
    contours, hierarchy = cv2.findContours(
        image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0  # no detect, set 0,0 for x,y
    for cnt in contours:
        area = cv2.contourArea(cnt)  # for every contour, we set an area
        if area > 500:
            # cv2.drawContours(imgResult,cnt,-1, (255,0,0), 3)
            # AFTER USED UP: we dont need contour lines now, we know they are detected.
            perimeter = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*perimeter, True)
            x, y, w, h = cv2.boundingRect(approx)

    return x+w//2, y  # returning top center location of pen if exist


def drawOnCanvas(points, colourValues):
    for point in points:
        # create circle at top center location of pen
        cv2.circle(imgResult, (point[0], point[1]),
                   10, colourValues[point[2]], cv2.FILLED)  # x=first parameter of myPoints list, y = second, colourIx = third


while True:
    success, img = cap.read()
    imgResult = img.copy()
    # we need to define newPoints in here too,
    newPoints = findColour(img, myColours,  myColourValues)
    # or it doesn't detect from function..???

    if len(newPoints) != 0:
        for newP in newPoints:
            # if there is a pen in screen, add its locations and colour index to myPoints list
            myPoints.append(newP)

    print(newPoints)  # x,y,whichColour of new points
    print("NP")
    #print(myPoints)  # x,y,whichColour of all points
    #print("MP")

    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColourValues)

    cv2.imshow("Webcam", imgResult)  # because we are boxing the imgResult
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
