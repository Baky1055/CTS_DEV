import sys
sys.path.append(sys.path[0] + "/....")

import unittest
from time import sleep

from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.loginPage import login_Page
from src.PageObject.Pages.HomePage import cts_home

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

<<<<<<< HEAD
        # cts_home_page = cts_home(driver)
        # cts_home_page.login_sign_in.click()
=======
        log_in_page = login_Page(driver)

        log_in_page.get_sign_in()
        log_in_page.input_user_name(valid_username)
        log_in_page.input_pass_word(valid_password)
        log_in_page.click_login_button()

>>>>>>> Initial commit
