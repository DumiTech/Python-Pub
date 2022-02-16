from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


url = 'https://jenniferdewalt.com/click_challenge.html'
browser = webdriver.Chrome()
browser.get(url)

action_chains = ActionChains(browser)

start = browser.find_element(By.ID, 'start').click()

for i in range(5000):
    action_chains.double_click().perform()