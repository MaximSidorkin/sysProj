import time
import unittest
global str

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

dev = 'http://dev.eor.gosapi.ru/'
test = 'http://test.eor.gosapi.ru/'

driver = webdriver.Firefox()
driver.get(dev)
driver.maximize_window()
wait = WebDriverWait(driver, 10)

class ASeleniumAutoTest_1(unittest.TestCase):
    def test_1CreatedInEORDev(self):
        assert "Login" in driver.title
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
            # open desktop

class BSeleniumOpenAllPjct_2(unittest.TestCase):
    def test_1OpenAllPjct(self):
        #time.sleep(3)
        _ = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.entypo-menu')))
        assert "ЭОР" in driver.title
        menu = driver.find_element_by_css_selector("i.entypo-menu")
        menu.click()
        time.sleep(4)
        allpj = driver.find_element_by_link_text("Все проекты")
        allpj.click()
    def test_2Not500or404(self):
        title = wait.until(EC.title_is('ЭОР - Checkpoint'))
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Checkpoint" in driver.title

        if __name__ == '__main__':
            unittest.main()

    def test_3Schedule(self):
        schedul = driver.find_element_by_link_text("Расписание")
        schedul.click()
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-meeting')))

    def test_4Not500or404(self):
        title = wait.until(EC.title_is('ЭОР - Default'))
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Default" in driver.title

        if __name__ == '__main__':
            unittest.main()

    def test_5Question(self):
        question = driver.find_element_by_link_text("Вопросы/Приоритеты")
        question.click()
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'navbar-header')))

    def test_6Not500or404(self):
        title = wait.until(EC.title_is('ЭОР - Question'))
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Question" in driver.title

        if __name__ == '__main__':
            unittest.main()

    def test_7Material(self):
        material = driver.find_element_by_link_text("Материалы")
        material.click()
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'search-a')))

    def test_8Not500or404(self):
        title = wait.until(EC.title_is('ЭОР - Material'))
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Material" in driver.title

        if __name__ == '__main__':
            unittest.main()

    def test_9Npa(self):
        npa = driver.find_element_by_link_text("Нормативно-правовые акты")
        npa.click()
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'search-show')))

    def test_9aNot500or404(self):
        title = wait.until(EC.title_is('ЭОР - Npa'))
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Npa" in driver.title

        if __name__ == '__main__':
             unittest.main()

    def test_9bDocument(self):
        document = driver.find_element_by_link_text("Библиотека")
        document.click()
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'search-show')))

    def test_9cNot500or404(self):
        title = wait.until(EC.title_is('ЭОР - Document'))
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Document" in driver.title

    def test_9dReport(self):
        report = driver.find_element_by_link_text("Отчёты")
        report.click()
        time.sleep(1)
        # Отчёт по контрольным точкам
        report1 = driver.find_element_by_link_text("Отчёт по контрольным точкам")
        report1.click()
        title = wait.until(EC.title_is('ЭОР - Report'))
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'load_table')))
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        # Отчёт Проект Расписания
        schedule = driver.find_element_by_link_text('Отчёт Проект Расписания')
        schedule.click()
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'title_gears')))
        title = wait.until(EC.title_is('ЭОР - Schedule'))
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Schedule" in driver.title
        # Отчёт Рейтинги
        rating = driver.find_element_by_link_text('Отчёт Рейтинги')
        rating.click()
        _ = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'title_gears')))
        title = wait.until(EC.title_is('ЭОР - Rating'))
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Rating" in driver.title

    def test_9eAdmin(self):
        admin = driver.find_element_by_link_text("Администрирование")
        admin.click()
        time.sleep(1)
        # Пользователи
    def test_9fUsers(self):
        users = driver.find_element_by_link_text('Пользователи')
        users.click()
        title = wait.until(EC.title_is('ЭОР - User'))
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'search-a')))
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - User" in driver.title
        # Роли
    def test_9gRole(self):
        users = driver.find_element_by_link_text('Роли')
        users.click()
        title = wait.until(EC.title_is('ЭОР - Role'))
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.ID, 'btn_create_user')))
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Role" in driver.title
        # Привилегии
    def test_9hPrivilege(self):
        users = driver.find_element_by_link_text('Привилегии')
        users.click()
        title = wait.until(EC.title_is('ЭОР - Privilege'))
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        _ = wait.until(EC.presence_of_element_located((By.ID, 'yw0')))
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Privilege" in driver.title
        # Журналы
    def test_9iJournal(self):
        journ = driver.find_element_by_link_text("Журналы")
        journ.click()
        time.sleep(1)
        # Авторизации
    def test_9jLogs(self):
        autor = driver.find_element_by_link_text("Авторизации")
        autor.click()
        title = wait.until(EC.title_is('ЭОР - Logs'))
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        _ = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'dropdown')))
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Logs" in driver.title
        # Обмен данными
    def test_9kData(self):
        autor = driver.find_element_by_link_text("Обмен данными")
        autor.click()
        title = wait.until(EC.title_is('ЭОР - Data'))
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        _ = wait.until(EC.presence_of_element_located((By.ID, 'resetFilters')))
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Data" in driver.title
        # Операции пользователя
    def test_9lOperation(self):
        autor = driver.find_element_by_link_text("Операции пользователя")
        autor.click()
        title = wait.until(EC.title_is('ЭОР - Operation'))
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        _ = wait.until(EC.presence_of_element_located((By.ID, 'resetFilters')))
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        assert "ЭОР - Operation" in driver.title
        # Справочники
    def test_9mDictionary(self):
        dictionary = driver.find_element_by_link_text("Справочники")
        dictionary.click()
        title = wait.until(EC.title_is('ЭОР - Dictionary'))
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Этапы НПА')))
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        # Приложения
    def test_9nApps(self):
        apps = driver.find_element_by_link_text("Приложения")
        apps.click()
        time.sleep(1)
        # Управление iPad ЭОР
    def test_9oIpad(self):
        driv = driver.find_element_by_link_text("Управление iPad ЭОР")
        driv.click()
        title = wait.until(EC.title_is('ЭОР - Ipad'))
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        _ = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Создать релиз')))
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        # Структура данных
    def test_9pStruct(self):
        struc = driver.find_element_by_link_text("Структура данных")
        struc.click()
        time.sleep(1)
        # Управление структурой
    def test_9rAdminStr(self):
        admStr = driver.find_element_by_link_text("Управление структурой")
        admStr.click()
        title = wait.until(EC.title_is('ЭОР - Gii'))
        assert "ЭОР - Gii" in driver.title
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        # Управление хранилищем данных
    def test_9sDatabase(self):
        database = driver.find_element_by_link_text("Управление хранилищем данных")
        database.click()
        title = wait.until(EC.title_is('ЭОР - Database'))
        assert "ЭОР - Database" in driver.title
        assert "500" not in driver.title  # проверка на 500/404 ошибку
        assert "404" not in driver.title
        # Ресурсы ИС
    def test_9tResource(self):
        res = driver.find_element_by_link_text("Ресурсы ИС")
        res.click()
        time.sleep(1)
        #





