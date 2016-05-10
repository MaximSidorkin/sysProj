import time
import unittest
global str
import page_objects

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("http://dev.eor.gosapi.ru/site/login")
driver.maximize_window()
wait = WebDriverWait(driver, 10)


class ASeleniumLogin_1(unittest.TestCase):
    def test_1LoginInEORDev(self):
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
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        assert "ЭОР" in driver.title
        menu = driver.find_element_by_css_selector("i.entypo-menu")
        menu.click()
        time.sleep(2)
        allpj = driver.find_element_by_link_text("Все проекты")
        allpj.click()

    if __name__ == '__main__':
        unittest.main()

    def test_2Not500or404(self):
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        if __name__ == '__main__':
            unittest.main()

class CSeleniumCreateNewPjct_3(unittest.TestCase):
    def test_1OpenForm(self):
        wait = WebDriverWait(driver, 10)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'create-cp')))
        btn1 = driver.find_element_by_id("create-cp")
        btn1.click()
        time.sleep(2)
        _ = driver.find_element_by_class_name('warn-cp')    #есть текст "Вы собираетесь создать блок."
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, '//form/div/div[2]/div[2]/div/div[1]/div[1]/span/i')))
        btn1 = driver.find_element_by_xpath('//form/div/div[2]/div[2]/div/div[1]/div[1]/span/i')
        btn1.click()

    if __name__ == '__main__':
        unittest.main()

    def test_2SearchBlock(self):
        SrcSelenBlock = driver.find_element_by_xpath('//form/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/input')
        SrcSelenBlock.send_keys('Selenium')
        time.sleep(2)
        # test
        GetTarget = driver.find_element(By.CLASS_NAME, "find-text").click()
        #GetTarget.click()
        #GetTarget = driver.find_element_by_xpath('//div/div[2]/div[2]/div/div[1]/div[2]/div[2]/ul/li[9]/a/span')
        #GetTarget.send_keys(Keys.ARROW_DOWN)

        #test

        #GetTarget = driver.find_element_by_xpath('//form/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/ul/li[25]/a/span/span')
        #GetTarget.click()
        time.sleep(2)

    if __name__ == '__main__':
        unittest.main()

    def test_3NewPjctFormBlock(self):
        wait.until(EC.element_to_be_clickable((By.ID, 'btnCloseForm')))      #test
        _ = driver.find_element_by_xpath("//form/div/div[2]/div[2]/div/div[4]/b")
        nameOfpjct = driver.find_element_by_xpath("//form/div/div[2]/div[4]/div/textarea")

        #nameOfpjct.click()  #test
        #time.sleep(1)
        #otherFild = driver.find_element_by_xpath('//div[2]/div[2]/div[2]/form/div/div[2]/div[6]/div/textarea')  #test
        #time.sleep(1)
        #otherFild.click()   #test
        #time.sleep(1)
        #otherFild.send_keys('1')
        #driver.find_element_by_xpath('//div[2]/div[2]/div[3]/form/div/div[2]/div[4]/div/div')   #test
        #time.sleep(1)
        #nameOfpjct = driver.find_element_by_xpath("//form/div/div[2]/div[4]/div/textarea")# test

        nameOfpjct.click()  #test
        nameOfpjct.send_keys("Тестовый проект созданный Selenium")

        time.sleep(2)
        _ = driver.find_element_by_class_name('warn-cp').text == 'проект'   # test
        autorDown = driver.find_element_by_xpath("//form/div/div[2]/div[8]/div/span/span[1]/span/span[2]")
        autorDown.click()
        autorName = driver.find_element_by_xpath("html/body/span/span/span[1]/input")
        autorName.send_keys(Keys.ARROW_DOWN)
        autorName.send_keys(Keys.ARROW_DOWN)
        #autorName.send_keys("Багрее")
        autorName.send_keys(Keys.ENTER)
        pjctMansger = driver.find_element_by_xpath("//form/div/div[2]/div[9]/div/span/span[1]/span/span[2]")
        pjctMansger.click()
        pjctMansgerName = driver.find_element_by_xpath("html/body/span/span/span[1]/input")
        pjctMansgerName.send_keys(Keys.ARROW_DOWN)
        pjctMansgerName.send_keys(Keys.ENTER)

    if __name__ == '__main__':
        unittest.main()

    def test_4CheckNoYesIsAvalible(self):
        NoElem = driver.find_element_by_xpath("//form/div/div[2]/div[20]/div/div[1]/div/label")
        NoElem.click()
        time.sleep(1)
        No2Elem = driver.find_element_by_xpath("//form/div/div[2]/div[21]/div/div[1]/div/label")
        No2Elem.click()
        time.sleep(1)
        YesElem = driver.find_element_by_xpath("//form/div/div[2]/div[20]/div/div[1]/div/label")
        YesElem.click()

    if __name__ == '__main__':
        unittest.main()

    def test_5ConfirmCreatingPjct(self):
        time.sleep(1)
        CreateButton = driver.find_element_by_xpath("//form/div/div[2]/div[23]/input[2]")
        CreateButton.click()

class DSeleniumEditProject(unittest.TestCase):
    def test_1CheckPage(self):
        #self.assertEqual()
        # <i class="fa fa-spinner fa-spin fa-2x"></i>
        # проверить элементы на странице
        time.sleep(5)
        driver.set_page_load_timeout(5)
        #try:
        #    driver.find_element_by_xpath('html/body/div[1]/div[2]/div[4]/div[2]/div[2]/div[2]/i').size()
        #except Exception:
        #    print('Тест завершен с ошибкой!')
        #finally:
        #    driver.save_screenshot('BlockError.png')
        #    print('Нет возможности завершить создание Блока, страница не прогружается, см. скриншот BlockError')
        #    driver.close()
        # repair it
        _ = WebDriverWait(driver, 50)
        _ = wait.until(EC.element_to_be_clickable((By.NAME, 'yt0')))
        EditProject = driver.find_element_by_name('yt0')
        EditProject.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        EditProject.click()

    if __name__ == '__main__':
        unittest.main()

    def test_2editProject(self):
        time.sleep(4)
        ShortName = driver.find_element_by_xpath("//form/div/div[2]/div[5]/div/textarea")
        ShortName.send_keys("Краткое наименование")
        FullName = driver.find_element_by_xpath("//form/div/div[2]/div[4]/div/textarea")
        FullName.send_keys(" edit ")
        SaveEdit = driver.find_element_by_xpath('//form/div/div[2]/div[22]/input[2]')
        SaveEdit.click()

    if __name__ == '__main__':
        unittest.main()

    def test_3AllRight(self):
        time.sleep(4)
        _ = driver.find_element_by_id('C_TITLE').text == ' edit '
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    if __name__ == '__main__':
        unittest.main()

    def test_4SeekAndDestroy(self):
       time.sleep(3)
       assert "ЭОР" in driver.title
       elem = driver.find_element_by_link_text('Поиск')
       elem.click()
       time.sleep(3)
       elemSearch = driver.find_element_by_id('search-text')
       elemSearch.click()
       elemSearch.send_keys(' edit ')
       elemSearch.send_keys(Keys.ENTER)
       time.sleep(2)
       elemTestBlock = driver.find_element_by_xpath('//div[2]/div[2]/div/table/tbody/tr/td[1]/h4')
       elemTestBlock.click()
       time.sleep(3)
       DelProject = driver.find_element_by_xpath('//div[2]/div[2]/div[2]/table/tbody/tr/td[2]/button[2]')
       DelProject.click()
       time.sleep(2)
       elemNo = driver.find_element_by_xpath("html/body/div[3]/div[3]/div/button[2]")
       elemNo.click()
       DelProject.click()
       time.sleep(3)
       elemYes = driver.find_element_by_xpath('html/body/div[3]/div[3]/div/button[1]')
       elemYes.click()

    if __name__ == '__main__':
        unittest.main()





