from threading import activeCount
from unicodedata import category
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas
from datetime import datetime
from time import sleep

def main(currency):

    url = 'https://www.tradingview.com/markets/cryptocurrencies/prices-all/'

    options_ = webdriver.ChromeOptions()
    options_.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    +"AppleWebKit/537.36 (KHTML, like Gecko)"
    +"Chrome/87.0.4280.141 Safari/537.36")

    browser = webdriver.Chrome(options=options_)

    browser.implicitly_wait(3)
    browser.maximize_window()

    browser.get(url)

    dateTimeObj = datetime.now()
    date_ = str(dateTimeObj.year)  + str('{:02d}'.format(dateTimeObj.month)) + str('{:02d}'.format(dateTimeObj.day)) + '_' + str('{:02d}'.format(dateTimeObj.hour)) + '-' + str('{:02d}'.format(dateTimeObj.minute))

    a = browser.execute_script('return navigator.userAgent')
    print('User agent: ')
    print(a)


    active_currency = browser.find_element(By.XPATH, '//span[contains(@class, "modeTitle-3iGYBWzh")]')
    if active_currency == currency:
        pass
    else:
        browser.find_element(By.XPATH, '//input[@type="checkbox"]').click()


    xlwriter = pandas.ExcelWriter('tradingViewCrypto_' + f'{date_}' + '.xlsx')
    categories = browser.find_elements(By.XPATH, '//div[starts-with(@class, "item-EE_m_Lmj")]')


    for category in categories:
        try:    
            browser.find_element(By.XPATH, f'//div[text()="{category.text}"]').click()
            sleep(2)
        except ElementNotInteractableException:
            pass

        load_more = True
        while load_more:
            try:
                browser.find_element(By.XPATH, '//span[@class="tv-load-more__btn"]').click()
                sleep(1.5)
            except ElementNotInteractableException:
                load_more = False


        df = pandas.read_html(browser.page_source)[1]
        # print(df)
        df.to_excel(xlwriter, sheet_name=category.text, index=False)
        
    xlwriter.save()
    browser.quit()


if __name__ == '__main__':
    currency = 'BTC'
    main(currency)
    
