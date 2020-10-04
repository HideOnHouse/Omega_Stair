import cv2
import numpy as np

"""
Capture Game image -> Preprocess -> return processed image as numpy array
"""


def do(current_image):
    img_array = np.array(current_image)
    img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
    img_array = cv2.resize(img_array, (30, 30), interpolation=cv2.INTER_CUBIC)
    return np.array(img_array)
