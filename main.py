import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://dev-citizen.ctrends-software.com/#/home")
driver.maximize_window()

driver.find_element(By.XPATH, "//i[@class='fas fa-sign-in-alt']").click()
driver.find_element(By.NAME, "username").send_keys("zia")
driver.find_element(By.NAME, "password").send_keys("abc123456AA")
driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
# driver.find_element(By.XPATH, "// a[normalize - space() = 'Logout']").click()
time.sleep(2)

nav_top_links = driver.find_element(By.XPATH, "//li[@class='dropdown']")
menu = nav_top_links.find_element(By.XPATH, "//li[@class='dropdown']//ul[@class='dropdown-menu']")
# menu.click()
time.sleep(1)

Signout = menu.find_element(By.XPATH, "//a[normalize-space()='Logout']")
Signout.click()

time.sleep(2)