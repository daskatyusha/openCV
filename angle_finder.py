import cv2
import math
 
path = 'Resources/cards.jpg'
img = cv2.imread(path)
pointsList = []
 
def mousePoints(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        size = len(pointsList)
        if size != 0 and size % 3 != 0:
            cv2.line(img,tuple(pointsList[round((size-1)/3)*3]),(x,y),(0,0,255),2)
        # tuple part: put 2 for size (not divided by 3) rounding it to 0 and * with 3
        # pointsList[0] tuple for point1, then x,y which is function feature for point2
        # then draws a line between them.
        cv2.circle(img,(x,y),3,(255,0,0),cv2.FILLED)
        pointsList.append([x,y])
        print(pointsList)

#on left click if pointList is not empty and contains items their counts
#is not divided by 3 , draw a line
#draw a circle to clicked place
 
 
def gradient(pt1,pt2):
    return (pt2[1]-pt1[1])/(pt2[0]-pt1[0])
 #pt1 => [129, 5] 5 for height 129 for width
 #y2 - y1 // x2 - x1 for m

def getAngle(pointsList):
    pt1, pt2, pt3 = pointsList[-3:] #last 3 items of pointsList
    m1 = gradient(pt1,pt2)
    m2 = gradient(pt1,pt3)
    angR = math.atan((m2-m1)/(1+(m2*m1)))
    angD = round(math.degrees(angR))
 
    cv2.putText(img,str(angD),(pt1[0]-40,pt1[1]-20),cv2.FONT_HERSHEY_COMPLEX,
                1,(0,0,255),2)
 
while True:
 
 
    if len(pointsList) % 3 == 0 and len(pointsList) !=0:
        getAngle(pointsList)
 
    cv2.imshow('Image',img)
    cv2.setMouseCallback('Image',mousePoints)
    if cv2.waitKey(1) & 0xFF ==ord('r'):
        pointsList = []
        img = cv2.imread(path)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break