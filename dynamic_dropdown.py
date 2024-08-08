# Using Dynaimc DropDown

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Uni")
driver.implicitly_wait(2)
uni = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")

# for i in uni:
#     print(i.text)

for i in uni:
    if i.text == "United Arab Emirates":
        i.click()
        break
# driver.find_element(By.XPATH,"//input[@type='text']")
arab= driver.find_element(By.XPATH,"//input[@type='text']").get_attribute("value")
assert arab == "United Arab Emirates"
print(arab)
time.sleep(4)
driver.close()
