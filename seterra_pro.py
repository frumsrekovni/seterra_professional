import cv2 as cv
import pyautogui
from os import listdir
from os.path import isfile, join

country_files = [f for f in listdir("country_captures/") if isfile(join("country_captures/", f))]


mouse_speed = 0.1
conf_value = 0.9
conf_value_decrease = 0.02

def locateCountry(countryName, mou_spee, conf, conf_dec):
    cou_name = "country_captures/"+countryName
    confid = conf
    coor = pyautogui.locateCenterOnScreen(cou_name,confidence=confid)
    while(confid != 0.0 and coor == None):
        print("Location confidence(Lower is less confident): "+str(confid))
        coor = pyautogui.locateCenterOnScreen(cou_name,confidence = confid)
        confid -= conf_dec
    if(coor != None):
        pyautogui.moveTo(coor.x,coor.y,mou_spee)
    

for x in country_files:
    print("Trying to find: "+x)
    locateCountry(x,mouse_speed,conf_value,conf_value_decrease)
