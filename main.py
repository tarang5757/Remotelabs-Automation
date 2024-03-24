#import librararies
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import tkinter 

def Automation(username, password):

        

    #execute the chrome driver application.
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    driver.maximize_window()

    

    driver.get("https://remotelab.eecs.yorku.ca/#/")

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )




    #user input
    userinput_element = driver.find_element(By.NAME, "username")
    userinput_element.send_keys(username);

    #password
    userinput_element = driver.find_element(By.NAME, "password")
    userinput_element.send_keys(password);


    #click login
    Login = driver.find_element(By.CLASS_NAME, "login")
    Login.send_keys(Keys.ENTER)

    #find the element to click on.
    WebDriverWait.find_element(By.PARTIAL_LINK_TEXT, "Remote Desktop")


    link = driver.find_element(By.PARTIAL_LINK_TEXT, "Remote Desktop (red1)")
    link.click()

    print("reached end")
    input("Press Enter to close...")  # Wait for user input to keep the console.

