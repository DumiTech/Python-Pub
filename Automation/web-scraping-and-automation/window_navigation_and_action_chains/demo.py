from selenium.webdriver import Firefox, Chrome, Edge, safari
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://finance.yahoo.com/'

browser = webdriver.Chrome()
browser.get(url)

accept_consent = browser.find_elements(By.XPATH, '//button')
accept_consent[0].click()

search_id_field = 'yfin-usr-qry'
element_search_field = browser.find_element(By.ID, search_id_field)
# print(element_search_field)
element_search_field.clear()
element_search_field.send_keys('TSLA')
element_search_field.send_keys(Keys.ENTER)

# print(browser.title)
# print(browser.current_url)
# print(browser.page_source)

# browser.quit()