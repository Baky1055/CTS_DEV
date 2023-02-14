import sys
sys.path.append(sys.path[0] + "/....")
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.PageObject.Locators import Citizen_locator


class login_Page(object):
    def __init__(self, driver):

        self.driver = driver

        # self.login_user_name = driver.find_element(By.NAME, Citizen_locator.username_name)
        # self.login_pass_ward = driver.find_element(By.NAME, Citizen_locator.password_name)
        # self.click_login_button = driver.find_element(By.XPATH, Citizen_locator.login_xpath)


    def input_user_name(self):
        return self.login_user_name

    def input_pass_word(self):
        return self.login_pass_ward

    def click_login_button(self):
        return self.click_sign_in_page()