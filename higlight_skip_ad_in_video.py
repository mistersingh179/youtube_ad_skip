import os
import cv2
import numpy as np
from helpers import *

template_images = load_template_images()

video_path = 'videos/youtube_skip_ad_video2.mp4'
vcap = cv2.VideoCapture(video_path)

while True:
  success, frame = vcap.read()
  if success == False:
    break
  frame = cv2.resize(frame, (1920, 1080))
  highlight_templates(frame, template_images)
  #print(get_template_location(frame, template_images))
  cv2.imshow('frame', frame)
  keycode = cv2.waitKey(1)
  if keycode == ord('q'):
    break

vcap.release()
cv2.destroyAllWindows()
