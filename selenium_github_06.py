# This is a github selenium with pycharm - Test all elements for second time
# This is a implicit wait into selenium

# *** Import Settings ***

import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

# Need to use elements, please check
input_boxes = driver.find_elements_by_class_name('text_field')
print(f'This is boxes in the page: ', (len(input_boxes)))

driver.find_element_by_id('RESULT_TextField-1').send_keys("Vinicius Miranda")
time.sleep(1)

driver.find_element_by_id('RESULT_TextField-2').send_keys('de Pinho')

driver.find_element_by_id('RESULT_TextField-3').send_keys('19-989490069')

time.sleep(5)

# This is close only one window
print("Finished Testing running....")
driver.close()
