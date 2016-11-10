import time
import unittest
import HTMLTestRunner

global str

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

dev = 'https://dev.eor.gosapi.ru/'
test = 'https://test.eor.gosapi.ru/'
dev1 = 'https://minakov.eor.gosapi.ru/'
dev2 = 'https://shmyrev.eor.gosapi.ru/'
tronov = 'https://tronov.eor.gosapi.ru/'
vragov = 'https://vragov.eor.gosapi.ru/'
surin = 'https://surin.eor.gosapi.ru/'

driver = webdriver.Firefox()
driver.get(dev)
driver.maximize_window()
wait = WebDriverWait(driver, 20)
driver.implicitly_wait(20)

class ASeleniumAutoTest_1(unittest.TestCase):
    def test001_CreatedInEORDev(self):
        assert "Login" in driver.title
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'LoginForm_username')))
        elem = driver.find_element_by_id("LoginForm_username")
        elem.send_keys("Ipad")
        elem = driver.find_element_by_id("LoginForm_password")
        elem.send_keys("ipad")
        elem.send_keys(Keys.RETURN)
    def test002_Not500or404andLoginIsVisible(self):
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "Error" not in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'hidden-xs')))
            # open desktop

    def test003_OpenAllPjct(self):
        #time.sleep(3)
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        assert "ЭОР" in driver.title
        menu = driver.find_element_by_css_selector("i.entypo-menu")
        menu.click()
        time.sleep(6)
        allpj = driver.find_element_by_link_text("Все проекты")
        allpj.click()
    def test004_Not500or404(self):
        title = wait.until(EC.title_is('ЭОР - Checkpoint'))
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Checkpoint" in driver.title
        # assert "Error" not in driver.title

    def test005_Schedule(self):
        schedul = driver.find_element_by_link_text("Расписание")
        schedul.click()
        time.sleep(6)
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-meeting')))

    def test006_Not500or404(self):
        title = wait.until(EC.title_is('ЭОР - Default'))
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Default" in driver.title

    def test007_Question(self):
        question = driver.find_element_by_link_text("Вопросы/Приоритеты")
        question.click()
        time.sleep(4)
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'navbar-header')))

    def test008_Not500or404(self):
        title = wait.until(EC.title_is('ЭОР - Question'))
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Question" in driver.title

    def test009_Material(self):
        material = driver.find_element_by_link_text("Материалы")
        material.click()
        time.sleep(4)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'search-show')))

    def test010_Not500or404(self):
        time.sleep(4)
        title = wait.until(EC.title_is('ЭОР - Material'))
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Material" in driver.title

    def test011_Npa(self):
        npa = driver.find_element_by_link_text("Нормативно-правовые акты")
        npa.click()
        time.sleep(4)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'search-show')))

    def test012_Not500or404(self):
        title = wait.until(EC.title_is('ЭОР - Npa'))
        time.sleep(4)
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!') # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Npa" in driver.title

    def test013_Document(self):
        document = driver.find_element_by_link_text("Библиотека")
        document.click()
        time.sleep(4)
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'search-show')))

    def test014_Not500or404(self):
        title = wait.until(EC.title_is('ЭОР - Document'))
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Document" in driver.title

    def test015_Report(self):
        report = driver.find_element_by_link_text("Отчёты")
        report.click()
        time.sleep(1)
        # Отчёт по контрольным точкам
        report1 = driver.find_element_by_link_text("Отчёт по контрольным точкам")
        report1.click()
        time.sleep(4)
        title = wait.until(EC.title_is('ЭОР - Report'))
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'load_table')))
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        # Отчёт Проект Расписания
        schedule = driver.find_element_by_link_text('Отчёт Проект Расписания')
        schedule.click()
        time.sleep(4)
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'title_gears')))
        title = wait.until(EC.title_is('ЭОР - Schedule'))
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Schedule" in driver.title
        # Отчёт Рейтинги
        rating = driver.find_element_by_link_text('Отчёт Рейтинги')
        rating.click()
        time.sleep(4)
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'title_gears')))
        title = wait.until(EC.title_is('ЭОР - Rating'))
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Rating" in driver.title

    def test016_Admin(self):
        admin = driver.find_element_by_link_text("Администрирование")
        admin.click()
        time.sleep(1)
        # Пользователи
    def test017_Users(self):
        users = driver.find_element_by_link_text('Пользователи')
        users.click()
        time.sleep(4)
        title = wait.until(EC.title_is('ЭОР - User'))
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        _ = wait.until(EC.element_to_be_clickable((By.ID, 'search-show')))
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - User" in driver.title

        # Роли
    def test018_Role(self):
        users = driver.find_element_by_link_text('Роли')
        users.click()
        time.sleep(4)
        title = wait.until(EC.title_is('ЭОР - Role'))
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        _ = wait.until(EC.element_to_be_clickable((By.ID, 'btn_create_user')))
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Role" in driver.title
        # Привилегии
    def test019_Privilege(self):
        users = driver.find_element_by_link_text('Права доступа')
        users.click()
        time.sleep(4)
        title = wait.until(EC.title_is('ЭОР - Privilege'))
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        time.sleep(5)
        _ = wait.until(EC.presence_of_element_located((By.ID, 'yw1')))
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Privilege" in driver.title
        # Журналы
    def test020_Journal(self):
        journ = driver.find_element_by_link_text("Журналы")
        journ.click()
        time.sleep(1)
        # Авторизации
    def test021_Logs(self):
        autor = driver.find_element_by_link_text("Авторизации")
        autor.click()
        time.sleep(4)
        title = wait.until(EC.title_is('ЭОР - Logs'))
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        _ = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'dropdown')))
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Logs" in driver.title
        # Обмен данными
    def test022_Data(self):
        autor = driver.find_element_by_link_text("Обмен данными")
        autor.click()
        time.sleep(4)
        title = wait.until(EC.title_is('ЭОР - Data'))
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        _ = wait.until(EC.presence_of_element_located((By.ID, 'resetFilters')))
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Data" in driver.title
        # Операции пользователя
    def test023_Operation(self):
        autor = driver.find_element_by_link_text("Операции пользователя")
        autor.click()
        time.sleep(4)
        title = wait.until(EC.title_is('ЭОР - Operation'))
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        _ = wait.until(EC.presence_of_element_located((By.ID, 'resetFilters')))
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Operation" in driver.title
        # Справочники
    def test024_Dictionary(self):
        dictionary = driver.find_element_by_link_text("Справочники")
        dictionary.click()
        time.sleep(4)
        title = wait.until(EC.title_is('ЭОР - Dictionary'))
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "Error" not in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Этапы НПА')))
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        # Приложения
    def test025_Apps(self):
        apps = driver.find_element_by_link_text("Приложения")
        apps.click()
        time.sleep(1)
        # Управление iPad ЭОР
    def test026_Ipad(self):
        driv = driver.find_element_by_link_text("Управление iPad ЭОР")
        driv.click()
        time.sleep(4)
        title = wait.until(EC.title_is('ЭОР - Ipad'))
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Создать релиз')))
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        # Структура данных
    def test027_Struct(self):
        struc = driver.find_element_by_link_text("Структура данных")
        struc.click()
        time.sleep(1)
        # Управление структурой
    def test028_AdminStr(self):
        admStr = driver.find_element_by_link_text("Управление структурой")
        admStr.click()
        time.sleep(4)
        title = wait.until(EC.title_is('ЭОР - Gii'))
        assert "ЭОР - Gii" in driver.title
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title

        # Управление хранилищем данных
    def test029_Database(self):
        database = driver.find_element_by_link_text("Управление хранилищем данных")
        database.click()
        time.sleep(4)
        title = wait.until(EC.title_is('ЭОР - Database'))
        assert "ЭОР - Database" in driver.title
        try:
            assert 'Error' not in driver.title
        except:
            print('ошибка 500!')  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        # Ресурсы ИС
    def test030_Resource(self):
        res = driver.find_element_by_link_text("Ресурсы ИС")
        res.click()
        time.sleep(2)
        #

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(ASeleniumAutoTest_1))
    # File
    buf = open("at_for_500and404.html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=buf,
        title='СОЗДАНИЕ/РЕДАКТИРОВАНИЕ/УДАЛЕНИЕ СОВЕЩАНИЯ ИЗ РАСПИСАНИЯ И РАБОЧЕГО СТОЛА',
        description='Отчет по тестированию'
    )
    runner.run(suite)



