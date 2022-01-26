from pytest import fixture
from selenium import webdriver

import time


@fixture(params=[webdriver.Chrome, webdriver.Opera])
def browser(request):
    driver = request.param
    drvr = driver()
    yield drvr
    drvr.quit()
    time.sleep(10)
