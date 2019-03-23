import cv2

import webcam
import face_detector

while True:
    frame = webcam.capture()

    face_detector.detect(frame)

    cv2.imshow('Video', frame)

    # Press Q to Exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


webcam.exit()
