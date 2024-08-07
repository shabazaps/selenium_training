# Using Different CSS_Selector and Xpath

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.CSS_SELECTOR,"input[name='username']").send_keys("Admin")
driver.find_element(By.CSS_SELECTOR,"input[type='password'").send_keys("admin123")

driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
time.sleep(4)

# driver.find_element(By.CLASS_NAME,"oxd-text").click()

# Select(driver.find_element(By.ID, "exampleFormControlSelect1")).select_by_visible_text("Claim")
driver.find_element(By.LINK_TEXT,"Claim").click()
# driver.find_element(By.XPATH,"(//button[@type='button'])[6]").click()

driver.find_element(By.XPATH,"//button[contains(., 'Assign Claim')]").click()

driver.find_element(By.XPATH,"//input[contains(@placeholder, 'Type for hints..')]").send_keys("Shabaz")
time.sleep(2)
driver.close()
