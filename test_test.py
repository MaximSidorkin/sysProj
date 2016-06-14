import unittest, inspect, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium import selenium
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)

class PythonOrgSearch(unittest.TestCase):
    def test_2 (self):

        driver.get('http://dev.eor.gosapi.ru/')
        #driver.maximize_window()

    def test_10 (self):
        assert "Login" in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)

