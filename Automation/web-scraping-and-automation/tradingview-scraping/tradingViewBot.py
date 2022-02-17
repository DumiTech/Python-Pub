from turtle import pd
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time
import datetime

urls = [
    'https://www.tradingview.com/markets/stocks-usa/market-movers-large-cap/',
    # 'https://www.tradingview.com/markets/stocks-usa/market-movers-active/'
]

browser = webdriver.Chrome()
browser.implicitly_wait(9)
browser.maximize_window()

for url in urls:
    browser.get(url)

file_base_name = url.split('/')[-2]
print(f'Scraping {url}')

xlwriter = pd.ExcelWriter(file_base_name + '.xlsx')


categories = ['Overview', 'Performance', 'Valuation', 'Dividends', 'Margins', 'Income Statement', 'Balance Sheet', 
              'Oscillators', 'Trend-Following']


for category in categories:
    print(f'Processing report: {category}')
    
    try: 
        element_tab = browser.find_element(By.XPATH, f'//div[text()="{category}"]')
        try:
            element_tab.click()
        except ElementNotInteractableException:
            continue
        
        time.sleep(2)
        
        df = pd.read_html(browser.page_source)[1]
        # df.replace('-', '', inplace=True)
        df.to_excel(xlwriter, sheet_name=category, index=False)
        
    except (NoSuchElementException, TimeoutException):
        print(f'Report {category} is not found')
        continue
    
    xlwriter.save()
    
# browser.quit()