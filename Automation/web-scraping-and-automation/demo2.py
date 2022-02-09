from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


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

# browser.refresh()
# browser.back()
# browser.forward()

# w, h = browser.get_window_size().values()
# browser.maximize_window()
# browser.minimize_window()
# browser.set_window_size(1936, 1056)

action_chains = ActionChains(browser)
action_chains.key_down(Keys.CONTROL).send_keys('V').key_up(Keys.CONTROL).perform()

xpath_string = '//*[@id="quote-nav"]/ul/li[2]/a/span'
element = browser.find_element(By.XPATH, xpath_string)

action_chains.move_to_element(element).click().perform()


browser.quit()