import sys
sys.path.append(sys.path[0] + "/....")

from selenium.webdriver.common.by import By
from src.PageObject.Locators import Citizen_locator

class cts_home(object):
    def __init__(self, driver):

        self.driver = driver
        self.cts_logo = driver.find_element(By.XPATH, Citizen_locator.Cts_logo_xpath)
        self.login_sign_in = driver.find_element(By.XPATH, Citizen_locator.login_xpath)

    def get_cts_logo(self):
        return self.cts_logo

    def get_sign_in(self):
        return self.login_sign_in