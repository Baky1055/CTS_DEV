import sys
import time

sys.path.append(sys.path[0] + "/....")

import unittest
from time import sleep

from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.loginPage import login_Page
from src.PageObject.Pages.HomePage import cts_home
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

valid_username = "zia"
valid_password = "abc123456AA"

invalid_username = "aedd"
invalid_password = "Abc34562hh"

Blank_username = " "
Blank_password = " "


class test_sign_page(WebDriverSetup):

    def test_sign_in_page(self):

        driver = self.driver
        self.driver.get("http://dev-citizen.ctrends-software.com/#/home")

        log_in_page = login_Page(driver)

        log_in_page.get_sign_in()
        log_in_page.input_user_name(valid_username)
        log_in_page.input_pass_word(valid_password)
        log_in_page.click_login_button()

    # def test_sign_in_with_valid_user_and_pass(self):
    #     driver = self.driver
    #     data = {
    #         "email" : valid_username,
    #         "password" : valid_password
    #     }
    #     signin_helper_valid_user_and_pass(driver,data)
    #     try:
    #         signout_helper(driver)
    #     except NoSuchElementException:
    #         self.fail('Not ok')

# def signin_helper_valid_user_and_pass(driver, row):
#     driver.delete_all_cookies()
#     driver.get("http://dev-citizen.ctrends-software.com/#/home")
#     time.sleep(1)
#     try:
#         log_in_page = login_Page(driver)
#         log_in_page.get_sign_in()
#         log_in_page.input_user_name(valid_username)
#         log_in_page.input_pass_word(valid_password)
#         log_in_page.click_login_button()
#         time.sleep(2)
#
#     except NoSuchElementException:
#         return 0
#
# def signout_helper(driver):
#     driver.get("http://dev-citizen.ctrends-software.com/#/")
#     # logout_page = login_Page(driver)
#     # logout_page.click_logout_button()
#     nav_top_links = driver.find_elements(By.XPATH, "//li[@class='dropdown']//ul[@class='dropdown-menu']")
#
#     signout = Select(nav_top_links)
#     signout.s
#         # nav_top_links.find_element(By.XPATH, "//a[normalize-space()='Logout']")
#     signout.click()
#
#     time.sleep(1)
#
# if __name__ == '__main__':
#     unittest.main()


