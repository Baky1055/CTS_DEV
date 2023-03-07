import sys
import time

sys.path.append(sys.path[0] + "/....")

import unittest
from time import sleep

from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.loginPage import login_Page
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
