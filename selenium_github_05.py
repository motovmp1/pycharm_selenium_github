# This is a github selenium with pycharm - Test all elements for second time
# This is a implicit wait into selenium

# *** Import Settings ***

import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# *** Test Case ***


driver = webdriver.Chrome(executable_path="/home/elsys/Documents/geckodriver_026/chromedriver")

driver.get("https://www.expedia.com/")
time.sleep(1)
driver.maximize_window()
driver.implicitly_wait(10)

# This is a title of the page
time.sleep(2)
print(driver.title)

# This is get URL of the page
time.sleep(1)
print(driver.current_url)

# flight button
driver.find_element_by_xpath("//button[@id='tab-flight-tab-hp']").click()

# from field
time.sleep(2)
driver.find_element_by_xpath("//input[@id='flight-origin-hp-flight']").click()
time.sleep(3)

driver.find_element_by_xpath("//input[@id='flight-origin-hp-flight']").send_keys("NYC")

time.sleep(3)
driver.find_element_by_xpath("//input[@id='flight-destination-hp-flight']").click()

time.sleep(3)
driver.find_element_by_xpath("//input[@id='flight-destination-hp-flight']").send_keys("SFO")

time.sleep(3)
driver.find_element_by_xpath("//input[@id='flight-departing-hp-flight']").send_keys("04/20/2020")

time.sleep(2)
driver.find_element_by_xpath("//input[@id='flight-returning-hp-flight']").send_keys(Keys.CONTROL + "a")
time.sleep(3)
driver.find_element_by_xpath("//input[@id='flight-returning-hp-flight']").send_keys("05/20/2020")

time.sleep(3)
driver.find_element_by_xpath("//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click()


# This is a explicit waiting in selenium
wait = WebDriverWait(driver, 15)

button_stop = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='changeOptionFilter-0']")))
button_stop.click()


# close all navigator
time.sleep(10)
driver.close()
