# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 12:39:31 2022

@author: a_esfahani
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from time import sleep
# import unittest
# import HTMLTestRunner

ser = Service(r"chromedriver.exe")
driver = webdriver.Chrome(service=ser)

# Open Namava
driver.get("https://www.namava.ir/")


# Click ورود/ ثبت نام
driver.find_element(By.LINK_TEXT,"ورود/ ثبت نام").click()
sleep(10)

# Click ثبت نام
driver.find_element(By.LINK_TEXT,"ثبت نام").click()
sleep(4)

# Page:register with phone number
inputPhoneNumberList = [1, 8799, 9877698756897695, 9981511810]

# False input
for i in range(len(inputPhoneNumberList)):
    phoneNumber = driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div[1]/div[2]/div/div/input")
    phoneNumber.send_keys(inputPhoneNumberList[i])
    sleep(3)
    # Click ثبت نام
    driver.find_element(By.ID,"register-phone-request").click()
    sleep(3)
    
    # Check if number is true exit from loop
    if inputPhoneNumberList[i] == 9981511810:        
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "register-phone-verify")))
        break
    
    # Click اصلاح شماره
    driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div[4]/div[3]/div[3]/div[3]").click()
    sleep(3)

    phoneNumber.clear()
    sleep(2)
    
    
    
# # True input
# driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div[1]/div[2]/div/div/input").send_keys("09981511810")
# sleep(3)
# # Click register button
# driver.find_element(By.ID,"register-phone-request").click() 
# sleep(3)

# # Click register button without any code
# driver.find_element(By.ID,"register-phone-verify").click() 
# sleep(3)


# # Click register button with wrong code
# for k in range(2):
#     # driver.find_element(By.CLASS_NAME,"t-input-0-1-569").send_keys("123123")
#     driver.find_element(By.CSS_SELECTOR, "input.t-input-0-1-553").send_keys("123123")
#     driver.find_element(By.ID,"register-phone-verify").click() 
#     sleep(3)
#     # Check 429 Error
# driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div[4]/div[3]/div[4]").click()
# sleep(3)


# # Check 429 Error
# for j in range (2):
#     driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div[2]/div[1]/span").click()
#     sleep(3)

    

# wait for user enter the code sent ********
print("Enter the code sent:")
wait = WebDriverWait(driver, 60)
wait.until(EC.presence_of_element_located((By.ID, "register-phone-finalize")))
# sleep(20)

# Register Phone Finalize page ???????
nameList = ["tt", "testtesttesttesttesttesttesttesttesttesttesttesttest"]
familyList = ["tt", "testtesttesttesttesttesttesttesttesttesttesttesttest"]
passwordList = ["a123"]
repeatPasswordList = ["a123"]

for g in range(len(nameList)):
    name = driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div[1]/div/div/input").send_keys(nameList[g])
    sleep(3)

    family = driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div[2]/div/div/input").send_keys(familyList[g])
    sleep(3)

    password = driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div[3]/div/div/input").send_keys("a123")
    sleep(3)

    repeatPassword = driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div[4]/div/div/input").send_keys("a123")
    sleep(3)

    driver.find_element(By.ID,"register-phone-finalize").click()
    sleep(5)


    
    # # clear All
    # name.clear()
    # family.clear()
    # password.clear()
    # repeatPassword.clear()
    # sleep(5)

    
    
# driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div[1]/div/div/input").clear().send_keys("test test test test test test test test test test test test test test")
# sleep(3)

# driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div[2]/div/div/input").clear().send_keys("test test test test test test test")
# sleep(3)

# driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div[3]/div/div/input").clear().send_keys("a123")
# sleep(3)

# driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div[4]/div/div/input").clear().send_keys("a123")
# sleep(3)

# driver.find_element(By.ID,"register-phone-finalize").click()
# sleep(5)

sleep(4)
print("\nEnd")
# driver.quit()
# if __name__ == '__main__':
#     HTMLTestRunner.main()
