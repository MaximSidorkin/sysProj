import time
import unittest
import HTMLTestRunner, sys

global str

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

oracle = 'https://task.eor.gosapi.ru/oracle/site/login'
pgs = 'https://task.eor.gosapi.ru/pgs/site/login'
dev = 'https://dev.eor.gosapi.ru/new/site/login'

driver = webdriver.Chrome()
driver.get(dev)
driver.maximize_window()
wait = WebDriverWait(driver, 40)

class ASeleniumLogin(unittest.TestCase):
    def test_1Login(self):
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        assert "Login" in driver.title
        elem = driver.find_element_by_id("LoginForm_username")
        elem.click()
        elem = driver.find_element_by_id("LoginForm_password")
        elem.click()
        elem.send_keys(Keys.RETURN)
        print('\n 1. Логин и пароль пользователя не введен')

    def test_2NoSendLogPass(self):
        assert "Login" in driver.title
        try:
            time.sleep(2)
            ErrTextLogin = driver.find_element_by_css_selector('div.errorMessage').text == 'Логин'
            ErrTextPassw = driver.find_element_by_xpath('//div[3]/div[2]').text == 'Пароль'
            time.sleep(2)
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
            ErrMsg = driver.find_element_by_css_selector('div.errorMessage')
            print('\n 3. Введены не корректные логин и пароль - выведено сообщение об ошибке')
        except:
            print('\n 3. ОШИБКА! сообщение о некорректном логине/пароле не выведено')

    def test_4LetMeIn(self):
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        driver.find_element_by_id("LoginForm_username").clear()
        driver.find_element_by_id("LoginForm_password").clear()
        time.sleep(1)
        driver.find_element_by_id("LoginForm_username").send_keys('ipad')
        elem = driver.find_element_by_id("LoginForm_password").send_keys('ipad'+Keys.ENTER)
        time.sleep(1)
        try:
            _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
            print('\n 4. Логин и пароль пользователя введен корректно, \nпользователь авторизован, вход в систему осуществлён')
        except:
            self.fail(print('\n\n 4. АВТОРИЗАЦИЯ С ВЕРНЫМИ ДАННЫМИ ПОЛЬЗОВАТЕЛЯ НЕ ПРОШЛА - ОШИБКА!\n\n'))

    def test_5CloseBrowser(self):
        print('\n 5. Тест завершен, браузер закрыт')
        driver.close()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumLogin))

    buf = open("at_for_login_pass_test.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=buf,
        title='ПРОВЕРКА КОРРЕКТНОСТИ ВВОДА ЛОГИНА И ПАРОЛЯ',
        description='Отчет по тестированию'
    )
    ret = not runner.run(suite).wasSuccessful()
    sys.exit(ret)