import dlib
import cv2

stream = cv2.VideoCapture(0)

face = dlib.get_frontal_face_detector()

def blurOut(face):
    # code to blur out faces

    return True

i = 0

while True:
    while((i % 3) != 0):
        (grabbed, frame) = stream.read()
        
