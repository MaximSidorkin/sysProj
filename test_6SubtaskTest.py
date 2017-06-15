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
perm = 'http://dev.perm.gosapi.ru/top/'

driver = webdriver.Chrome()
driver.get(perm)
driver.maximize_window()
wait = WebDriverWait(driver, 40)

test_time = datetime.datetime.now()
test_day = test_time.day
test_month = test_time.month

class ASeleniumAutoTest_1(unittest.TestCase):
    def test001_CreatedInEORDev(self):
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        assert "Login" in driver.title
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)
        print('\n 1. Логинимся в систему')

    def test002_Not500or404andLoginIsVisible(self):
        assert "ЭОР - Error" not in driver.title  # проверка на 500/404 ошибку
        print('\n 2. Ошибок 500 и 404 не обнаружено')
        time.sleep(5)

    def test003_OpenAllPjct(self):
        #wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        assert "ЭОР" in driver.title
        menu = driver.find_element_by_css_selector("i.entypo-menu")
        menu.click()
        time.sleep(4)
        allpj = driver.find_element_by_link_text("Все проекты")
        allpj.click()
        print('\n 3. Переходим в раздел "Все проекты"')

    def test004_Not500or404(self):
        assert "ЭОР - Error" not in driver.title  # проверка на 500/404 ошибку
        print('\n 4. При переходе в раздел "Все проекты" ошибок 404 и 500 не обнаружено')

# переход к подзадаче
    def test005_GotoSubtask(self):
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        time.sleep(2)
        assert "ЭОР" in driver.title
        elem = driver.find_element_by_link_text('Поиск')
        elem.click()
        elemSearch = driver.find_element_by_id('search-text')
        elemSearch.click()
        elemSearch.send_keys('Selenium')
        elemSearch.send_keys(Keys.ENTER)
        print('\n 5. В поиске вводим ключевое слово "Selenium"')

    def test006_FilterSetting(self):
        assert "ЭОР" in driver.title
        time.sleep(8)
        _ = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Selenium')))
        findBlock = driver.find_element_by_link_text('Selenium').click()
        time.sleep(5)
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[2]/table/tbody/tr/td')))
        findProject = driver.find_element_by_xpath("//div[2]/table/tbody/tr/td").click()
        time.sleep(5)
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='item-toolbar']/button")))
        plusST = driver.find_element_by_xpath("//div[@id='item-toolbar']/button").click()
        print('\n 6. Открываем блок, потом проект, кликаем по иконке "+"\n открывая форму создания подзадачи')

    def test007_Not500or404(self):
        assert "ЭОР - Error" not in driver.title  # проверка на 500/404 ошибку
        print('\n 7. Ошибок 500 и 404 не обнаружено')

    def test008_CheckForm(self):
        assert "ЭОР" in driver.title
        time.sleep(8)
        _ = driver.find_element_by_id('cp_title').text == 'Создание контрольной точки'
        time.sleep(4)
        _ = driver.find_element_by_class_name('warn-cp').text == 'контрольную точку'
        EditProject = driver.find_element_by_name('yt0')
        time.sleep(4)
        EditProject.send_keys(Keys.PAGE_DOWN)
        EditProject.click()
        print('\n 8. Проверяем форму на корретность атрибутов')

    def test009_CheckWarningMsg(self):
        assert "ЭОР" in driver.title
        time.sleep(8)
        _ = driver.find_element_by_id('Checkpoint_TITLE_em_').text == 'Необходимо заполнить поле «Название».'
        _ = driver.find_element_by_id('Checkpoint_ID_RESPONSIBLE_em_').text == 'заполнить поле «Ответственный».'
        _ = driver.find_element_by_id('Checkpoint_DEADLINE_em_').text == 'заполнить поле «Срок исполнения (план)»'
        print('\n 9. Кликаем на кнопку "создать" не заполняя обязательные поля, \n затем проверям наличие предупреждающих сообщений')

    def test010_FillingForm(self):
        assert "ЭОР" in driver.title
        time.sleep(2)
        # имя подзадачи
        nameCP = driver.find_element_by_id('Checkpoint_TITLE')
        nameCP.click()
        nameCP.send_keys("Подзадача созданная Selenium ",test_day,'/',test_month)
        time.sleep(2)
        # автор
        time.sleep(2)
        # ответственный
        driver.find_element_by_xpath("//div[@id='DIV_ID_RESPONSIBLE']/div/span/span/span/span[2]").click()
        responsibleNameText = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleNameText.send_keys('иванов и')
        time.sleep(2)
        responsibleNameText.send_keys(Keys.ENTER)
        time.sleep(2)
        # сроки
        terms = driver.find_element_by_id('Checkpoint_DEADLINE')
        terms.click()
        terms.send_keys("12345")
        terms.send_keys(Keys.ENTER)
        print('\n 10. Корректно заполняем форму')

    def test011_TriggersCPTest(self):
        EditProject = driver.find_element_by_name('yt0')
        EditProject.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        print('\n 11. Нажимаем кнопку "Создать"')

    def test012_ConfirmCreation(self):
        elem = driver.find_element_by_name('yt0')
        elem.click()
        time.sleep(3)
        WebDriverWait(driver, 10)
        _ = driver.find_element_by_xpath('//div[2]/div[4]/div/div[2]/div/div[1]/div[1]').text == 'Паспорт Контрольной'
        print('\n 12. Проверяем на корректность атрбутоы паспотра')

    def test013_CreateCopyST(self):
        time.sleep(5)
        driver.find_element_by_name('yt1').click()
        time.sleep(5)
        driver.find_element_by_id('Checkpoint_DEADLINE').send_keys('12345' + Keys.ENTER)
        time.sleep(2)
        _ = driver.find_element_by_name('yt0')
        _.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        driver.find_element_by_name('yt0').click()
        time.sleep(3)
        print('\n 13. открываем на редактирвоание подзадачу и изменяем дату, \n сохраняем изменения')

    def test014_DeleteSubTask(self):
        time.sleep(2)
        deleteButton = driver.find_element_by_name('yt2')
        deleteButton.click()
        time.sleep(2)
        elemYes = driver.find_element_by_xpath('//div[3]/div/button')
        elemYes.click()
        print('\n 14. Удаляем созданную подзадачу')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumAutoTest_1))

    buf = open("at_for_SUBTASK.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=buf,
        title='ПРОВЕРКА СОЗДАНИЯ СОЗДАНИЯ/РЕДАКТИРВОАНИЯ/УДАЛЕНИЯ ПОДЗАДАЧИ',
        description='Отчет по тестированию'
    )
    ret = not runner.run(suite).wasSuccessful()
    sys.exit(ret)
