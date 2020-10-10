import cv2
import os

path = "image_classifier/ImageQuery"
orb = cv2.ORB_create(nfeatures=1000)

#### IMPORTING IMAGES
images = []
classNames = []
myList = os.listdir(path)
print(f"{len(myList)} classes detected.")

for cl in myList: # cl for class
    imgCurrent = cv2.imread(f"{path}/{cl}",0)
    images.append(imgCurrent) 
    classNames.append(os.path.splitext(cl)[0]) #we need to remove .jpg .png stuff

print(classNames)


def findDescriptor(images):
    descriptorList=[]
    for img in images:
        keyPoint, descriptor = orb.detectAndCompute(img, None)
        descriptorList.append(descriptor)
    return descriptorList


def findID(img, descriptorList, thres=15):
    keyPoint2, descriptor2 = orb.detectAndCompute(img, None) #descriptor of the current frame is descriptor2
    bf = cv2.BFMatcher()
    matchList= []
    finalValue = -1
    try:
        for descriptor in descriptorList:
            goodMatches = []
            matches = bf.knnMatch(descriptor, descriptor2, k=2) # k => we want 2 values that we can compare later on
            for m,n in matches: #m,n is 2 values that we planned ya know
                if m.distance < 0.75*n.distance:
                    goodMatches.append([m])
            matchList.append(len(goodMatches))
    except:
        pass

    print(matchList)
    if len(matchList)!=0:
        if max(matchList) > thres:
            finalValue = matchList.index(max(matchList)) #selecting index of maximum value
    
    return finalValue




descriptorList = findDescriptor(images)

cap = cv2.VideoCapture(1)

while True:
    
    success, img2 = cap.read()
    imgPure = img2.copy()
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


    id = findID(img2, descriptorList)
    if id != -1: # not an index of list
        cv2.putText(imgPure, classNames[id], (50,50), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)


    cv2.imshow("Camera", imgPure)
    if cv2.waitKey(1) & 0xFF ==ord("q"):
        break


