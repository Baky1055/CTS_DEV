import sys
import time

sys.path.append(sys.path[0] + "/....")

import unittest
from time import sleep

from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.SignUpPages import signup_page
from src.PageObject.Pages.HomePage import cts_home
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome import webdriver

from selenium.webdriver.common.by import By


full_name = "Mr Rahim"
User_Name = "Rahim"
Phone_Number = "01234567898"
email = "rahim123@gmail.com"


class Test_Sign_Up(WebDriverSetup):

    def test_sign_up_page(self):

        driver = self.driver
        self.driver.get("http://dev-citizen.ctrends-software.com/#/home")

        Sign_Up_page = signup_page(driver)

        signup_page.get1_sign_in()
        Sign_Up_page.get_signup_click()
        Sign_Up_page.input_fullname(full_name)
        Sign_Up_page.input_username(User_Name)
        Sign_Up_page.input_phone_number(Phone_Number)
        Sign_Up_page.input_email_id(email)



def register_helper(driver, row):
    driver.refresh()
    time.sleep(1)
    try:
        try:


