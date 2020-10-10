import cv2

img1_pure = cv2.imread("image_classifier/ImageQuery/diabloQ.jpg",0)
img1 = cv2.resize(img1_pure, (800, 600))
img2 = cv2.imread("image_classifier/ImageTrain/pazartesi.jpg",0)

orb = cv2.ORB_create(nfeatures= 500)  #you can change feature value tho
# this algorithm finds 500 feature and for each feature,
# discribes it with 32 values

keyPoint1, descriptor1 = orb.detectAndCompute(img1, None) 
keyPoint2, descriptor2 = orb.detectAndCompute(img2, None)
imgKp1 = cv2.drawKeypoints(img1, keyPoint1, None)
imgKp2 = cv2.drawKeypoints(img2, keyPoint2, None)
#cv2.imshow("img1 with keypoints", imgKp1)
#cv2.imshow("img2 with keypoints", imgKp2)
# the idea of this project is simply matching descriptors and detecting highest similarities.
# to match descriptor we have algorithms too.
# brute force matter => it gets 1 descriptor and tries to match it with trying others one by one.
# We are going to use K nearest neighbours instead of brute force.

bf = cv2.BFMatcher()
matches = bf.knnMatch(descriptor1, descriptor2, k=2) # k => we want 2 values that we can compare later on

goodMatches = []
for m,n in matches: #m,n is 2 values that we planned ya know
    if m.distance < 0.75*n.distance:
        goodMatches.append([m])
print(len(goodMatches))

img3 = cv2.drawMatchesKnn(img1, keyPoint1, img2, keyPoint2, goodMatches, None, flags=2) # flags is how do you want to show?




#cv2.imshow("1", img1)
#cv2.imshow("2", img2)
cv2.imshow("Matched", img3)
cv2.waitKey(0)
