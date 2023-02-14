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

<<<<<<< HEAD

    def input_user_name(self):
        return self.login_user_name

    def input_pass_word(self):
        return self.login_pass_ward

    def click_login_button(self):
        return self.click_sign_in_page()
=======
    def get_sign_in(self):
        self.driver.find_element(By.XPATH, Citizen_locator.sign_in_xpath).click()


    def input_user_name(self, username):
        self.driver.find_element(By.NAME, Citizen_locator.username_name).send_keys(username)

    def input_pass_word(self, password):
        self.driver.find_element(By.NAME, Citizen_locator.password_name).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, Citizen_locator.login_xpath)
>>>>>>> Initial commit
