# https://rahulshettyacademy.com/seleniumPractise/#/

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions

import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(2)
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@type='search']").send_keys("ro")
# vegs = driver.find_elements(By.CSS_SELECTOR,".search-keyword")\

# Lists are exceptional, so we have to put time.sleep here.
time.sleep(2)
vegs = driver.find_elements(By.XPATH,"//div[@class='products']/div")

item_list = driver.find_elements(By.XPATH,"//h4[@class='product-name']")
for i in item_list:
    print(i.text)

#Chaining parent with child
for i in vegs:
    i.find_element(By.XPATH,"div/button").click()
    # time.sleep(1)

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
# time.sleep(2)

prices = driver.find_elements(By.XPATH,"//tr/td[5]/p")
sum=0
for i in prices:
    sum += int(i.text)


total= int(driver.find_element(By.XPATH,"//span[@class='totAmt']").text)
assert sum == total

driver.find_element(By.XPATH,"//input[@class='promoCode']").send_keys("rahulshettyacademy")

driver.find_element(By.XPATH,"//button[@class='promoBtn']").click()
# time.sleep(5)
wait = WebDriverWait(driver,10)
# wait.until(EC.presence_of_element_located((By.XPATH,"//span[@class='promoInfo']")))
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//span[@class='promoInfo']")))

discount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
# print(discount)
assert total >= sum

promo = driver.find_element(By.XPATH,"//span[@class='promoInfo']").text
# print(sum)
# assert promo == "Code applied ..!"

