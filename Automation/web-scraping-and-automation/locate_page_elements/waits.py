from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By


url = 'https://booking.com'

browser = webdriver.Chrome()
browser.implicitly_wait(9)
browser.get(url)

dir_EC = dir(EC)
print(dir_EC)

duration = 9
try:
    element = WebDriverWait(browser, duration).until(EC.presence_of_element_located(
    (By.CLASS_NAME, 'bui-title__text') 
))
except TimeoutException as e:
    print('Loading Exceeds Delay Time')
else:
    print(element.get_attribute('innerHTML'))
