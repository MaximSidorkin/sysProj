import time
import unittest
global str

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("https://dev.eor.gosapi.ru")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# логин в систему
class ASeleniumAutoTest_1(unittest.TestCase):
    def test001_CreatedInEORDev(self):
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
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))

    def test003_OpenAllPjct(self):
        wait = WebDriverWait(driver, 10)
        # time.sleep(3)
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        assert "ЭОР" in driver.title
        menu = driver.find_element_by_css_selector("i.entypo-menu")
        menu.click()
        time.sleep(4)
        allpj = driver.find_element_by_link_text("Все проекты")
        allpj.click()

    def test004_Not500or404(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

# переход к подзадаче
    def test005_GotoSubtask(self):
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        time.sleep(1)
        assert "ЭОР" in driver.title
        elem = driver.find_element_by_link_text('Поиск')
        elem.click()
        elemSearch = driver.find_element_by_id('search-text')
        elemSearch.click()
        elemSearch.send_keys('Selenium')
        elemSearch.send_keys(Keys.ENTER)

    def test006_FilterSetting(self):
        assert "ЭОР" in driver.title
        time.sleep(3)
        '''
        FilterSetting = driver.find_element_by_xpath('html/body/div[1]/div[2]/div[4]/nav/div/div[2]/ul[2]/li/a/span')
        FilterSetting.click()
        SnipClick = driver.find_element_by_xpath('//nav/div/div[2]/ul[2]/li/ul/li[3]/div/ul/li[1]/div/label[1]/div')
        SnipClick.click()
        ConfirmFilter = driver.find_element_by_xpath('//div[1]/div[2]/div[4]/nav/div/div[2]/ul[2]/li/ul/li[4]/button[2]')
        ConfirmFilter.click()
        '''
        time.sleep(2)
        findeBlock = driver.find_element_by_link_text('Создал Selenium _для редактирования').click()
        time.sleep(2)
        findeProject = driver.find_element_by_xpath("//div[2]/table/tbody/tr/td").click()
        time.sleep(2)
        plusST = driver.find_element_by_xpath('//div[@id="item-toolbar"]/button').click()
        print('STOP!')

    def test007_Not500or404(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test008_CheckForm(self):
        assert "ЭОР" in driver.title
        time.sleep(3)
        _ = driver.find_element_by_id('cp_title').text == 'Создание контрольной точки'
        time.sleep(2)
        _ = driver.find_element_by_class_name('warn-cp').text == 'контрольную точку'
        EditProject = driver.find_element_by_name('yt0')
        time.sleep(2)
        EditProject.send_keys(Keys.PAGE_DOWN)
        EditProject.click()
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test009_CheckWarningMsg(self):
        assert "ЭОР" in driver.title
        time.sleep(3)
        _ = driver.find_element_by_id('Checkpoint_TITLE_em_').text == 'Необходимо заполнить поле «Название».'
        _ = driver.find_element_by_id('Checkpoint_ID_AUTHOR_MISSION_em_').text == 'заполнить поле «Автор поручения».'
        _ = driver.find_element_by_id('Checkpoint_ID_RESPONSIBLE_em_').text == 'заполнить поле «Ответственный».'
        _ = driver.find_element_by_id('Checkpoint_DEADLINE_em_').text == 'заполнить поле «Срок исполнения (план)»'
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test010_FillingForm(self):
        assert "ЭОР" in driver.title
        time.sleep(2)

        #имя подзадачи
        nameCP = driver.find_element_by_id('Checkpoint_TITLE')
        nameCP.click()
        nameCP.send_keys("Подзадача созданная Selenium")
        time.sleep(2)
        # автор
        autorName = driver.find_element_by_xpath("//div[@id='DIV_AUTHOR_MISSION']/div/span/span/span/span[2]").click()
        #autorName.click()
        autorNameText = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        autorNameText.send_keys('Багреева')
        autorNameText.send_keys(Keys.ENTER)
        time.sleep(2)
        # ответственный
        responsibleName = driver.find_element_by_xpath("//div[@id='DIV_ID_RESPONSIBLE']/div/span/span/span/span[2]").click()
        #responsibleName.click()
        responsibleNameText = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleNameText.send_keys('DIT')
        time.sleep(2)
        responsibleNameText.send_keys(Keys.ENTER)
        time.sleep(2)
        # сроки
        terms = driver.find_element_by_id('Checkpoint_DEADLINE')
        terms.click()
        terms.send_keys("12345")
        terms.send_keys(Keys.ENTER)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test011_TriggersCPTest(self):
        EditProject = driver.find_element_by_name('yt0')
        EditProject.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        EditProject = driver.find_element_by_name('yt0')
        EditProject.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        #туда
        triggerKPI = driver.find_element_by_xpath("//div[@id='DIV_IS_PRIORITY']/div/div/div/label")
        triggerKPI.click()
        time.sleep(1)
        triggerDone = driver.find_element_by_xpath("//div[@id='DIV_IS_DONE']/div/div/div/span[2]")
        triggerDone.click()
        time.sleep(1)
        #и обратно
        triggerKPI.click()
        time.sleep(1)
        triggerDone.click()
        time.sleep(2)

    def test012_ConfirmCreation(self):
        elem = driver.find_element_by_name('yt0')
        elem.click()
        time.sleep(3)
        wait = WebDriverWait(driver, 10)
        #wait.until(EC.element_to_be_clickable((By.XPATH, '//div[4]/div/div[2]/div/div[2]/div[11]/input[3]')))
        _ = driver.find_element_by_xpath('//div[2]/div[4]/div/div[2]/div/div[1]/div[1]').text == 'Паспорт Контрольной'

    def test013_CreateCopyST(self):
        time.sleep(2)
        driver.find_element_by_name('yt1').click()
        time.sleep(3)
        driver.find_element_by_id('Checkpoint_DEADLINE').send_keys('12345' + Keys.ENTER)
        time.sleep(1)
        _ = driver.find_element_by_name('yt0')
        _.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        driver.find_element_by_name('yt0').click()
        time.sleep(3)

    def test014_DeleteSubTask(self):
        time.sleep(2)
        deleteButton = driver.find_element_by_name('yt2')
        deleteButton.click()
        time.sleep(2)
        elemYes = driver.find_element_by_xpath('//div[3]/div/button')
        elemYes.click()

        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title


    if __name__ == '__main__':
        unittest.main()








