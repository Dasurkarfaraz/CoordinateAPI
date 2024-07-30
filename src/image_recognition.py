import cv2
import numpy as np

def find_image_coordinates(screenshot_path, template_path):
    screenshot = cv2.imread(screenshot_path)
    template = cv2.imread(template_path)

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    top_left = max_loc
    h, w, _ = template.shape
    center_x = top_left[0] + w // 2
    center_y = top_left[1] + h // 2

    return center_x, center_y
