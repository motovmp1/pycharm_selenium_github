# This is a github selenium with pycharm - Test all elements for second time
# This is a implicit wait into selenium

# *** Import Settings ***

import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# *** Test Case ***
driver = webdriver.Firefox()

driver.get("http://testautomationpractice.blogspot.com/")
# apply to all elements inside the page
driver.maximize_window()
driver.implicitly_wait(6)

# This is a title of the page
time.sleep(1)
print(driver.title)

# This is get URL of the page
time.sleep(1)
print(driver.current_url)

# *******************  Test Case ***************************

driver.find_element_by_xpath("//button[contains(text(),'Click Me')]").click()
time.sleep(5)
# switch command to accepted # dismiss can be used
driver.switch_to_alert().accept()
time.sleep(5)

message = driver.find_element_by_xpath("//p[@id='demo']").text
print(message)

assert message == "You pressed OK!"



# ********************  End Test Case  **********************

#  ****************  Close Setup ********************
# This is close only one window navigator
time.sleep(5)
print("Finished Testing running....")
driver.close()
