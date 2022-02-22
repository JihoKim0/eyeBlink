import dlib
import cv2
import numpy as np
import matplotlib as plt
import threading
import time

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

#얼굴 특징점 구분
RIGHT_EYEBROW_POINTS = list(range(17, 22))
lEFT_EYEBROW = list(range(22, 27))
RIGHT_EYE = list(range(36, 42))
LEFT_EYE = list(range(42, 48))
NOSE = list(range(27, 36))
MOUTH_OUTLINE = list(range(48, 61))
MOUTH_INNER = list(range(61, 68))
JAWLINE = list(range(0, 17))

#필요한 특징 정리해보기 - 왼/오 위/아래로 구분
LEFT_EYE_UP = list(range(43, 44))
LEFT_EYE_DOWN = list(range(46, 47))
RIGHT_EYE_UP = list(range(37, 38))
RIGHT_EYE_DOWN = list(range(40, 41))

def print1(x, y, w, h):
    print(x, y, w, h)
    threading.Timer(5, print1).start()

def detect(gray, frame):
    #find face
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)

    #find landmark on face
    for (x, y, w, h) in faces:
        dlib_rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))
        landmarks = np.matrix([[p.x, p.y] for p in predictor(frame, dlib_rect).parts()])
        #landmarks_display = landmarks[0:68] #put all points
        # put just eye points 
        landmarks_display = landmarks[RIGHT_EYE + LEFT_EYE]
        #print point
        for idx, point in enumerate(landmarks_display):
            pos = (point[0, 0], point[0, 1])
            cv2.circle(frame, pos, 2, color=(255, 0, 255), thickness=-1)
        for p in LEFT_EYE_UP.parts():
            print([p.x, p.y])
    return frame

video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while True:
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    canvas = detect(gray, frame)
    cv2.imshow("haha", canvas)


    if cv2.waitKey(1) & 0xFF == 27:  # esc키 입력시 창 닫기
            break

video_capture.release()
cv2.destroyAllWindows()