import time
import unittest, requests
import HTMLTestRunner, sys

global str

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

dev = 'https://dev.eor.gosapi.ru/new'
test = 'https://test.eor.gosapi.ru/'
dev1 = 'https://minakov.eor.gosapi.ru/'
dev2 = 'https://shmyrev.eor.gosapi.ru/'
tronov = 'https://tronov.eor.gosapi.ru/'
vragov = 'https://vragov.eor.gosapi.ru/'
surin = 'https://surin.eor.gosapi.ru/'
oracle = 'https://task.eor.gosapi.ru/oracle/site/login'
pgs = 'https://task.eor.gosapi.ru/pgs/site/login'

driver = webdriver.Chrome()
driver.get(pgs)
driver.maximize_window()
wait = WebDriverWait(driver, 40)
driver.implicitly_wait(40)

class ASeleniumAutoTest_1(unittest.TestCase):
    def test001_CreatedInEORDev(self):
        try:
            assert 'ЭОР - Error' not in driver.title
            print('\n 1. Нет ошибок при вводе логина')
        except:
            print('ошибка 500!')
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        assert "Login" in driver.title
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)

    def test002_Not500or404andLoginIsVisible(self):
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
        try:
            print('\n 2. Нет ошибок на рабочем столе')
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "ЭОР - Error" not in driver.title
        # open desktop

    def test003_OpenAllPjct(self):
        _ = wait.until(EC.element_to_be_clickable((By.XPATH, '//i')))
        assert "ЭОР" in driver.title
        time.sleep(1)
        driver.find_element_by_xpath('//i').click()
        time.sleep(6)
        allpj = driver.find_element_by_link_text("Все проекты")
        allpj.click()
        print('\n 3. переходим раздел "Все проекты"')

    def test004_Not500or404(self):
        title = wait.until(EC.title_is('ЭОР - Checkpoint'))
        # test
        driver.find_element_by_id('search-show').click()
        time.sleep(1)
        textFild = driver.find_element_by_id('search-text')
        textFild.send_keys("'")
        textFild.send_keys(Keys.ENTER)
        time.sleep(5)
        r = requests.get('https://task.eor.gosapi.ru/pgs/checkpoint/checkpoint/table')
        time.sleep(2)
        if r.status_code == 404 or r.status_code == 500:
            print(' ERROR! STATUS CODE IS WRONG!',r)
        else:
            print(' Ok. Status code is',r)
        # test
        try:
            assert 'Error' not in driver.title
            print('\n 4. Нет ошибок в разделе "Все проекты"')
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Checkpoint" in driver.title

    def test005_Schedule(self):
        schedul = driver.find_element_by_link_text("Расписание")
        schedul.click()
        time.sleep(2)
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-meeting')))
        print('\n 5. Переходим в раздел "Расписание"')

    def test006_Not500or404(self):
        title = wait.until(EC.title_is('ЭОР - Default'))
        try:
            assert 'ЭОР - Error' not in driver.title
            driver.find_element_by_xpath('//td/span')
            print('\n 6. Нет ошибок в разделе "Расписание"')
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Default" in driver.title

    def test007_Question(self):
        question = driver.find_element_by_link_text("Вопросы/Приоритеты")
        question.click()
        time.sleep(4)
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'navbar-header')))
        print('\n 7. Переходим в раздел "Вопросы/приоритеты"')

    def test008_Not500or404(self):
        title = wait.until(EC.title_is('ЭОР - Question'))
        try:
            assert 'ЭОР - Error' not in driver.title
            print('\n 8. Нет ошибок в разделе "Вопросы/приоритеты"')
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Question" in driver.title

    def test009_Material(self):
        material = driver.find_element_by_link_text("Материалы")
        material.click()
        time.sleep(4)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'search-show')))
        print('\n 9. Переходим в раздел "Материалы"')
        # test
        _ = wait.until(EC.element_to_be_clickable((By.XPATH,"//nav/div/div[2]/ul/li/a/span")))
        # filter period
        #driver.find_element_by_xpath('//nav/div/div[2]/ul/li/a/span').click()
        #time.sleep(2)
        #driver.find_element_by_xpath("//a[contains(text(),'Не учитывать')]").click()
        # filter where
        #driver.find_element_by_xpath('//ul[2]/li/a/span').click()
        #time.sleep(2)
        #driver.find_element_by_link_text('Из Совещаний').click()
        # spinner
        #try:
        #    driver.find_element_by_xpath('//div[2]/i')
        #    print(' Спиннер появился')
        #except:
        #    print(' Спиннер не появился/появился на очень короткое время')
        #try:
        #    driver.find_element_by_css_selector('div.alert.alert-default')
        #    print(" Появилось сообщение о не найденых материалоах")
        #except:
        #    print(" Не появилось сообщение о не найденых материалоах")
        #try:
        #    driver.find_element_by_css_selector("div.panel-title")
        #    print(' Появился список материалов')
        #except:
        #    print(" Не появился список материалов!")

    def test010_Not500or404(self):
        time.sleep(4)
        title = wait.until(EC.title_is('ЭОР - Material'))
        try:
            assert 'ЭОР - Error' not in driver.title
            print('\n 10. Нет ошибок в разделе "Материалы"')
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Material" in driver.title

    def test011_Npa(self):
        npa = driver.find_element_by_link_text("Нормативно-правовые акты")
        npa.click()
        time.sleep(4)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'search-show')))
        print('\n 11. Переходим в раздел "Нормативно правовые акты"')

    def test012_Not500or404(self):
        title = wait.until(EC.title_is('ЭОР - Npa'))
        time.sleep(4)
        try:
            assert 'ЭОР - Error' not in driver.title
            print('\n 12. Нет ошибок в разделе "Нормативно правовые акты"')
        except:
            print('ошибка 500!') # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Npa" in driver.title

    def test013_Document(self):
        #self.skipTest(self)
        document = driver.find_element_by_link_text("Библиотека")
        document.click()
        time.sleep(4)
        assert 'ЭОР - Error' not in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'search-show')))
        print('\n 13. Переходим в раздел "Библиотека"')

    def test014_Not500or404(self):
        #self.skipTest(self)
        title = wait.until(EC.title_is('ЭОР - Document'))
        try:
            assert 'ЭОР - Error' not in driver.title
            print('\n 14. Нет ошибок в разделе "Библиотека"')
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Document" in driver.title

    def test015_Report(self):
        report = driver.find_element_by_link_text("Отчёты")
        report.click()
        time.sleep(1)
        # Отчёт по контрольным точкам
        report1 = driver.find_element_by_link_text("Отчет по задачам")
        report1.click()
        time.sleep(4)
        title = wait.until(EC.title_is('ЭОР - Report'))
        try:
            assert 'ЭОР - Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'load_table')))
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        # add
        try:    # вкладка "Блок"
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div.tree.project > div.head')))
            driver.find_element_by_css_selector('div.tree.project > div.head')
            print('Ошибка 500 при переходе на вкладку "Блок" не найдено')
        except:
            self.fail(
                print('Ошибка 500! при переходе на вкладку "Блок" в разделе Отчеты -> Отчёты по контрольным точкам')
            )
        driver.find_element_by_xpath('//li/label[2]').click()
        try:    # вкладка "Проект"
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div.tree.project > div.head')))
            driver.find_element_by_css_selector('div.tree.project > div.head')
            print('Ошибка 500 при переходе на вкладку "Проект" не найдено')
        except:
            self.fail(
                print('Ошибка 500! при переходе на вкладку "Проект" в разделе Отчеты -> Отчёты по контрольным точкам')
            )
        wait.until(EC.element_to_be_clickable((By.XPATH, '//label[3]')))
        driver.find_element_by_xpath('//label[3]').click()
        try:    # вкладка "Ответственный"
            wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.tree.project > div.head')))
            driver.find_element_by_css_selector('div.tree.project > div.head')
            print('Ошибка 500 при переходе на вкладку "Ответственный" не найдено')
        except:
            self.fail(
                print('Ошибка 500! при переходе на вкладку "Ответственный" в разделе Отчеты -> Отчёты по контрольным точкам')
            )
        wait.until(EC.element_to_be_clickable((By.XPATH, '//label[4]')))
        driver.find_element_by_xpath('//label[4]').click()
        try:  # вкладка "Замы"
            time.sleep(7)
            driver.find_element_by_id('report-content')
            print('Ошибка 500 при переходе на вкладку "Замы" не найдено')
        except:
            self.fail(
                print('Ошибка 500! при переходе на вкладку "Замы" в разделе Отчеты -> Отчёты по контрольным точкам')
            )
        # Отчёт Проект Расписания
        schedule = driver.find_element_by_link_text('Отчет по совещаниям')
        schedule.click()
        time.sleep(4)
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'title_gears')))
        title = wait.until(EC.title_is('ЭОР - Schedule'))
        try:
            assert 'ЭОР - Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Schedule" in driver.title
        # Отчёт Рейтинги по Проектам
        rating = driver.find_element_by_link_text('Отчёт Рейтинги по Проектам')
        rating.click()
        time.sleep(4)
        title = wait.until(EC.title_is('ЭОР - Projectsrating'))
        try:
            driver.find_element_by_xpath('//div[2]/table/thead/tr/th')
            assert 'ЭОР - Error' not in driver.title
            print('\n 15. Переходим в раздел "Отчеты", во всех отчетах нет ошибок')
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        # Отчёт по Проектам
        rating = driver.find_element_by_link_text('Отчёт по Проектам')
        rating.click()
        time.sleep(4)
        title = wait.until(EC.title_is('ЭОР - Отчет по проектам'))
        try:
            driver.find_element_by_css_selector('div.project-report-group-title')
            assert 'ЭОР - Error' not in driver.title
            print('\n 15. Переходим в раздел "Отчёт по Проектам", во всех отчетах нет ошибок')
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title

    def test016_Admin(self):
        self.skipTest(self)
        admin = driver.find_element_by_link_text("Администрирование")
        admin.click()
        time.sleep(1)
        print('\n 16. Переходим в раздел "Администрирование"')
        # Пользователи

    def test017_Users(self):
        self.skipTest(self)
        users = driver.find_element_by_link_text('Пользователи')
        users.click()
        time.sleep(4)
        title = wait.until(EC.title_is('ЭОР - User'))
        try:
            assert 'ЭОР - Error' not in driver.title
            print('\n 17. Нет ошибок в разделе пользователи')
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        _ = wait.until(EC.element_to_be_clickable((By.ID, 'search-show')))
        try:
            assert 'ЭОР - Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - User" in driver.title

        # Роли
    def test018_Role(self):
        self.skipTest(self)
        users = driver.find_element_by_link_text('Роли')
        users.click()
        time.sleep(4)
        title = wait.until(EC.title_is('ЭОР - Role'))
        try:
            print('\n 18. Нет ошибок в разделе "Роли"')
            assert 'ЭОР - Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        _ = wait.until(EC.element_to_be_clickable((By.ID, 'btn_create_user')))
        try:
            print('\n Нет ошибки на странице пользователи')
            assert 'ЭОР - Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Role" in driver.title
        # Привилегии
    def test019_Privilege(self):
        self.skipTest(self)
        users = driver.find_element_by_link_text('Права доступа')
        users.click()
        time.sleep(4)
        title = wait.until(EC.title_is('ЭОР - Privilege'))
        try:
            assert 'ЭОР - Error' not in driver.title
            print('\n 19. Переходим в раздел "Права доступа"')
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        time.sleep(5)
        _ = wait.until(EC.presence_of_element_located((By.ID, 'yw1')))
        try:
            print('\n Нет ошибки на странице "Права доступа"')
            assert 'ЭОР - Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Privilege" in driver.title
        # Журналы
    def test020_Journal(self):
        self.skipTest(self)
        journ = driver.find_element_by_link_text("Журналы")
        journ.click()
        time.sleep(1)
        print('\n 20. переходим в раздел "Журналы"')
        # Авторизации
    def test021_Logs(self):
        self.skipTest(self)
        autor = driver.find_element_by_link_text("Авторизации")
        autor.click()
        time.sleep(4)
        title = wait.until(EC.title_is('ЭОР - Logs'))
        try:
            assert 'ЭОР - Error' not in driver.title
            print('\n 21. Переходим в раздел "Авторизации"')
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        _ = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'dropdown')))
        try:
            assert 'ЭОР - Error' not in driver.title
            print('\n нет ошибко в разделе "Авторизации"')
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Logs" in driver.title
        # Обмен данными
    def test022_Data(self):
        self.skipTest(self)
        autor = driver.find_element_by_link_text("Обмен данными")
        autor.click()
        time.sleep(4)
        title = wait.until(EC.title_is('ЭОР - Data'))
        try:
            assert 'ЭОР - Error' not in driver.title
            print('\n 22. Переходим в раздел "Обмен данными"')
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        _ = wait.until(EC.presence_of_element_located((By.ID, 'resetFilters')))
        try:
            assert 'ЭОР - Error' not in driver.title
            print('\n нет ошибок в разделе "Авторизации"')
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Data" in driver.title
        # Операции пользователя
    def test023_Operation(self):
        self.skipTest(self)
        autor = driver.find_element_by_link_text("Операции пользователя")
        autor.click()
        time.sleep(4)
        title = wait.until(EC.title_is('ЭОР - Operation'))
        try:
            assert 'ЭОР - Error' not in driver.title
            print('\n 23. Переходим в раздел "Операции пользователя"')
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        _ = wait.until(EC.presence_of_element_located((By.ID, 'resetFilters')))
        try:
            assert 'ЭОР - Error' not in driver.title
            print('\n Нет ошибок в разделе "Операции пользователя"')
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Operation" in driver.title
        # Справочники
    def test024_Dictionary(self):
        self.skipTest(self)
        dictionary = driver.find_element_by_link_text("Справочники")
        dictionary.click()
        time.sleep(4)
        title = wait.until(EC.title_is('ЭОР - Dictionary'))
        try:
            assert 'ЭОР - Error' not in driver.title
            print('\n 24. Переходим в раздел "Справочники"')
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "Error" not in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Этапы НПА')))
        try:
            assert 'ЭОР - Error' not in driver.title
            print('\n нет ошибок в разделе "Справочники"')
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        # Структура данных
    def test027_GoodTone(self):
        print('\n 27. ТЕСТ ЗАВЕРШЕН ')
        driver.close()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumAutoTest_1))
    # File
    buf = open("at_for_500and404.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=buf,
        title='ПРОВЕРКА ВСЕХ РАЗДЕЛОВ ЭОР НА ОШИБКИ 500 И 404',
        description='Отчет по тестированию'
    )
    ret = not runner.run(suite).wasSuccessful()
    sys.exit(ret)



