from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

from bs4 import BeautifulSoup
import pandas as pd
import time
import numpy as np

import cv2 as cv
import pyautogui
from os import listdir
from os.path import isfile, join


SOLUTION = "WEBELEMENT"
prev_country = " "
ser = Service(ChromeDriverManager().install())
MAPS = ["https://online.seterra.com/en/vgp/3007","https://online.seterra.com/en/vgp/3003","https://online.seterra.com/en/vgp/3163","https://online.seterra.com/en/vgp/3254","https://online.seterra.com/en/vgp/3123","https://online.seterra.com/en/vgp/3023"]
chrome_options = Options()
chrome_options.add_extension(r'C:\Users\Joshua\Python\pro_seterra_player\extension_1_42_4_0.crx') # Noticed that there are different pop-ups that destroy the script in different ways. So now chrome boots up with ad block.
driver = webdriver.Chrome(service=ser,options=chrome_options)
for x in MAPS:
    driver.get(x)
    driver.maximize_window()
    driver.execute_script("window.scrollTo(0, 600)")  # Scroll down
    #This zooms in the web browser whatever amount you enter after zoom=. Meant to solve the issue of the clickable surfaces not being visible but is now instead solved with this driver.execute_script("window.scrollTo(0, 500)") 

    #WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "accept-choices"))) # Waits until the terms and conditions window is visible before clicking it
    #driver.find_element(By.ID, "accept-choices").click() # Accept the terms and conditions so it goes away
    #driver.execute_script("document.body.style.zoom='50%'")
    driver.find_element(By.ID, "cmdRestart").click() # Press the restart button in order to get a hilariously fast solve time

    #Tried getting rid of the water that kept intercepting clicks but the problem is that 
    #driver.execute_script("arguments[0].setAttribute('width',arguments[1])",driver.find_element(By.ID, "WATER"), "0")
    if(SOLUTION == "WEBELEMENT"):
        while(True):
            currentQuestion = str(driver.find_element(By.ID, "currQuestion").text).replace('| Click on ','') # Convert to string and remove the filler text
            if(currentQuestion == ""):
                break
            print("Current Question: ",currentQuestion)

            try:
                driver.find_element(By.XPATH,"//*[@data-qText='"+currentQuestion+"']").click()      
            except NoSuchElementException:
                print("IM IN NO SUCH ELEMENT EXCEPTION")
                element = driver.find_element(By.XPATH,"//*[@data-qText='"+currentQuestion+"']").find_element(By.TAG_NAME,"rect")
                webdriver.ActionChains(driver).move_to_element(element).click(element ).perform()
            except ElementClickInterceptedException:
                print("IM IN CLICK INTERCEPTED EXCEPTION")
                if(currentQuestion == prev_country):
                    element = driver.find_element(By.XPATH,"//*[@data-qText='"+currentQuestion+"']").find_element(By.TAG_NAME,"path")
                    webdriver.ActionChains(driver).move_to_element(element).click(element ).perform()
                else:
                    element = driver.find_element(By.XPATH,"//*[@data-qText='"+currentQuestion+"']").find_element(By.TAG_NAME,"rect")
                    webdriver.ActionChains(driver).move_to_element(element).click(element ).perform()

            driver.execute_script("window.scrollTo(0, 750)")
            prev_country = currentQuestion
    elif(SOLUTION == "TEMPLATE"):
        swe_img = cv.imread('country_captures/sweden.png', cv.IMREAD_UNCHANGED)

    print("MAP SOLVED!")
    time.sleep(2)
driver.quit()


#Below is code for using image recognistion in opencv and pyautogui to find the country and drag the mouse to solve it. Very inaccurate and unreliable.
# country_files = [f for f in listdir("country_captures/") if isfile(join("country_captures/", f))]

# mouse_speed = 0.1
# conf_value = 0.9
# conf_value_decrease = 0.05

# def locateCountry(countryName, mou_spee, conf, conf_dec):
#     cou_name = "country_captures/"+countryName
#     confid = conf
#     coor = pyautogui.locateCenterOnScreen(cou_name,confidence=confid)
#     while(confid != 0.0 and coor == None):
#         print("Location confidence(Lower is less confident): "+str(confid))
#         coor = pyautogui.locateCenterOnScreen(cou_name,confidence = confid)
#         confid -= conf_dec
#     if(coor != None):
#         pyautogui.moveTo(coor.x,coor.y,mou_spee)
    

# for x in country_files:
#     print("Trying to find: "+x)
#     locateCountry(x,mouse_speed,conf_value,conf_value_decrease)


# I have learnt alot about the differences between clicking on a webelement with selenium's click, executing a javascript script in order to click or using the ActionChains library in order to click.
# The selenium one visually is the most pleasing since it does not move around the screen. It just emulates a click. While ActionChains much more mimick the act of using the mouse to click on something
# which results in scrolling around on the screen alot.