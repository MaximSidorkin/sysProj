import time
import unittest
global str

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("https://dev.eor.gosapi.ru/site/login")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

class ASeleniumLogin_1(unittest.TestCase):
    def test001_LoginInEORDev(self):
        assert "Login" in driver.title
        #wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)

    def test002_Not500or404andLoginIsVisible(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        time.sleep(4)
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        if __name__ == '__main__':
            unittest.main()

    def test003_OpenAllPjct(self):
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        assert "ЭОР" in driver.title
        menu = driver.find_element_by_css_selector("i.entypo-menu")
        menu.click()
        time.sleep(2)
        allpj = driver.find_element_by_link_text("Все проекты")
        allpj.click()

    def test004_Not500or404(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test005_OpenForm(self):
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        #btn1 = driver.find_element_by_id("create-cp")
        #btn1.click()
        time.sleep(2)
        assert "ЭОР" in driver.title
        elem = driver.find_element_by_link_text('Поиск')
        elem.click()
        elemSearch = driver.find_element_by_id('search-text')
        elemSearch.click()
        elemSearch.send_keys('Selenium')
        elemSearch.send_keys(Keys.ENTER)
        time.sleep(3)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test006_FindBlock(self):
        #находим блок
        findBlock = driver.find_element_by_link_text('Создал Selenium _для редактирования')
        findBlock.click()
        time.sleep(3)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test007_FindProject(self):
        #находим проект
        findProject = driver.find_element_by_xpath('//div[2]/div[2]/table/tbody/tr/td[1]/h4/strong/a/span')
        findProject.click()
        time.sleep(2)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test008_CreateCP(self):
        #создаем контрольную точку
        CreateCP = driver.find_element_by_id('create-cp')
        CreateCP.click()
        time.sleep(1)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test009_FillingCPForm(self):
        time.sleep(3)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        _ = driver.find_element_by_class_name('warn-cp').text == 'контрольную точку'  # test
        time.sleep(2)
        #имя контрольной точки
        nameCP = driver.find_element_by_id('Checkpoint_TITLE').send_keys("контрольная точка созданная Selenium")
        time.sleep(3)
        #автор
        driver.implicitly_wait(10)
        #autorName = driver.find_element_by_id('DIV_AUTHOR_MISSION')
        #_ = wait.until(EC.element_to_be_clickable((By.XPATH, '//form/div/div[2]/div[10]/div/span/span/span/span[2]')))
        #autorName.click()
        time.sleep(3)
        #driver.implicitly_wait(10)
        #autorNameText = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        #autorNameText.send_keys('Б' + Keys.ENTER)
        time.sleep(2)
        #ответственный
        driver.implicitly_wait(10)
        responsibleName = driver.find_element_by_xpath("//div[@id='DIV_ID_RESPONSIBLE']/div/span/span/span/span[2]")
        responsibleName.click()
        time.sleep(2)
        responsibleNameText = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleNameText.send_keys('DIT' + Keys.ENTER)
        time.sleep(2)
        driver.implicitly_wait(10)
        #сроки
        terms = driver.find_element_by_id('Checkpoint_DEADLINE').send_keys('12345' + Keys.ENTER)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test009_TriggersCPTest(self):
        EditProject = driver.find_element_by_name('yt0')
        EditProject.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        #туда
        #triggerKPI = driver.find_element_by_xpath("//div[@id='DIV_IS_PRIORITY']/div/div/div/label")
        #triggerKPI.click()
        #time.sleep(1)
        #triggerDone = driver.find_element_by_xpath("//div[@id='DIV_IS_DONE']/div/div/div/span[2]")
        #triggerDone.click()
        time.sleep(1)
        #и обратно
        #triggerKPI.click()
        #time.sleep(1)
        #triggerDone.click()
        #time.sleep(1)

        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test010_ConfirmCPCreating(self):
        finishButton = driver.find_element_by_name('yt0')
        finishButton.click()
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        time.sleep(3)

    def test011_ClickEditButton(self):
        driver.implicitly_wait(20)
        time.sleep(3)
        editButton = driver.find_element_by_name('yt0')
        editButton.click()
        time.sleep(2)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        time.sleep(3)

    def test012_editCP(self):
        driver.implicitly_wait(20)
        time.sleep(3)
        #_ = driver.find_element_by_class_name('warn-cp').text == 'контрольную точку'
        nameCP = driver.find_element_by_id('Checkpoint_TITLE')
        nameCP.click()
        nameCP.send_keys(' редактировано ')
        EditProject = driver.find_element_by_name('yt0')
        EditProject.send_keys(Keys.PAGE_DOWN)
        saveButton = driver.find_element_by_name('yt0')
        saveButton.click()
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test013_AllRight(self):
        time.sleep(4)
        driver.implicitly_wait(20)
        _ = driver.find_element_by_id('C_TITLE').text == ' редактировано '
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test014_CreateCopyCP(self):
        time.sleep(3)
        assert "ЭОР" in driver.title
        '''
        FilterSetting = driver.find_element_by_xpath('html/body/div[1]/div[2]/div[4]/nav/div/div[2]/ul[2]/li/a/span')
        FilterSetting.click()
        SnipClick = driver.find_element_by_xpath('//nav/div/div[2]/ul[2]/li/ul/li[3]/div/ul/li[1]/div/label[1]/div')
        SnipClick.click()
        ConfirmFilter = driver.find_element_by_xpath('//div[1]/div[2]/div[4]/nav/div/div[2]/ul[2]/li/ul/li[4]/button[2]')
        ConfirmFilter.click()
        time.sleep(3)
        '''
        driver.find_element_by_name('yt1').click()
        time.sleep(3)
        driver.find_element_by_id('Checkpoint_DEADLINE').send_keys('12345' + Keys.ENTER)
        time.sleep(1)
        _ = driver.find_element_by_name('yt0')
        _.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        driver.find_element_by_name('yt0').click()
        time.sleep(3)

    def test015_DelCP(self):
        driver.find_element_by_name('yt2').click()
        time.sleep(1)
        driver.find_element_by_xpath('//div[3]/div/button').click()
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    if __name__ == '__main__':
        unittest.main()