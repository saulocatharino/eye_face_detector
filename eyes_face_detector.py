#! /usr/bin/python3
# -*- coding:utf-8 -*-

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
def tudo():
	_, frame = cap.read()
	resim = frame

	gray = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
	saulo_detect = face_cascade.detectMultiScale(gray, 1.3, 5)

	for (x, y, w, h) in saulo_detect:
		cv2.rectangle(resim, (x, y), (x+w, y+h), (255, 0, 0), 2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = resim[y:y+h, x:x+w]
		goz_detect = eye_cascade.detectMultiScale(roi_gray)
		for (ex, ey, ew, eh) in goz_detect :
			cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 1)

	cv2.imshow('Detecção de Rosto e Olhos', resim )

	k = cv2.waitKey(30) & 0xff
	if k == 27:
		exit()
while True:
	tudo()



