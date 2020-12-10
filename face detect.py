import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
        Centre_x = (x+x+w)/2
        Centre_y = (y+y+h)/2
        print (Centre_x, Centre_y)
        
    cv2.imshow('img', img)
    k = cv2.waitKey (30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
            

        


    
