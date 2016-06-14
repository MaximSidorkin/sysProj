import time
import unittest
global str

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("http://dev.eor.gosapi.ru/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

class ASeleniumAutoTest_1(unittest.TestCase):
    def test_001CreatedInEORDev(self):
        assert "Login" in driver.title
        #wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        driver.save_screenshot('LoginPassPage.png')
        elem.send_keys(Keys.RETURN)
    def test_002Not500or404andLoginIsVisible(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
    '''
    def test_003OpenAllPjct(self):
        wait = WebDriverWait(driver, 10)
        #time.sleep(3)
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        assert "ЭОР" in driver.title
        menu = driver.find_element_by_css_selector("i.entypo-menu").click()
        time.sleep(2)
        allpj = driver.find_element_by_link_text("Все проекты").click()
    def test_004Not500or404(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
    '''
    def test_003Question(self):
        menu = driver.find_element_by_css_selector("i.entypo-menu").click()
        time.sleep(2)
        question = driver.find_element_by_link_text("Вопросы/Приоритеты").click()
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'navbar-header')))