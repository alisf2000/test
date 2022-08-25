# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 08:47:27 2022

@author: pc2
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import unittest

driver = webdriver.Chrome(executable_path=r"E:\chrome driver\New folder\chromedriver.exe")

# Open Namava
driver.get("https://www.namava.ir/")


try:
    n = 1
  # 1
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,"//*[@id='profile-login']/div/span")))
    # print(n)
    n += 1
        
  # 2
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT,"ورود/ ثبت نام")))
    # print(n)
    n += 1
    
  # 3
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,"//*[@id='105412']")))
    # print(n)
    n += 1
    
  # 4
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,"//*[@id='profile-plans']/div/span")))
    # print(n)
    n += 1
    
    not_found = True
    print("PASS ALL")
except:
    not_found = False

assert not_found , "khata dar shomare: " + str(n)

sleep(4)
# print("\nEnd")
driver.quit()