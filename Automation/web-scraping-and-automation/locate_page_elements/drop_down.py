from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException


url = 'https://www.amazon.com'

browser = webdriver.Chrome()
browser.get(url)

element_dd = browser.find_element(By.ID, 'searchDropdownBox')
select = Select(element_dd)

try:
    select.select_by_visible_text('Computers')
except NoSuchElementException:
    print('The item is not visible')
else:
    print('The item was selected succesfully!')


select.select_by_index(10)