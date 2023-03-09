import sys
sys.path.append(sys.path[0] + "/....")
from selenium import webdriver
from selenium.webdriver.common.by import By
from src.PageObject.Locators import Citizen_locator


class signup_page(object):
    def __init__(self, driver):

        self.driver = driver

    def get1_sign_in(self):
        self.driver.find_element(By.XPATH, Citizen_locator.sign_in_xpath).click()

    def get_signup_click(self):
        self.driver.find_element(By.CLASS_NAME,Citizen_locator.signup_className).click()

    def input_fullname(self,fullname):
        self.driver.find_element(By.NAME,Citizen_locator.fullname_Name).send_keys(fullname)

    def input_username(self,username):
        self.driver.find_element(By.NAME,Citizen_locator.username_name).send_keys(username)

    def input_phone_number(self,phonenumber):
        self.driver.find_element(By.NAME,Citizen_locator.PhoneNumber_Name).send_keys(phonenumber)

    def input_email_id(self,email):
        self.driver.find_element(By.NAME,Citizen_locator.Email_Name).send_keys(email)
