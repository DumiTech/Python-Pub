from selenium import webdriver

import selenium
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning) 

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome(options=options)
browser.get("https://techstepacademy.com/trial-of-the-stones")


#Riddle of Stone
stone_input = browser.find_element_by_css_selector('input[id="r1Input"]')
stone_btn = browser.find_element_by_xpath('//button[@id="r1Btn"]')
stone_input.send_keys('rock')
stone_btn.click()


#Riddle of Secrets
password_input = browser.find_element_by_css_selector('input[id="r2Input"]')
password = browser.find_element_by_css_selector("div#passwordBanner > h4").text
input2_btn = browser.find_element_by_xpath('//button[@id="r2Butn"]')

password_input.send_keys(password)
input2_btn.click()


#The Two Merchants
richest_merchant_input = browser.find_element_by_css_selector('input[id="r3Input"]')
richest_merchant = browser.find_element_by_xpath('//p[text()="3000"] /.. /span').text
richest_merchant_btn = browser.find_element_by_xpath('//button[@id="r3Butn"]')

richest_merchant_input.send_keys(richest_merchant)
richest_merchant_btn.click()

#Checking the answers
check_answers_btn = browser.find_element_by_xpath('//button[@id="checkButn"]')
check_answers_btn.click()

#Verifying
trial_complete_msg = browser.find_element_by_id('trialCompleteBanner')
assert trial_complete_msg.text == 'Trial Complete'
