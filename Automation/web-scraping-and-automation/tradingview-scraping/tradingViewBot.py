from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# import selenium
from selenium.webdriver.common.action_chains import ActionChains
import pandas
from datetime import datetime


urls = [
    'https://www.tradingview.com/markets/stocks-usa/market-movers-large-cap/',
    # 'https://www.tradingview.com/markets/stocks-usa/market-movers-active/'
]

browser = webdriver.Chrome()
browser.implicitly_wait(3)
browser.maximize_window()

for url in urls:
    browser.get(url)

dateTimeObj = datetime.now()
date_ = str(dateTimeObj.year)  + str('{:02d}'.format(dateTimeObj.month)) + str('{:02d}'.format(dateTimeObj.day)) + '_' + str('{:02d}'.format(dateTimeObj.hour)) + '-' + str('{:02d}'.format(dateTimeObj.minute))

file_base_name = url.split('/')[-2]
print(f'Scraping {url}')

xlwriter = pandas.ExcelWriter(file_base_name + '_' + '{date_}'.format(date_ = date_) + '.xlsx')


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
        
        df = pandas.read_html(browser.page_source)[1]
        # df.replace('-', '', inplace=True)
        df.to_excel(xlwriter, sheet_name=category, index=False)
        
    except (NoSuchElementException, TimeoutException):
        print(f'Report {category} is not found')
        continue
    
    xlwriter.save()
    
# browser.quit()