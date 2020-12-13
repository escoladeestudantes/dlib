#Usar
#python 02_FaceDetection_MMOD_video.py

#Biblioteca
import dlib
import cv2
import time

#Carregar detector
cnn_face_detector = dlib.cnn_face_detection_model_v1("./mmod_human_face_detector.dat")

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('EduardoMarinho01.mp4')
time.sleep(2.0)

cont=1
start = time.time()
while(cont<300):
    ret, frame = cap.read() 
    #faces = cnn_face_detector(frame, 0)
    faces = cnn_face_detector(frame, 1)
    for face in faces:
        cv2.rectangle(frame, (face.rect.left(),face.rect.top()), (face.rect.right(),face.rect.bottom()), (255,0,0), 2)
    cont= cont+1
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
end = time.time()
print('Tempo: {}'.format(end - start))
cap.release() 
cv2.destroyAllWindows()
