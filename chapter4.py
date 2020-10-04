import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8) #512 x 512 box with RGB255 color options
#cv2.imshow("Test1",img) #black square

#img[:] = 255,0,0 
#cv2.imshow("Test2",img) #blue square



cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) #you can check features when you typing
#img.shape[1] => img height / [0] => img width
cv2.rectangle(img,(0,0),(200,250),(0,0,255),2)
cv2.circle(img,(400,50),30,(255,255,0),2)
cv2.putText(img,"EXAMPLE",(300,100),cv2.FONT_HERSHEY_SIMPLEX,0.75,(0,100,150),1)



cv2.imshow("All Features Image",img)
cv2.waitKey(0)
