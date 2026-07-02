import cv2
import blur
from camera import Camera

camera = Camera()

blur_enabled = False
while True:
    frame = camera.read()

    if frame is None:
        break

    if blur_enabled:
        frame = blur.apply(frame)

    cv2.imshow("Foto Kita Blur", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("b"):
        blur_enabled = not blur_enabled
        print(f"Blur: {'ON' if blur_enabled else 'OFF'}")

    if key == ord("q"):
        break

camera.release()