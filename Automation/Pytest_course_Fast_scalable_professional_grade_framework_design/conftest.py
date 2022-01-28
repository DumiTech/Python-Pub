from pytest import fixture
from selenium import webdriver

import time

@fixture(scope='function')  #or 'session'
def chrome_browser():
    browser = webdriver.Chrome()
    yield browser
    
    time.sleep(5)
    
    # Teardown
    print('I am tearing down this browser')