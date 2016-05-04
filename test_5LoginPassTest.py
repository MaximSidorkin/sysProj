import time
import unittest
global str

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("http://test.eor.gosapi.ru/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

class ASeleniumLogin(unittest.TestCase):
    def test_1Login(self):
        assert "Login" in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.click()
        elem = driver.find_element_by_id("LoginForm_password")
        elem.click()
        elem.send_keys(Keys.RETURN)

        if __name__ == '__main__':
            unittest.main()

    def test_2NoSendLogPass(self):
        assert "Login" in driver.title
        ErrTextLogin = driver.find_element_by_id('LoginForm_username_em_').text == 'Логин'
        ErrTextPassw = driver.find_element_by_id('LoginForm_password_em_').text == 'Пароль'
        time.sleep(4)

        if __name__ == '__main__':
            unittest.main()

    def test_3SendIncorrectLogPass(self):
        assert "Login" in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys('123')
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys('123')
        elem.send_keys(Keys.RETURN)
        time.sleep(3)
        ErrMsg = driver.find_element_by_id('LoginForm_password_em_').text == 'Неправильно указан логин или пароль'

        if __name__ == '__main__':
            unittest.main()