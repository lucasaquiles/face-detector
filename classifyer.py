import numpy as np
import cv2 as cv
from collections import OrderedDict

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv.CascadeClassifier('haarcascade_smile.xml')

colors = [(19, 199, 109), (79, 76, 240), (230, 159, 23),
                  (168, 100, 168), (158, 163, 32),
                  (163, 38, 32), (180, 42, 220)]

FACIAL_LANDMARKS_INDEXES = OrderedDict([
    ("Mouth", (48, 68)),
    ("Right_Eyebrow", (17, 22)),
    ("Left_Eyebrow", (22, 27)),
    ("Right_Eye", (36, 42)),
    ("Left_Eye", (42, 48)),
    ("Nose", (27, 35)),
    ("Jaw", (0, 17))
])

img = cv.imread('sachin.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
facial_features_cordinates = {}
faces = face_cascade.detectMultiScale(gray, 1.2, 5)
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    
    overlay = img.copy()
    output = img.copy()

    eyes = eye_cascade.detectMultiScale(roi_gray)
    print overlay

    for (ex,ey,ew,eh) in eyes:
       cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    smile = smile_cascade.detectMultiScale(roi_gray)
    for (sx,sy,sw,sh) in smile:
     	cv.rectangle(roi_gray,(sx,sy),(sx+sw,sy+sh),(1,0,0),1)

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()
