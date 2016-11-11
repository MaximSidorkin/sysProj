import time
import unittest
import HTMLTestRunner

global str

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("https://dev.eor.gosapi.ru/")
driver.maximize_window()
wait = WebDriverWait(driver, 20)

class ASeleniumLogin(unittest.TestCase):
    def test_1Login(self):
        assert "Login" in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.click()
        elem = driver.find_element_by_id("LoginForm_password")
        elem.click()
        elem.send_keys(Keys.RETURN)
        print('\n 1. Логин и пароль пользователя не введен')

    def test_2NoSendLogPass(self):
        assert "Login" in driver.title
        try:
            ErrTextLogin = driver.find_element_by_id('LoginForm_username_em_').text == 'Логин'
            ErrTextPassw = driver.find_element_by_id('LoginForm_password_em_').text == 'Пароль'
            time.sleep(4)
            print('\n 2. Выведено сообщение об ошибке')
        except:
            print('\n 2. ОШИБКА! сообщение о незаполненных полях не выведено')

    def test_3SendIncorrectLogPass(self):
        assert "Login" in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys('123')
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys('123')
        elem.send_keys(Keys.RETURN)
        time.sleep(7)
        try:
            ErrMsg = driver.find_element_by_id('LoginForm_password_em_')
            print('\n 3. Введены не корректные логин и пароль - выведено сообщение об ошибке')
        except:
            print('\n 3. ОШИБКА! сообщение о некорректном логине/пароле не выведено')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumLogin))
    # File
    buf = open("at_for_login_pass_test.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=buf,
        title='ПРОВЕРКА КОРРЕКТНОСТИ ВВОДА ЛОГИНА И ПАРОЛЯ',
        description='Отчет по тестированию'
    )
    runner.run(suite)