
from picamera2 import Picamera2, Preview

from time import sleep

cam = Picamera2()
cam.start_preview(Preview.QT) #computationally heavy to preview!
cam.configure(cam.create_still_configuration(main={"size": (1920, 1080)}))      
# we need bounding boxes to that we can then implement avoidance logic
cam.start()

sleep(5)

cam.capture_file("test-1-image.jpg")
print("Image saved !!")

cam.stop()

# I need a continous stream using the picamera library


from ai_cameara import IMX500Detector
detector = IMX500Detector()
detector.start()
