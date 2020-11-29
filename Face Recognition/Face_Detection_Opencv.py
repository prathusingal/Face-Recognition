#pip install opencv-python
import numpy as np
import matplotlib.pyplot as plt
import cv2
img = plt.imread("group-photo1.png")
#img.shape
#plt.imshow(img)
detector = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
faces = detector.detectMultiScale(img)
for face in faces:
    x,y, w, h = face
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,255), 3)
plt.imshow(img)