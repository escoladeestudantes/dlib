#python 03_Dlib_detector_image.py

import cv2
import dlib


detector = dlib.simple_object_detector("mask.svm")

frame = cv2.imread('/home/edee/Desktop/dlib_train/dataset/test/002.jpg')

detections = detector(frame)
if len(detections) > 0:
	print("Mascaras detectadas: {}".format(len(detections)))
	for k, d in enumerate(detections):
		print("Mascara {}: Left: {} Top: {} Right: {} Bottom: {}".format(
		k, d.left(), d.top(), d.right(), d.bottom()))
		cv2.rectangle(frame, (d.left(), d.top()), (d.right(), d.bottom()), (0, 0, 255), 2)
cv2.imshow("Frame", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
