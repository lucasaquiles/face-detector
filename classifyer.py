import numpy as np
import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv.CascadeClassifier('haarcascade_smile.xml')

img = cv.imread('/home/s2it_laquiles/Downloads/itatiba-team/giu.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.2, 5)
for (x,y,w,h) in faces:
    # cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    # roi_gray = gray[y:y+h, x:x+w]
    # roi_color = img[y:y+h, x:x+w]

    # eyes = eye_cascade.detectMultiScale(roi_gray)
    # print eyes
    # for (ex,ey,ew,eh) in eyes:
    #     cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    smile = smile_cascade.detectMultiScale(roi_gray)
    for (sx,sy,sw,sh) in smile:
    	 cv.rectangle(roi_color,(sx,sy),(sx+sw,sy+sh),(1,0,0),1)

cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()