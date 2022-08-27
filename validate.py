# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 14:51:51 2022

@author: a_esfahani
"""

import unittest
from unittest.suite import TestSuite
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# first test class
class TestBing(unittest.TestCase):

    def setUp(self):
        self.ser = Service(r"chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.ser)

    def test_open_bing1(self):
        self.driver.get("https://bing.com")

# second test class
class TestCherCherTech(unittest.TestCase):

    def setUp(self):
        self.ser = Service(r"chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.ser)

    def test_open_bing2(self):
        self.driver.get("https://chercher.tech")
        
    def test_open_bing3(self):
        self.driver.get("https://google.com")        
    
    def test_open_bing4(self):
        self.driver.get("https://che")

if __name__ == "__main__":

	# create the suite from the test classes
    suite = TestSuite()
    # load the tests
    tests = unittest.TestLoader()

	# add the tests to the suite
    suite.addTests(tests.loadTestsFromTestCase(TestBing))
    suite.addTests(tests.loadTestsFromTestCase(TestCherCherTech))

    # run the suite
    runner = unittest.TextTestRunner()
    runner.run(suite)