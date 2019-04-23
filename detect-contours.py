from scipy.spatial import distance as dist
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') 

img = cv2.imread('sachin.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.2, 5)

for (x,y,w,h) in faces: 
      
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = img[y:y+h, x:x+w] 
        ret, thresh = cv2.threshold(gray, 127, 255, 1)
        im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(img, contours, -1, (0,0,0), 1)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
