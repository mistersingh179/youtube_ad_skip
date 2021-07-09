import os, sys
import cv2
import numpy as np
from helpers import *
from mss import mss
import time

template_images = load_template_images()

MOINTOR_NUMBER = 2

while True:
  with mss() as sct:
    mon = sct.monitors[MOINTOR_NUMBER]
    sct_img = sct.grab(mon)

  img_arr = np.array(sct_img)
  screen_image = cv2.resize(img_arr, (1920, 1080))
  screen_image = cv2.cvtColor(screen_image, cv2.COLOR_RGBA2RGB)
  image_with_annot = screen_image.copy()
  highlight_templates(image_with_annot, template_images)
  image_with_annot = cv2.resize(image_with_annot, (int(1920/3), int(1080/3)))
  cv2.imshow('debug', image_with_annot)
  locations = get_template_location(screen_image, template_images)
  location = locations[0]
  print(location)
  likelyhood, (x, y), (w,h) = location
  if likelyhood > 0.9:
    print('CLICKING!!!')
    click_at_skip_ad(x,y)
  if cv2.waitKey(1) == ord('q'):
    cv2.destroyAllWindows()
    sys.exit(0)

