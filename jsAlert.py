# https://rahulshettyacademy.com/AutomationPractice/

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
name="Shabaz"
driver.find_element(By.XPATH,"//input[@id='name']").send_keys(name)
driver.find_element(By.XPATH,"//input[@id='alertbtn']").click()

alert = driver.switch_to.alert
time.sleep(2)
print(alert.text)
assert name in alert.text
alert.accept()
time.sleep(2)

driver.find_element(By.XPATH,"//input[@id='confirmbtn']").click()
time.sleep(2)
alert1 = driver.switch_to.alert
print(alert1.text)
alert.dismiss()
time.sleep(2)

