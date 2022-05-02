from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from datetime import datetime
import time

urls = [
    'https://www.tradingview.com/markets/stocks-usa/market-movers-all-stocks/',
    'https://www.tradingview.com/markets/stocks-usa/market-movers-high-dividend/',
    'https://www.tradingview.com/markets/stocks-usa/market-movers-large-cap/',
    'https://www.tradingview.com/markets/stocks-usa/market-movers-largest-employers/',
    'https://www.tradingview.com/markets/stocks-usa/market-movers-highest-net-income/',
    'https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/',
    'https://www.tradingview.com/markets/stocks-usa/market-movers-losers/'
]

options_ = webdriver.ChromeOptions()
options_.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
+"AppleWebKit/537.36 (KHTML, like Gecko)"
+"Chrome/87.0.4280.141 Safari/537.36")

browser = webdriver.Chrome(options=options_)

browser.implicitly_wait(3)
browser.maximize_window()


for url in urls:
    browser.get(url)
    file_base_name = url.split('/')[-2]
    # print(file_base_name)
    xlwriter = pd.ExcelWriter(file_base_name + '.xlsx')

    categories = browser.find_elements(By.CLASS_NAME, 'content-vcCjkHCG')

    for category in categories:
        print(f'Processing Report: {category.text}')
        try:
            try:
                browser.find_element(By.XPATH, f'//span[text()="{category.text}"]').click()
                time.sleep(1)
            except ElementNotInteractableException:
                pass
                
            # load_more = True
            # counter = 0 
            # max_counter = 3

            # while load_more:
            #     try:
            #         browser.find_element(By.CLASS_NAME, 'loadButton-59hnCnPW').click()
            #         time.sleep(1)
            #         if counter > max_counter:
            #             load_more = False
            #         counter += 1
            #     except ElementNotInteractableException:
            #         load_more = False

            df = pd.read_html(browser.page_source)[1]
            df.replace('—', '', inplace=True)
            df.to_excel(xlwriter, sheet_name=category.text, index=False)

        except (NoSuchElementException, TimeoutException):
            print(f'Report: {category.text} is not found.')
            continue

    print('Excel file saved at {}'.format(file_base_name + '.xlsx'))
    xlwriter.save()
    print()

browser.quit()