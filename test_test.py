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

#driver = webdriver.Firefox()
#wait = WebDriverWait(driver, 40)

# ПРОВЕРКА НАЛИЧИЯ МОДАЛЬНЫХ ОКОН
import time
import unittest
import HTMLTestRunner
import sys
#global str

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("https://dev.eor.gosapi.ru/new/")
driver.maximize_window()
wait = WebDriverWait(driver, 40)
body = driver.find_element_by_tag_name('body')

class ASeleniumLogin_1(unittest.TestCase):
    def test_001_LoginInEORDev(self):
        assert "Login" in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)
        print('\n 1. Логинимся в систему\n')

    def test_002_Not500or404andLoginIsVisible(self):
        time.sleep(3)
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        print(' 2. Логин пользователя отображается\n')

    def test_003_CreateCPfromDT(self):
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        assert "ЭОР" in driver.title
        menu = driver.find_element_by_css_selector("i.entypo-menu")
        menu.click()
        time.sleep(4)
        allpj = driver.find_element_by_link_text("Все проекты")
        allpj.click()
        print('\n 3. Переходим в раздел "Все проекты"')

        time.sleep(4)

        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        time.sleep(3)
        searchButton = driver.find_element_by_id('search-show').click()
        time.sleep(2)
        textFild = driver.find_element_by_id('search-text')
        textFild.send_keys('Selenium')
        textFild.send_keys(Keys.ENTER)
        time.sleep(4)


if __name__ == '__main__':
    unittest.main()