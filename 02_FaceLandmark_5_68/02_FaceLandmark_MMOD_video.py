#Usar
#python 02_FaceLandmark_MMOD_video.py

#Biblioteca
import dlib
import cv2
import time

#Carregar detector
cnn_face_detector = dlib.cnn_face_detection_model_v1("./mmod_human_face_detector.dat")
#predictor = dlib.shape_predictor('shape_predictor_5_face_landmarks.dat')
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

#cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('EduardoMarinho01.mp4')
cap = cv2.VideoCapture('FabioBrazza01.mp4')
time.sleep(2.0)

#cont=1
cont=200
start = time.time()
while(cont<300):
    ret, frame = cap.read()
    faces = cnn_face_detector(frame, 0)
    for face in faces:
        shape = predictor(frame, face.rect)
        #for i in range(0,5):
        for i in range(0,68):
            #print(shape.part(i))
            cv2.circle(frame, (shape.part(i).x, shape.part(i).y), 1, (0,255,0), thickness=-1)
        cv2.rectangle(frame, (face.rect.left(),face.rect.top()), (face.rect.right(),face.rect.bottom()), (255,0,0), 2)
    cv2.imshow('Frame', frame)
    cont= cont+1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
end = time.time()
print('Tempo: {}'.format(end - start))
cap.release() 
cv2.destroyAllWindows()

