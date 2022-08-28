# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 09:45:43 2022

@author: pc2
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 22:56:00 2022

@author: pc2
"""

import unittest
import HTMLTestRunner
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



from time import sleep

ser = Service(r"chromedriver.exe")
driver = webdriver.Chrome(service=ser)

class testadd(unittest.TestCase):
    def setUp(self):        
        pass
    def test_add1(self):
        self.assertEqual(2 + 3 + 10,15)
    def test_add2(self):
        self.assertEqual(10 + 150,160)
    def test_add3(self):
        #One error, view test results
        self.assertEqual(2 * 5 * 7, 40)
         #Baidu search use cases 
    def test_namava1(self):
        # self.ser = Service(r"chromedriver.exe")
        # self.driver = webdriver.Chrome(service=self.ser)
        self.base_url = "https://www.namava.ir/"
        self.verificationErrors = []
        self.accept_next_alert = True
        # driver = self.driver
        driver.get(self.base_url)
        
        driver.find_element(By.LINK_TEXT,"ورود/ ثبت نام").click()
        sleep(10)

        # Click ثبت نام
        driver.find_element(By.LINK_TEXT,"ثبت نام").click()
        sleep(4)

        # driver.quit()

        
    def test_namava2(self):
        # ser = Service(r"chromedriver.exe")
        # driver = webdriver.Chrome(service=ser)
        # self.base_url = "https://www.namava.ir/"
        # self.verificationErrors = []
        # self.accept_next_alert = True
        # # driver = self.driver
        # driver.get(self.base_url)


        # # Click ورود/ ثبت نام
        # driver.find_element(By.LINK_TEXT,"ورود/ ثبت نام").click()
        # sleep(10)

        # # Click ثبت نام
        # driver.find_element(By.LINK_TEXT,"ثبت نام").click()
        # sleep(4)

        # Page:register with phone number
        inputPhoneNumberList = [1, 8799, 9877698756897695, 9981511810]

        # False input
        for i in range(len(inputPhoneNumberList)):
            phoneNumber = driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div[1]/div[2]/div/div/input")
            phoneNumber.send_keys(inputPhoneNumberList[i])
            sleep(2)
            # Click ثبت نام
            driver.find_element(By.ID,"register-phone-request").click()
            sleep(2)
    
            # Check if number is true exit from loop
            if inputPhoneNumberList[i] == 9981511810:        
                wait = WebDriverWait(driver, 10)
                wait.until(EC.presence_of_element_located((By.ID, "register-phone-verify")))
                break
    
            # Click اصلاح شماره
            driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div[4]/div[3]/div[3]/div[3]").click()
            sleep(2)

            phoneNumber.clear()
            sleep(2)
    

        # driver.quit()

    def test_namava3(self):
        # Resend Code to mobile
        sleep(2)
        driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[2]/div[2]/div[1]").click()

        # wait for user enter the code sent ********
        print("Enter the code sent:")
        wait = WebDriverWait(driver, 60)
        wait.until(EC.presence_of_element_located((By.ID, "register-phone-finalize")))

    def test_namava4(self):
        # Register Phone Finalize page ???????
        nameList = ["tt", "testtesttesttesttesttesttesttesttesttesttesttesttest"]
        familyList = ["tt", "testtesttesttesttesttesttesttesttesttesttesttesttest"]
        passwordList = ["a123"]
        repeatPasswordList = ["a123"]

        for g in range(len(nameList)):
            name = driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div[1]/div/div/input").send_keys(nameList[g])
            sleep(2)

            family = driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div[2]/div/div/input").send_keys(familyList[g])
            sleep(2)

            password = driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div[3]/div/div/input").send_keys("a123")
            sleep(2)

            repeatPassword = driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div[4]/div/div/input").send_keys("a123")
            sleep(7)

            driver.find_element(By.ID,"register-phone-finalize").click()
            sleep(5)
        
    def tearDown(self):
        pass
def suite():
    test_suite=unittest.TestSuite()
    test_suite.addTest(testadd("test_add1"))
    test_suite.addTest(testadd("test_add2"))
    test_suite.addTest(testadd("test_add3"))
    test_suite.addTest(testadd("test_namava1"))
    test_suite.addTest(testadd("test_namava2"))
    test_suite.addTest(testadd("test_namava3"))
    test_suite.addTest(testadd("test_namava4"))
    return test_suite

if __name__=="__main__":
   # Store path in C Disk directory
   filepath='C:\\Users\\pc2\\Documents\\py3\\testNewHTMLReport\\pyresult.html'
   fp=open(filepath,'wb')
   #Define the title and description of the test report
   runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'Shatel/Namava',description=u'I am the wind complaining about the test report description of Jiangnan')
   runner.run(suite())
   fp.close()