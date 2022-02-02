from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.select import Select

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome(options=options)
browser.get("https://techstepacademy.com/training-ground")

# print("Before alert")
# WebDriverWait(browser).until(alert_is_present())
# print("After alert")

#webelement:
sell = browser.find_element_by_id("sel1")
my_select = Select(sell)