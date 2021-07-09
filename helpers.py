import os
import cv2
import numpy as np
import pyautogui

def load_template_images():
  template_images = []
  for template in os.listdir('templates'):
    if template.find('template') != 0:
      continue
    else:
      img = cv2.imread('templates/'+template, cv2.IMREAD_UNCHANGED)
      img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
      template_images.append(img)
  return template_images

def highlight_templates(frame, template_images,count=10):
  locations = get_template_location(frame, template_images)
  for index, location in enumerate(locations[:count]):
    likelyhood, (x, y), (w,h) = location
    cv2.putText(frame, "Likelyhood: ", (100, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
    cv2.putText(frame, str(round(likelyhood, 2)), (100, 350 + (50 * index)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
    cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 2)


def get_template_location(frame, template_images):
  items = []
  for index, template_image in enumerate(template_images):
    h, w, _ = template_image.shape
    template_match_result = cv2.matchTemplate(frame, template_image, cv2.TM_CCOEFF_NORMED)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(template_match_result)
    items.append((maxVal, maxLoc, (w,h)))
  items.sort(key=lambda item: item[0], reverse=True)
  return items

def click_at_skip_ad(x,y):
  # In Image of size (1920,1080) we found match at (1005, 771)
  # so what are the coordinates when image size is (1536 and 960)
  monitor_width = 1536
  monitor_height = 960

  image_width = 1920
  image_height = 1080

  x = (x / image_width) * monitor_width
  y = (y / image_height) * monitor_height
  x_on_left_screen = -(monitor_width - x)

  original_position = pyautogui.position()
  pyautogui.moveTo(x_on_left_screen, y)
  pyautogui.click()  # to select the window
  pyautogui.click()
  pyautogui.moveTo(*original_position)  # to come back where we were
  pyautogui.click()  # to click back where we were