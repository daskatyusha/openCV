# LIVE FACE DETECTION
import cv2

faceCascade = cv2.CascadeClassifier(
    "Resources/haarcascade_frontalface_default.xml")
# we are using prepared cascade (trained data), you can train your own tho.

cap = cv2.VideoCapture(1)#trying to solve "can't grab image" error for about 2 hours. Problem was webcam.
#who would have guessed that the problem might be the webcam
cap.set(3, 640)  # width
cap.set(4, 480)  # height


while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.5, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img, "Face", (x-10, y-10),
                    cv2.FONT_HERSHEY_DUPLEX, 4, (0, 255, 0), 2)
    cv2.imshow("Live Face Detection", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):  # press q to leave
        break
