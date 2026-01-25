from picamera2 import Picamera2
from picamera2.devices import IMX500
import time

# Open camera
picam2 = Picamera2()

# Load IMX500 model
imx500 = IMX500("/usr/share/rpi-camera-assets/imx500_mobilenet_ssd.json")

# Attach IMX500 as post-processor
picam2.post_callback = imx500

# IMPORTANT: NO main stream at all
config = picam2.create_video_configuration(
    controls={"FrameRate": 20}
)

picam2.configure(config)
picam2.start()

print("IMX500 inference running (metadata only)")

start = time.time()
while time.time() - start < 10:
    metadata = picam2.capture_metadata()
    detections = metadata.get("imx500.object_detect", [])
    if detections:
        print(detections)
    time.sleep(0.05)

picam2.stop()
