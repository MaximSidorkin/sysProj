import time
import unittest
import HTMLTestRunner, sys
import datetime

global str
import page_objects

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

oracle = 'https://task.eor.gosapi.ru/oracle/site/login'
pgs = 'https://task.eor.gosapi.ru/pgs/site/login'
dev = 'https://dev.eor.gosapi.ru/new/site/login'
perm = 'http://dev.perm.gosapi.ru/top/'

driver = webdriver.Chrome()
driver.get(pgs)
driver.maximize_window()
wait = WebDriverWait(driver, 40)

test_time = datetime.datetime.now()
test_day = test_time.day
test_month = test_time.month


class ASeleniumLogin_1(unittest.TestCase):
    def test_001_LoginInEORDev(self):
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        assert "Login" in driver.title
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)
        print('\n 1. Логинимся в ЭОР')

    def test_002_Not500or404andLoginIsVisible(self):
        assert "ЭОР - Error" not in driver.title  # проверка на 500/404 ошибку
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        print('\n 2. Ждем пока страница рабочего стола загрузится \n проверяем на 500/404 проекта')

    def test_003_OpenAllPjct(self):
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        time.sleep(3)
        assert "ЭОР" in driver.title
        menu = driver.find_element_by_css_selector("i.entypo-menu")
        menu.click()
        time.sleep(2)
        allpj = driver.find_element_by_link_text("Все проекты")
        allpj.click()
        print('\n 3. Переходим в раздел все проекты')

    def test_004_Not500or404(self):
        assert "ЭОР - Error" not in driver.title  # проверка на 500/404 ошибку
        print('\n 4. Ошибок 400/500 не обнаружено')

    def test_005_OpenForm(self):
        time.sleep(4)
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        time.sleep(3)
        searchButton = driver.find_element_by_id('search-show').click()
        time.sleep(2)
        textFild = driver.find_element_by_id('search-text')
        textFild.send_keys('Selenium')
        textFild.send_keys(Keys.ENTER)
        time.sleep(4)
        #driver.find_element_by_xpath("//a[contains(text(),'Selenium')]").click()
        driver.find_element_by_link_text('Selenium').click()
        # new fnc
        time.sleep(5)
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        btn1 = driver.find_element_by_id("create-cp")
        btn1.click()
        time.sleep(10)
        _ = driver.find_element_by_class_name('warn-cp')    #есть текст "Вы собираетесь создать проект."
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, '//div/span/i')))
        print('\n 5. Переходим от блока к проектам и нажимаем кнопку "Создать"')

    def test_006_SearchBlock(self):
        time.sleep(3)
        print('\n 6. Ждем загрузки формы создания проекта')

    def test_007_NewPjctFormBlock(self):
        wait.until(EC.element_to_be_clickable((By.ID, 'btnCloseForm')))      #test
        _ = driver.find_element_by_xpath("//form/div/div[2]/div[1]/div/div[4]/b")
        nameOfpjct = driver.find_element_by_id("Checkpoint_TITLE")#.send_keys("Тестовый проект созданный Selenium")
        nameOfpjct.click()  #test
        nameOfpjct.send_keys("Тестовый проект созданный Selenium ",test_day,'/',test_month)
        time.sleep(2)
        _ = driver.find_element_by_class_name('warn-cp').text == 'проект'   # test
        # руководитель
        autorDown = driver.find_element_by_xpath("//div[@id='DIV_ID_RESPONSIBLE']/div/span/span/span/span").click()
        autorName = driver.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys("Иванов И" + Keys.ENTER)
        # куратор
        pjctMansger = driver.find_element_by_xpath("//div[@id='DIV_PROJECT_CURATOR']/div/span/span/span/span[2]").click()
        pjctMansgerName = driver.find_element_by_xpath("html/body/span/span/span[1]/input").send_keys("Иванов И" + Keys.ENTER)
        print('\n 7. Заполняем форму проекта')

    def test_008_ConfirmCreatingPjct(self):
        time.sleep(2)
        driver.find_element_by_name("yt0").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        CreateButton = driver.find_element_by_name("yt0").click()
        print('\n 8. Сохраняем новый проект')

    def test_009_CheckPage(self):
        # проверить элементы на странице
        time.sleep(5)
        driver.set_page_load_timeout(5)
        _ = WebDriverWait(driver, 50)
        _ = wait.until(EC.element_to_be_clickable((By.NAME, 'yt0')))
        EditProject = driver.find_element_by_name('yt0')
        EditProject.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)
        EditProject.click()
        print('\n 9. Проверяем элементы на странице и нажимаем кнопку редактировать')

    def test_010_editProject(self):
        time.sleep(6)
        ShortName = driver.find_element_by_id("Checkpoint_SHORT_NAME").send_keys("Краткое наименование")
        FullName = driver.find_element_by_id("Checkpoint_TITLE").send_keys(" edit ")
        SaveEdit = driver.find_element_by_name('yt0').click()
        print('\n 10. Редактируем проект и сохраняем его')

    def test_011_AllRight(self):
        time.sleep(4)
        _ = driver.find_element_by_id('C_TITLE').text == ' edit '
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        print('\n 11. Проверяем, отобразились ли в паспорте проекта внесенные изменения')

    def test_012_SeekAndDestroy(self):
       time.sleep(6)
       assert "ЭОР" in driver.title
       driver.find_element_by_id('search-text').clear()
       time.sleep(1)
       driver.find_element_by_id('search-text').send_keys('Тестовый проект созданный Selenium ',test_day,'/',test_month, ' edit ')   #new text for search
       driver.find_element_by_id('search-text-push').click()    # Search click
       time.sleep(6)

       elemTestBlock = driver.find_element_by_xpath('//div[2]/div[2]/div/table/tbody/tr/td[1]/h4')
       elemTestBlock.click()
       time.sleep(4)
       DelProject = driver.find_element_by_xpath('//div[2]/div[2]/div[2]/table/tbody/tr/td[2]/button[2]')
       DelProject.click()
       time.sleep(3)
       elemNo = driver.find_element_by_xpath("//div[3]/div/button[2]")
       elemNo.click()
       DelProject.click()
       time.sleep(4)
       driver.implicitly_wait(10)
       elemYes = driver.find_element_by_xpath('//div[3]/div/button')
       elemYes.click()
       print('\n 12. Заново находим проект и удаляем его \n (проверка кнопок "удалить да/нет", удалить да/да присутствует)')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumLogin_1))

    buf = open("at_for_PROJECT.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=buf,
        title='ПРОВЕРКА СОЗДАНИЯ СОЗДАНИЯ/РЕДАКТИРВОАНИЯ/УДАЛЕНИЯ ПРОЕКТА',
        description='Отчет по тестированию'
    )
    ret = not runner.run(suite).wasSuccessful()
    sys.exit(ret)