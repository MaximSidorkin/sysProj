import unittest

global str

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

dev = 'https://dev.eor.gosapi.ru/'

driver = webdriver.Firefox()
driver.get(dev)
driver.maximize_window()
wait = WebDriverWait(driver, 20)
driver.implicitly_wait(20)

class ASeleniumAutoTest_1(unittest.TestCase):
    def test001_CreatedInEORDev(self):
        assert "Login" in driver.title
        try:
            assert 'ЭОР - Error' not in driver.title
            print('\n 1. Нет ошибок при вводе логина')
        except:
            print('ошибка 500!')
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)

