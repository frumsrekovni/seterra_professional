import pyautogui
from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth', 500)
import time
import requests
import random
import cv2

float confidence = 0.8

#page = requests.get("https://online.seterra.com/en/vgp/3199")


#soup = bs(page.content)


#print(soup.find(id='currQuestion').get_text())


#x, y = pyautogui.locateCenterOnScreen('finland.png')
x, y = pyautogui.locateCenterOnScreen('belgium.png',confidence=0.8)
pyautogui.moveTo(x, y, 0.2)
x, y = pyautogui.locateCenterOnScreen('ireland.png',confidence=0.8)
pyautogui.moveTo(x, y, 0.2)
x, y = pyautogui.locateCenterOnScreen('estonia.png',confidence=0.8)
pyautogui.moveTo(x, y, 0.2)
""" distance = 200
while distance > 0:
        pyautogui.drag(distance, 0, duration=0.5)   # move right
        distance -= 5
        pyautogui.drag(0, distance, duration=0.5)   # move down
        pyautogui.drag(-distance, 0, duration=0.5)  # move left
        distance -= 5
        pyautogui.drag(0, -distance, duration=0.5)  # move up """