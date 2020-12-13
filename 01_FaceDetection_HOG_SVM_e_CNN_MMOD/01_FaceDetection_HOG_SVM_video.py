#Usar
#python 01_FaceDetection_HOG_SVM_video.py

#Biblioteca
import dlib
import cv2
import time

#Carregar detector
hog_face_detector = dlib.get_frontal_face_detector()

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('EduardoMarinho01.mp4')
time.sleep(2.0)

cont=1
start = time.time()
while(cont<300):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = hog_face_detector(gray, 0)
    #faces = hog_face_detector(gray, 1)
    for (i, face) in enumerate(faces):
        cv2.rectangle(frame, (face.left(),face.top()), (face.right(),face.bottom()), (255,0,0), 2)
    cv2.imshow('Frame', frame)
    cont= cont+1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
end = time.time()
print('Tempo: {}'.format(end - start))
cap.release() 
cv2.destroyAllWindows()

