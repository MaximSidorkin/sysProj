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

# логин в систему
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
        # time.sleep(3)
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
# переход к подзадаче
class CSeleniumSubtask_3(unittest.TestCase):
    def test_1GotoSubtask(self):
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        time.sleep(1)
        assert "ЭОР" in driver.title
        elem = driver.find_element_by_link_text('Поиск')
        elem.click()
        elemSearch = driver.find_element_by_id('search-text')
        elemSearch.click()
        elemSearch.send_keys('Selenium')
        elemSearch.send_keys(Keys.ENTER)

    def test_2FilterSetting(self):
        assert "ЭОР" in driver.title
        time.sleep(2)
        FilterSetting = driver.find_element_by_xpath('html/body/div[1]/div[2]/div[4]/nav/div/div[2]/ul[2]/li/a/span')
        FilterSetting.click()
        SnipClick = driver.find_element_by_xpath('//nav/div/div[2]/ul[2]/li/ul/li[3]/div/ul/li[1]/div/label[1]/div')
        SnipClick.click()
        ConfirmFilter = driver.find_element_by_xpath('//div[1]/div[2]/div[4]/nav/div/div[2]/ul[2]/li/ul/li[4]/button[2]')
        ConfirmFilter.click()
        time.sleep(3)
        findBlock = driver.find_element_by_link_text('Тестовый проект созданный Selenium')
        findBlock.click()
        time.sleep(1)
        findProject = driver.find_element_by_link_text('Для контрольной точки')
        findProject.click()
        time.sleep(1)
        CreateSubtask = driver.find_element_by_xpath('//div[2]/div[2]/div[3]/div/div[1]/div/div/button[1]')
        CreateSubtask.click()
        time.sleep(1)

    def test_3Not500or404(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

class DSeleniumFillingForm(unittest.TestCase):
    def test_1CheckForm(self):
        assert "ЭОР" in driver.title
        _ = driver.find_element_by_id('cp_title').text == 'Создание контрольной точки'
        _ = driver.find_element_by_class_name('warn-cp').text == 'контрольную точку'
        EditProject = driver.find_element_by_name('yt0')
        EditProject.send_keys(Keys.PAGE_DOWN)
        EditProject.click()
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test_2CheckWarningMsg(self):
        assert "ЭОР" in driver.title
        time.sleep(2)
        _ = driver.find_element_by_id('Checkpoint_TITLE_em_').text == 'Необходимо заполнить поле «Название».'
        _ = driver.find_element_by_id('Checkpoint_ID_AUTHOR_MISSION_em_').text == 'заполнить поле «Автор поручения».'
        _ = driver.find_element_by_id('Checkpoint_ID_RESPONSIBLE_em_').text == 'заполнить поле «Ответственный».'
        _ = driver.find_element_by_id('Checkpoint_DEADLINE_em_').text == 'заполнить поле «Срок исполнения (план)»'
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test_3FillingForm(self):
        assert "ЭОР" in driver.title
        time.sleep(2)

        #имя подзадачи
        nameCP = driver.find_element_by_id('Checkpoint_TITLE')
        nameCP.click()
        nameCP.send_keys("Подзадача созданная Selenium")
        time.sleep(1)
        # автор
        autorName = driver.find_element_by_xpath('//form/div/div[2]/div[9]/div/span/span[1]/span/span[1]')
        autorName.click()
        autorNameText = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        autorNameText.send_keys('Багреева')
        autorNameText.send_keys(Keys.ENTER)
        time.sleep(1)
        # ответственный
        responsibleName = driver.find_element_by_xpath('//form/div/div[2]/div[10]/div/span/span[1]/span/span[1]')
        responsibleName.click()
        responsibleNameText = driver.find_element_by_xpath('html/body/span/span/span[1]/input')
        responsibleNameText.send_keys('DIT')
        time.sleep(1)
        responsibleNameText.send_keys(Keys.ENTER)
        time.sleep(1)
        # сроки
        terms = driver.find_element_by_id('Checkpoint_DEADLINE')
        terms.click()
        terms.send_keys("12345")
        terms.send_keys(Keys.ENTER)
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test_4TriggersCPTest(self):
        EditProject = driver.find_element_by_name('yt0')
        EditProject.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        # туда
        triggerKPI = driver.find_element_by_xpath('//form/div/div[2]/div[18]/div/div/div/label')
        triggerKPI.click()
        time.sleep(1)
        triggerPriority = driver.find_element_by_xpath('//form/div/div[2]/div[19]/div/div/div/label')
        triggerPriority.click()
        time.sleep(1)
        triggerDone = driver.find_element_by_xpath('//form/div/div[2]/div[20]/div/div[1]/div/label')
        triggerDone.click()
        time.sleep(1)
        # и обратно
        triggerKPI.click()
        time.sleep(1)
        triggerPriority.click()
        time.sleep(1)
        triggerDone.click()
        time.sleep(1)

        # ещё один триггер
        triggerAL = driver.find_element_by_xpath('//form/div/div[2]/div[23]/div[1]/div[2]/div[3]/div/div/div/label')
        triggerAL.click()
        _ = driver.find_element_by_class_name('col-sm-5')
        time.sleep(2)
        triggerAL.click()






