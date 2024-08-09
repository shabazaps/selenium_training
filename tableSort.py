# https://rahulshettyacademy.com/seleniumPractise/#/offers

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

driver.implicitly_wait(2)

driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()

vegWebElement = driver.find_elements(By.XPATH,"//tr/td[1]")

veggie_List = []
for i in vegWebElement:
    veggie_List.append(i.text)

originalVegList = veggie_List.copy()

veggie_List.sort()

assert veggie_List==originalVegList

for i in originalVegList:
    print(i)