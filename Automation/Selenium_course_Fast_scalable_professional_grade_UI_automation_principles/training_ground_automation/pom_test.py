from selenium import webdriver

from training_ground_page import TrainingGroundPage
from trial_page import TrialPage

import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning) 
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Test Setup
driver = webdriver.Chrome(options=options)

# Test
trial_page = TrialPage(driver)
trial_page.go()
trial_page.stone_input.input_text('rock')
trial_page.stone_button.click()


#Training grounds
instruction_page = TrainingGroundPage(driver = browser)
instruction_page.go()
assert instruction_page.button1.text == 'Button1', 'Unexpected button1 text'
browser.quit()


##for training_ground_page.py import:
# instruction_page.type_into_input(test_value)
## instruction_page.click_button_1() 
# text_from_input = instruction_page.get_input_text()
# assert text_from_input == test_value, f'Test Failed: Input did not match expected ({test_value}).'
# print('Test passed!')
