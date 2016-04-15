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

assert "ЭОР" in driver.title
menu = driver.find_element_by_css_selector("i.entypo-menu")
menu.click()

time.sleep(4)
allpj = driver.find_element_by_link_text("Все проекты")
allpj.click()

assert "ЭОР - Checkpoint" in driver.title
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID,'create-cp')))

#time.sleep(5)
btn1 = driver.find_element_by_id("create-cp")
btn1.click()
