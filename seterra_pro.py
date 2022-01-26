from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time

import cv2 as cv
import pyautogui
from os import listdir
from os.path import isfile, join
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://online.seterra.com/en/vgp/3229")
#driver.execute_script("document.body.style.zoom='50%'")
time.sleep(3)
driver.find_element(By.ID, "accept-choices").click()
driver.execute_script("window.scrollTo(0, 500)") 
time.sleep(1)
driver.find_element(By.ID, "cmdRestart").click()
#content = driver.page_source
#soup = BeautifulSoup(content)
while(True):
    #currentQuestion = driver.find_element(By.ID, "currQuestion").text.split()[-1]
    currentQuestion = str(driver.find_element(By.ID, "currQuestion").text).replace('| Click on ','')
    #refinedCurrentQuestion = currentQuestion.replace(' ', '_')

    print("Current Question: ")
    print(currentQuestion)
    #str(currentQuestion).upper()
    #By.xpath("//ID[contains(.,'GERMANY')]/following-sibling::rect"))
    #findElement(By.xpath("following-sibling::*"))
    #countryInfo = driver.find_element(By.XPATH, "//path[contains(.,'GERMANY')]/following-sibling::rect")
    #countryInfo = driver.find_element(By.ID, "NETHERLANDS").find_element(By.XPATH, "//*[name()='rect']").get_attribute("x")

    #countryInfo = driver.find_element(By.XPATH, "//*[name()='svg']//*[@id='GERMANY']//*[name()='rect']").get_attribute("x")
    #countryInfo = driver.find_element(By.ID, "rect12_2_")
    #print(driver.find_element(By.XPATH,"//g[contains(@id,'"+(refinedCurrentQuestion.upper())+"']").get_attribute("data-qText"))
    countryInfo = driver.find_element(By.XPATH,"//*[@data-qText='"+currentQuestion+"']").click()
    #areaCountry = "AREA_"+str(refinedCurrentQuestion).upper()
    #countryInfo = driver.find_element(By.ID, areaCountry).click()

#pyautogui.moveTo(countryInfo.rect['x'],countryInfo.rect['y'],1)
time.sleep(100)
driver.quit()
# https://online.seterra.com/en/vgp/3007

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
