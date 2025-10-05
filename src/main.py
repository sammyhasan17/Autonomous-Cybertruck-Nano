
from picamera2 import Picamera2 # pip install picamera2

from time import sleep

cam = Picamera2()
cam.start_preview()

cam.start()

sleep(5)

cam.capture_file("test-1-image.jpg")
print("Image saved !!")

cam.stop()