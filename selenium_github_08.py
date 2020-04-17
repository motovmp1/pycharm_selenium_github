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

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
# apply to all elements inside the page
driver.implicitly_wait(6)

# This is a title of the page
time.sleep(1)
print(driver.title)

# This is get URL of the page
time.sleep(1)
print(driver.current_url)

element_drp = driver.find_element_by_id("RESULT_RadioButton-9")
drop_list = Select(element_drp)

drop_list.select_by_visible_text("Morning")

time.sleep(3)
drop_list.select_by_index(2)

time.sleep(2)

print(len(drop_list.options))

all_options_label = drop_list.options

for option in all_options_label:
    print(option.text)
    time.sleep(1)

time.sleep(6)

# This is close only one window navigator
print("Finished Testing running....")
driver.close()
