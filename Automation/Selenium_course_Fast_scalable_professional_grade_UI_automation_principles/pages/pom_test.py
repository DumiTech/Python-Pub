from selenium import webdriver

from training_ground_page_v2 import TrainingGroundPage

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Test Setup
browser = webdriver.Chrome(options=options)
test_value = 'well done'

# Test
instruction_page = TrainingGroundPage(driver = browser)
instruction_page.go()
assert instruction_page.button1.text == 'Button1'
instruction_page.button1.click()

browser.quit()



##for training_ground_page.py import:
# instruction_page.type_into_input(test_value)
## instruction_page.click_button_1() 
# text_from_input = instruction_page.get_input_text()
# assert text_from_input == test_value, f'Test Failed: Input did not match expected ({test_value}).'
# print('Test passed!')
