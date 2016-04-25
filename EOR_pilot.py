import time
import unittest
global str

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("http://dev.eor.gosapi.ru/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

class ASeleniumAutoTest_1(unittest.TestCase):
    def test_1CreatedInEORDev(self):
        assert "Login" in driver.title
        #wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)
    def test_2Not500or404andLoginIsVisible(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))

        if __name__ == '__main__':
            unittest.main()

class BSeleniumOpenAllPjct_2(unittest.TestCase):
    def test_1OpenAllPjct(self):
        wait = WebDriverWait(driver, 10)
        #time.sleep(3)
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        assert "ЭОР" in driver.title
        menu = driver.find_element_by_css_selector("i.entypo-menu")
        menu.click()
        time.sleep(4)
        allpj = driver.find_element_by_link_text("Все проекты")
        allpj.click()
    def test_2Not500or404(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        if __name__ == '__main__':
            unittest.main()

class CSeleniumCreateNewBlock_3(unittest.TestCase):
    def test_1CreateNewBlock(self):
        time.sleep(3)
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.ID,'create-cp')))
        btn1 = driver.find_element_by_id("create-cp")
        btn1.click()
        time.sleep(4)
        _ = driver.find_element_by_class_name('warn-cp')    #есть текст "Вы собираетесь создать блок."
        elemTitle = wait.until(EC.element_to_be_clickable((By.ID,'Checkpoint_TITLE')))
        elemTitle = driver.find_element_by_id("Checkpoint_TITLE")
        elemTitle.send_keys("Создал Selenium")
    def test_2Not500or404(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        if __name__ == '__main__':
            unittest.main()

class DSeleniumTestConfirm_4(unittest.TestCase):
    def test_1Confirm(self):
        wait = WebDriverWait(driver, 10)
        btn2 = driver.find_element_by_name("yt0")
        btn2.click()
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        _ = driver.find_element_by_id("create-cp")
    def test_2Not500or404(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        if __name__ == '__main__':
            unittest.main()

class ESeleniumTestDelBlock_5(unittest.TestCase):
    def test_1DelBlock(self):
        time.sleep(5)
        wait = WebDriverWait(driver, 10)
        assert "ЭОР" in driver.title
        elem = driver.find_element_by_link_text('Поиск')
        elem.click()
        time.sleep(2)
        elemSearch = driver.find_element_by_id('search-text')
        elemSearch.click()
        elemSearch.send_keys('Создал Selenium')
        elemSearch.send_keys(Keys.ENTER)
        #добавить проверку "нашел или не нашёл"
    def test_2SearchNewBlock(self):
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        time.sleep(2)
        BoxElem = driver.find_element_by_xpath("//tbody/tr[1]/td[2]/button[2]")
        BoxElem.click()
        elemYes = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/button[1]")
        elemYes.click()
        time.sleep(3)
        #добавить проверку "удалил или не удалил"
    def test_3ConfirmDeleteBlock(self):
        elemSearch = driver.find_element_by_id("search-text-push")
        elemSearch.click()
        time.sleep(3)
        _ = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[4]/div[2]/div[2]/div/table/tbody/tr/td/div").text == "Ничего не найдено"
    def test_4Not500or404(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        if __name__ == '__main__':
            unittest.main()



