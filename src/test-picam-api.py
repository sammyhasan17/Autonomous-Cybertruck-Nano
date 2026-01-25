import time
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder # turn frames into a video stream 
from picamera2.outputs import FileOutput # video stream to mp4 file
from picamera2.previews import QtPreview

picam2 = Picamera2()

video_config = picam2.create_video_configuration()
picam2.configure(video_config)

picam2.start_preview(QtPreview())

encoder = H264Encoder(bitrate=10_000_000)
output = FileOutput("test.mp4")

picam2.start_recording(encoder, output)
time.sleep(5)
picam2.stop_recording()
picam2.stop_preview()

picam2.stop()

