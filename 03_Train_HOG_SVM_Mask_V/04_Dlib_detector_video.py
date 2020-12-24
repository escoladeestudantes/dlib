#python 04_Dlib_detector_video.py

import cv2
import dlib


detector = dlib.simple_object_detector("mask.svm")

cam = cv2.VideoCapture('/home/edee/Desktop/dlib_train/mask_test.mp4')

while cam.isOpened():
	ret, frame = cam.read()
	orig = frame.copy()
	detections = detector(frame)
	if len(detections) > 0:
		for (i, mask) in enumerate(detections):
			cv2.rectangle(frame, (mask.left(),mask.top()), (mask.right(),mask.bottom()), (0,255,0), 4)
	cv2.imshow("Frame", cv2.resize(frame, (int(0.5*frame.shape[1]), int(0.5*frame.shape[0]))))
	key = cv2.waitKey(1) & 0xff
	if key == 27:
		break
cv2.waitKey(0)
cv2.destroyAllWindows()
