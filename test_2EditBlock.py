import time
import unittest
import HTMLTestRunner, sys
import datetime

global str

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver.get("https://dev.eor.gosapi.ru/new")
driver.maximize_window()
wait = WebDriverWait(driver, 40)
test_time = datetime.datetime.now()
test_day = test_time.day
test_month = test_time.month

class ASeleniumAutoTest_1(unittest.TestCase):
    def test_001_CreatedInEORDev(self):
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        assert "Login" in driver.title
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)
        print('\n 1. Логинимся в ЭОР')

        print('ДАТА ТЕСТА: ',test_day,'/',test_month)

    def test_002_Not500or404andLoginIsVisible(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        print('\n 2. Проверяем наличие ошибок 500/404 на странице')

    def test_003_OpenAllPjct(self):
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        assert "ЭОР" in driver.title
        menu = driver.find_element_by_css_selector("i.entypo-menu")
        menu.click()
        time.sleep(4)
        allpj = driver.find_element_by_link_text("Все проекты")
        allpj.click()
        print('\n 3. Переходим в раздел "Все проекты"')

    def test_004_Not500or404(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        print('\n 4. Проверяем наличие ошибок 500/404 на странице')

    def test_005_CreateNewBlock(self):
        time.sleep(5)
        _ = wait.until(EC.element_to_be_clickable((By.ID,'create-cp')))
        time.sleep(2)
        btn1 = driver.find_element_by_id("create-cp")
        btn1.click()
        time.sleep(5)
        _ = driver.find_element_by_class_name('warn-cp')
        btn2 = driver.find_element_by_name("yt0")
        btn2.click()
        time.sleep(3)
        try:
            if driver.find_element_by_id('Checkpoint_TITLE_em_'):
                print("ok")
        except:
            print('fall')
        time.sleep(3)
        _ = driver.find_element_by_id('Checkpoint_TITLE_em_')

        print('\n 5. Нажимаем кнопку "создать" не заполняя обязательные поля \nПроверяем наличие предупреждающих сообщений')

    def test_006_CreateNewBlockRight(self):
        wait.until(EC.element_to_be_clickable((By.ID, 'Checkpoint_TITLE')))
        elemTitle = driver.find_element_by_id("Checkpoint_TITLE")
        elemTitle.send_keys('Создал Selenium _для редактирования ',test_day,'/',test_month)
        btn2 = driver.find_element_by_name("yt0")
        btn2.click()
        driver.save_screenshot('CreateNewBlock.png')
        print('\n 6. Заполняем обязательные поля и нажимаем создать')

    # находим только что созданный блок
    def test_007_FindBlock(self):
        time.sleep(4)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        time.sleep(3)
        driver.find_element_by_id('search-show').click()
        time.sleep(2)
        textFild = driver.find_element_by_id('search-text')
        textFild.send_keys('Создал Selenium _для редактирования ',test_day,'/',test_month)
        textFild.send_keys(Keys.ENTER)
        print('\n 7. Находим только что созданный блок')

    # редактируем блок
    def test_008_EditBlock(self):
        time.sleep(5)
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[2]/div[2]/div/table/tbody/tr/td[2]/button[1]')))
        editButton = driver.find_element_by_xpath('//div[2]/div[2]/div/table/tbody/tr/td[2]/button[1]')
        editButton.click()
        time.sleep(6)
        NewTitle = driver.find_element_by_id('Checkpoint_TITLE')
        NewTitle.send_keys(' edit ')
        plus = driver.find_element_by_css_selector('i.fa.fa-plus')
        plus.click()
        time.sleep(2)
        newCat = driver.find_element_by_id('Category_S_NAME')
        newCat.send_keys('1')
        catOk = driver.find_element_by_id('catOk')
        catOk.click()

        time.sleep(1)
        plus = driver.find_element_by_css_selector('i.fa.fa-plus')
        plus.click()
        time.sleep(2)
        newCat2 = driver.find_element_by_id('Category_S_NAME')
        newCat2.send_keys('2')
        time.sleep(5)
        #driver.implicitly_wait(10)
        catOk2 = driver.find_element_by_id('catOk')
        catOk2.click()
        time.sleep(3)
        driver.save_screenshot('EditBlock.png')
        print('\n 8. Редактируем блок меняя название, добавляя категории')

    def test_009_NegativEditBlock(self):
        plus = driver.find_element_by_css_selector('i.fa.fa-plus')
        plus.click()
        time.sleep(5)
        #driver.implicitly_wait(10)
        catOk = driver.find_element_by_id('catOk')
        catOk.click()
        negativMsg = driver.find_element_by_id('result').text == 'Не удалось сохранить категорию'
        time.sleep(2)
        driver.save_screenshot('C:\Program Files (x86)\Jenkins\jobs\Создание Блока\workspace\errorMsg.jpg')
        catCancel = driver.find_element_by_id('catCancel')
        catCancel.click()
        print('\n 9. Проверяем невозможность создания категории без имени')

    def test_010_SeveAndDelBlock(self):
        driver.find_element_by_name('yt0').click()
        time.sleep(2)
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, '//td[2]/button[2]')))
        driver.find_element_by_xpath('//td[2]/button[2]').click()
        driver.find_element_by_xpath("//div[3]/div/button").click()
        time.sleep(2)
        driver.close()
        print('\n 10. Удаляем только что созданный блок')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumAutoTest_1))

    buf = open("at_for_BLOCK.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=buf,
        title='ПРОВЕРКА СОЗДАНИЯ СОЗДАНИЯ/РЕДАКТИРВОАНИЯ/УДАЛЕНИЯ БЛОКА',
        description='Отчет по тестированию'
    )
    ret = not runner.run(suite).wasSuccessful()
    sys.exit(ret)