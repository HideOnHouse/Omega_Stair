from time import sleep

import cv2
import numpy as np
import pyautogui


def do(switch_location):
    """

    :param switch_location: location of switch button
    :return: preprocessed image
    """
    current = pyautogui.screenshot(region=(switch_location.left - 20, switch_location.top - 430, 320, 530))
    img_array = np.array(current)
    img_array = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
    img_array = cv2.resize(img_array, (30, 30), interpolation=cv2.INTER_CUBIC)
    return np.array(img_array)


def get_screen_information():
    """
    your source should located at ./source
    :return: locations of start button, climb button, switch button
    """
    start_location = pyautogui.locateOnScreen("source/start_button.PNG")
    pyautogui.click(start_location)
    sleep(1)
    climb_location = pyautogui.locateOnScreen("source/climb.PNG")
    switch_location = pyautogui.locateOnScreen("source/switch.PNG")
    return start_location, climb_location, switch_location


def make_dataset():
    while True:
        pass
