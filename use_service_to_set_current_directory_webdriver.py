# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 10:41:34 2022

@author: pc2
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.chrome.service import Service


# driver must quit because Service wont close webdriver.******
ser = Service(r"chromedriver.exe")
driver = webdriver.Chrome(service=ser)

# Open Namava
driver.get("https://www.namava.ir/")

# Click ورود/ ثبت نام
driver.find_element(By.LINK_TEXT,"ورود/ ثبت نام").click()
sleep(10)

driver.quit()