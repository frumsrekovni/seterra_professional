from selenium import webdriver
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
PATH = "C:\Program Files (x86)\chromedriver.exe"
SITE = "https://online.seterra.com/en/vgp/3163"
prev_country = " "

driver = webdriver.Chrome(PATH)
driver.get(SITE)
driver.maximize_window()
driver.execute_script("window.scrollTo(0, 600)")  # Scroll down
#This zooms in the web browser whatever amount you enter after zoom=. Meant to solve the issue of the clickable surfaces not being visible but is now instead solved with this driver.execute_script("window.scrollTo(0, 500)") 
#driver.execute_script("document.body.style.zoom='50%'")

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "accept-choices"))) # Waits until the terms and conditions window is visible before clicking it
driver.find_element(By.ID, "accept-choices").click() # Accept the terms and conditions so it goes away
driver.find_element(By.ID, "cmdRestart").click() # Press the restart button in order to get a hilariously fast solve time


#Tried getting rid of the water that kept intercepting clicks but the problem is that 
#driver.execute_script("arguments[0].setAttribute('width',arguments[1])",driver.find_element(By.ID, "WATER"), "0")
if(SOLUTION == "WEBELEMENT"):
    while(True):
        currentQuestion = str(driver.find_element(By.ID, "currQuestion").text).replace('| Click on ','') # Convert to string and remove the filler text
        print("Current Question: ",currentQuestion)

        #This works to get the tiny rect over each country
        #countryInfo = driver.find_element(By.XPATH, "//path[contains(.,'GERMANY')]/following-sibling::rect")
        #Another option to achieve to same thing
        #countryInfo = driver.find_element(By.ID, "NETHERLANDS").find_element(By.XPATH, "//*[name()='rect']").get_attribute("x")

        #The info in data-qText is the most reliable in relation to what is parsed from currentQuestion
        #move_to_element(driver.find_element(By.XPATH,"//*[@data-qText='"+currentQuestion+"']"))
        
        #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@data-qText='"+currentQuestion+"']")))
        #driver.find_element(By.XPATH,"//*[@data-qText='"+currentQuestion+"']").click()
        #JavascriptExecutor executor = 
        #element = driver.find_element(By.XPATH,"//*[@data-qText='"+currentQuestion+"']")
        #driver.execute_script("arguments[0].click();", element)

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
        #pyautogui.moveTo(872, 148*2,1)
        driver.execute_script("window.scrollTo(0, 800)")
        #driver.execute_script("arguments[0].click()", element)
        prev_country = currentQuestion
elif(SOLUTION == "TEMPLATE"):
    swe_img = cv.imread('country_captures/sweden.png', cv.IMREAD_UNCHANGED)


time.sleep(100)
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