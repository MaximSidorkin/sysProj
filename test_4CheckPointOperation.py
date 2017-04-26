import time, datetime
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
driver.get(pgs)
driver.maximize_window()
wait = WebDriverWait(driver, 40)

test_time = datetime.datetime.now()
test_day = test_time.day
test_month = test_time.month

class ASeleniumLogin_1(unittest.TestCase):
    def test001_LoginInEORDev(self):
        wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        assert "Login" in driver.title
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("admin")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("adminpass")
        elem.send_keys(Keys.RETURN)

        print('\n 1. Логинимся в ЭОР')

    def test002_Not500or404andLoginIsVisible(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        time.sleep(4)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))

        print('\n 2. Ждем пока страница загрузится проверяем на 500/404')

    def test003_OpenAllPjct(self):
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        assert "ЭОР" in driver.title
        driver.find_element_by_css_selector("i.entypo-menu").click()    # menu click
        time.sleep(2)
        driver.find_element_by_link_text("Все проекты").click()         # all project click

        print('\n 3. переходим в раздел все проекты')

    def test004_Not500or404(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        print('\n 4. Подтверждаем, что страница успешно загрузилась')

    def test005_OpenForm(self):
        wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        time.sleep(2)
        assert "ЭОР" in driver.title
        driver.find_element_by_link_text('Поиск').click()           # search click
        elemSearch = driver.find_element_by_id('search-text')
        elemSearch.click()
        elemSearch.send_keys('Selenium')
        elemSearch.send_keys(Keys.ENTER)
        time.sleep(3)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        print('\n 5. В поиске по ключевому слову selenium находим блок')

    def test006_FindBlock(self):
        #находим блок
        driver.find_element_by_link_text('Selenium').click()
        time.sleep(3)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        print('\n 6. Переходим от блока к проекту')

    def test007_FindProject(self):
        #находим проект
        driver.find_element_by_xpath('//div[2]/div[2]/table/tbody/tr/td[1]/h4/strong/a/span').click()
        time.sleep(2)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        print('\n 7. переходим от проекта к контрольным точкам')

    def test008_CreateCP(self):
        #создаем контрольную точку
        driver.find_element_by_id('create-cp').click()
        time.sleep(1)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        print('\n 8. нажимаем кнопку "Создать"')

    def test009_FillingCPForm(self):
        time.sleep(3)
        wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        _ = driver.find_element_by_class_name('warn-cp').text == 'контрольную точку'  # test
        time.sleep(2)
        #имя контрольной точки
        driver.find_element_by_id('Checkpoint_TITLE').send_keys("контрольная точка созданная Selenium ",test_day,'/',test_month)
        #автор
        #driver.implicitly_wait(10)
        time.sleep(2)
        #ответственный
        #driver.implicitly_wait(10)
        driver.find_element_by_xpath("//div[@id='DIV_ID_RESPONSIBLE']/div/span/span/span/span[2]").click()
        time.sleep(2)
        driver.find_element_by_xpath('html/body/span/span/span[1]/input').send_keys('яadmin' + Keys.ENTER)
        time.sleep(2)
        #driver.implicitly_wait(10)
        #сроки
        driver.find_element_by_id('Checkpoint_DEADLINE').send_keys('12345' + Keys.ENTER)    # deadline date
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        print('\n 8. Заполняем форму контрольной точки')

    def test009_TriggersCPTest(self):
        driver.find_element_by_name('yt0').send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        print('\n 9. Находим кнопку "Сохранить"')

    def test010_ConfirmCPCreating(self):
        driver.find_element_by_name('yt0').click()
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        time.sleep(3)

        print('\n 10. Сохраняем новую контрольную точку')

    def test011_ClickEditButton(self):
        #driver.implicitly_wait(20)
        time.sleep(3)
        driver.find_element_by_name('yt0').click()
        time.sleep(2)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        time.sleep(3)

        print('\n 11. Нажимаем кнопку "редактировать" на паспорте контрольной точки')

    def test012_editCP(self):
        #driver.implicitly_wait(20)
        time.sleep(3)
        driver.find_element_by_id('Checkpoint_TITLE').send_keys(' редактировано ') #.click()
        driver.find_element_by_name('yt0').send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        driver.find_element_by_name('yt0').click()
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        print('\n 12. вносим изменения в контрольную точку и сохраняем')

    def test013_AllRight(self):
        time.sleep(4)
        #driver.implicitly_wait(20)
        _ = driver.find_element_by_id('C_TITLE').text == ' редактировано '
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        print('\n 13. Подтверждаем, что изменения отображаются в \n паспорте контрольной точки')

    def test014_CreateCopyCP(self):
        time.sleep(3)
        assert "ЭОР" in driver.title
        driver.find_element_by_name('yt1').click()
        time.sleep(3)
        driver.find_element_by_id('Checkpoint_DEADLINE').send_keys('12345' + Keys.ENTER)
        time.sleep(1)
        _ = driver.find_element_by_name('yt0')
        _.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        driver.find_element_by_name('yt0').click()
        time.sleep(3)

        print('\n 14. Создаём копию контрольной точки')

    def test015_DelCP(self):
        driver.find_element_by_name('yt2').click()
        time.sleep(1)
        driver.find_element_by_xpath('//div[3]/div/button').click()
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        print('\n 15. Удаляем контрольную точку')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumLogin_1))

    buf = open("at_for_CHECKPOINT.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=buf,
        title='ПРОВЕРКА СОЗДАНИЯ СОЗДАНИЯ/РЕДАКТИРВОАНИЯ/УДАЛЕНИЯ КОНТРОЛЬНОЙ ТОЧКИ',
        description='Отчет по тестированию'
    )
    ret = not runner.run(suite).wasSuccessful()
    sys.exit(ret)