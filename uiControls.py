# https://rahulshettyacademy.com/AutomationPractice/

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

radios= driver.find_elements(By.XPATH,"//input[@type='radio']")

for i in radios:
    if i.get_attribute('value') == 'option2':
        i.click()
        assert i.is_selected()
        break
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

for i in checkboxes:
    if i.get_attribute('value') == 'option3':
        i.click()
        assert i.is_selected()
        break

driver.find_element(By.XPATH,"//input[@autocomplete = 'off']").send_keys("Ind")
driver.implicitly_wait(2)
countries= driver.find_elements(By.XPATH,"//div[@tabindex='-1']")

for i in countries:
    if i.text == 'India':
        i.click()
        break

time.sleep(2)



