# This is a github selenium with pycharm - Test all elements for second time
# This is a implicit wait into selenium

# *** Import Settings ***

import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# *** Test Case ***
driver = webdriver.Firefox()

driver.get("http://www.newtours.demoaut.com/")
# apply to all elements inside the page
driver.implicitly_wait(6)

# This is a title of the page
time.sleep(1)
print(driver.title)

# This is get URL of the page
time.sleep(1)
print(driver.current_url)

assert "Welcome: Mercury Tours" in driver.title

# This is provide user name
print("name...")
driver.find_element_by_xpath("//input[@name='userName']").send_keys("tutorial")
time.sleep(1)

# This is provide password into field
print("password...")
driver.find_element_by_xpath("//input[@name='password']").send_keys("tutorial")
time.sleep(1)

# This is a login button press
print("Press button")
driver.find_element_by_xpath("//input[@name='login']").click()

time.sleep(1)

timer1 = 0
for timer1 in range(0, 20, 1):
    print(timer1, end=". ", flush=True)
    time.sleep(1)
    if driver.title == "Find a Flight: Mercury Tours:":
        break

second_page = driver.title
print("")
print(second_page)

assert "Find a Flight: Mercury Tours:" in driver.title

time.sleep(5)

# This is close only one window
print("Finished Testing running....")
driver.close()
