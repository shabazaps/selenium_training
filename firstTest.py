# Testing this Website: https://rahulshettyacademy.com/angularpractice/

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time
driver=webdriver.Chrome()

driver.maximize_window()

# name
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME,"name").send_keys("Robert Mathews")
time.sleep(1)

driver.find_element(By.XPATH,"//input[@name='email']").send_keys("netsh.alternative@example.com")
time.sleep(1)

# driver.find_element(By.ID,"exampleInputPassword1").send_keys("netsh.exampleInputPassword")
# Custom CSS_SELECTOR
driver.find_element(By.CSS_SELECTOR,"input[type='password']").send_keys("netsh.exampleInputPassword")
time.sleep(1)

driver.find_element(By.ID,"exampleCheck1").click()
time.sleep(1)

Select(driver.find_element(By.ID, "exampleFormControlSelect1")).select_by_visible_text("Male")
time.sleep(1)

driver.find_element(By.NAME,"inlineRadioOptions").click()
time.sleep(1)

driver.find_element(By.NAME,"bday").send_keys("28-05-2000")
time.sleep(1)

# driver.find_element(By.CLASS_NAME,"btn-success").click()
# Custom EXpath:
driver.find_element(By.XPATH,"//input[@value='Submit']").click()
time.sleep(1)

# driver.find_element(By.XPATH,"//input[@")

sucess_msg=driver.find_element(By.CLASS_NAME,"alert").text

assert "Success" in sucess_msg
