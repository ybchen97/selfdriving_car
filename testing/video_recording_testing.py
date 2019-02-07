# import the necessary packages
import cv2
import time
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
from datetime import datetime

# 1d timestamp array log
time_log = []
video_array = np.array([])

with PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 10
    time.sleep(0.5)
    start = time.time()
    with PiRGBArray(camera) as stream:
        for frame in camera.capture_continuous(stream, format='bgr', use_video_port=True):
            timestamp = datetime.now()
            time_log.append(timestamp)
            image = frame.array
            print(image)
            print('image captured')
            video_array = np.append(video_array, image)
            print('image appended')
            stream.truncate(0)
            if time.time() - start > 2:
                break

print(video_array)