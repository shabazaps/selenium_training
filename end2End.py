# import selenium


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
# a[href*='shop'] or //a[contains(@href,'shop')
driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")

# driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
driver.find_element(By.XPATH,"//a[contains(@href,'shop')]").click()
items= driver.find_elements(By.CLASS_NAME,"card")

for i in items:
    product = (i.find_element(By.XPATH,"//div/h4/a")).text
    if product == "iphone X":
        driver.find_element(By.XPATH,"//button[@class = 'btn btn-info']").click()
        break
# time.sleep(4)

driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()

# time.sleep(2)

driver.find_element(By.XPATH,"//input[@id='country']").send_keys("ind")
wait= WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
# time.sleep(2)
driver.find_element(By.XPATH,"//label[@for='checkbox2']").click()
# time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
# time.sleep(2)

alert = (driver.find_element(By.CSS_SELECTOR,"[class='alert alert-success alert-dismissible']")).text
assert "Success!" in alert

driver.close()