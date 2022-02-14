from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

url = 'https://booking.com'

browser = webdriver.Chrome()
browser.get(url)

browser.window_handles

browser.execute_script('window.open("https://news.ycombinator.com/login?goto=news")')
print(browser.current_window_handle)

browser.current_window_handle

browser.switch_to.window(browser.window_handles[1])
browser.title

browser.switch_to.window(browser.window_handles[0])


browser.execute_script('window.scrollBy(0, 100)')

element = browser.find_element(By.XPATH, '//h2[text()="Destinations we love"]')
element.rect
element.location
element.size

browser.execute_script('window.scrollTo(0, {0})'.format(element.rect['y']))
