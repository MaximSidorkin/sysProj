# coding: utf8

import time
import unittest
import HTMLTestRunner, sys

global str

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("https://owa.mos.ru/EWS/Exchange.asmx")
driver.maximize_window()
wait = WebDriverWait(driver, 40)

class A_GetImp(unittest.TestCase):
    def t1_firstStep(self):
        time.sleep(5)
        print('\n\n\n Ok \n\n\n')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(A_GetImp))

    buf = open("at_for_OWA.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=buf,
        title='ПРОВЕРКА OWA',
        description='Отчет по тестированию'
    )
    ret = not runner.run(suite).wasSuccessful()
    sys.exit(ret)