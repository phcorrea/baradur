import cv2

video_capture = cv2.VideoCapture(0)

def capture():
    ret, frame = video_capture.read()
    return frame

def exit():
    video_capture.release()
    cv2.destroyAllWindows()
