import cv2
import blur
from camera import Camera
from gesture import GestureDetector

camera = Camera()
gesture = GestureDetector()

blur_enabled = False

try:
    while True:
        frame = camera.read()

        if frame is None:
            break

        peace_detected = gesture.detect(frame)

        if peace_detected:
            print("Peace sign detected!")

        if blur_enabled or peace_detected:
            frame = blur.apply(frame)

        cv2.imshow("Foto Kita Blur", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("b"):
            blur_enabled = not blur_enabled
            print(f"Blur: {'ON' if blur_enabled else 'OFF'}")

        if key == ord("q"):
            break
finally:
    camera.release()