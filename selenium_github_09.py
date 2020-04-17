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

driver.get("http://www.newtours.demoaut.com/")
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


links_table = driver.find_elements_by_tag_name("a")
print(f' This is links in the page : ', (len(links_table)))

for index, link in enumerate(links_table):
    print(index, link.text)
    time.sleep(0.2)

print("Button register has been press....")
driver.find_element_by_partial_link_text("REGISTER").click()

# ********************  End Test Case  **********************

#  ****************  Close Setup ********************
# This is close only one window navigator
time.sleep(5)
print("Finished Testing running....")
driver.close()
