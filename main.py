from sys import argv
import torch
import numpy as np
from matplotlib import pyplot as plt
from preprocessing import do
import pyautogui
from time import sleep


class ActionClassifier(torch.nn.Module):
    def __init__(self):
        super(ActionClassifier, self).__init__()
        self.features = torch.nn.Sequential()
        self.classifier = torch.nn.Linear()

    def forward(self, x):
        x = self.features(x)
        x.view(-1, 0)
        out = self.classifier(x)
        return out


def main(argv):
    start_location = pyautogui.locateOnScreen("source/start_button.PNG")
    pyautogui.click(start_location)
    sleep(1)
    climb_location = pyautogui.locateOnScreen("source/climb.PNG")
    switch_location = pyautogui.locateOnScreen("source/switch.PNG")
    current = pyautogui.screenshot(region=(switch_location.left - 20, switch_location.top - 430, 320, 530))
    do(current)


if __name__ == '__main__':
    main(argv)
