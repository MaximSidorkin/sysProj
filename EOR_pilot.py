import time

from selenium import webdriver
from selenium.webdriver.common.by import By                             # mb is not right
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait               # mb is not right

driver = webdriver.Firefox()
driver.get("http://dev.eor.gosapi.ru/")
assert "Login" in driver.title
elem = driver.find_element_by_id("LoginForm_username")
elem.send_keys("Ipad")

elem = driver.find_element_by_id("LoginForm_password")
elem.send_keys("ipad")
elem.send_keys(Keys.RETURN)

time.sleep(3)
assert "ЭОР" in driver.title
menu = driver.find_element_by_css_selector("i.entypo-menu")
menu.click()

time.sleep(4)
allpj = driver.find_element_by_link_text("Все проекты")
allpj.click()

time.sleep(3)
assert "ЭОР - Checkpoint" in driver.title
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID,'create-cp')))   #очень хороший пример ПРАВИЛЬНОЙ задержки! Сам же писал его!

btn1 = driver.find_element_by_id("create-cp")                           #btn1 = "Создать"  блок
btn1.click()

elemTitle = wait.until(EC.element_to_be_clickable((By.ID,'Checkpoint_TITLE')))  #test
elemTitle = driver.find_element_by_id("Checkpoint_TITLE")
elemTitle.send_keys("Создал Selenium")

btn2 = driver.find_element_by_name("yt0")                               #btn2 = "Создать"   подтвердить создание блока
btn2.click()
#автотест создал блок
#убери слипы! кошмар же!
btn1.send_keys(Keys.F5)                                                 #обновить страницу
assert "500" not in driver.title                                        #проверка на 500 ошибку