"""
1 - launch browser
2 - verify home page title
3 - verify login
4 - close browser

setupclass() - ONly one time in the begin
teardown() - only one time in the end

this is a command line that we need to use for test and html report
python3 test_case_orangehtml.py

"""

from selenium import webdriver
import unittest
import HtmlTestRunner
import time


class OrangeHtml(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        time.sleep(1)
        cls.driver.implicitly_wait(5)

    def test_home_page_title(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/%22")
        time.sleep(1)
        title_page = self.driver.title
        print("")
        print(f'This is a title of the page: {title_page}')
        self.assertEqual("OrangeHRM", self.driver.title, "web page title is not match")

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/%22")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        time.sleep(1)
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        time.sleep(1)
        self.driver.find_element_by_name("Submit").click()
        time.sleep(2)
        invalid_check = self.driver.find_element_by_xpath("//span[@id='spanMessage']").text
        print(f'This is a label for invalid text: {invalid_check}')
        self.assertEqual("Invalid credentials", invalid_check, "Login panel not safe")

    @classmethod
    def tearDownClass(cls):
        print("")
        print("Closing browser")
        time.sleep(4)
        cls.driver.close()
        print("Testing is finished...")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/elsys/PycharmProjects'
                                                                  '/pycharm_selenium_github/report_html'))
