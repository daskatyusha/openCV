import cv2

cap = cv2.VideoCapture(1)  # fixed webcam bug, my webcam broke tho
cap.set(3, 640) #width code= 3
cap.set(4, 480) #height code = 4
cap.set(10, 150) #brightness code = 10

while True:
    success, img = cap.read()
    cv2.imshow("Webcam", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
