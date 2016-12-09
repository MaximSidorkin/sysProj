# не очень понимаю, что этот тест вообще делает, но удалять его я конечно же не буду
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
driver.get("http://dev.eor.gosapi.ru/")
driver.maximize_window()
wait = WebDriverWait(driver, 20)

class ASeleniumAutoTest_1(unittest.TestCase):
    def test_001CreatedInEORDev(self):
        assert "Login" in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        driver.save_screenshot('LoginPassPage.png')
        elem.send_keys(Keys.RETURN)

    def test_002Not500or404andLoginIsVisible(self):
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))

    def test_003Question(self):
        driver.find_element_by_css_selector("i.entypo-menu").click()
        time.sleep(2)
        driver.find_element_by_link_text("Вопросы/Приоритеты").click()
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'navbar-header')))

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumAutoTest_1))
    # File
    buf = open("at_for_undefined_test.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=buf,
        title='НЕ ВЫГРУЖАЕМЫЙ ТЕСТ. ЗНАЧЕНИЯ НЕ ИМЕЕТ',
        description=' \n '
    )
    runner.run(suite)