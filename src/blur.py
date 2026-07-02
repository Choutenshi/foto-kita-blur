import cv2

def apply(frame):
    return cv2.GaussianBlur(frame, (31, 31), 0)