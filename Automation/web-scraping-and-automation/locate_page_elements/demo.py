from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

###Find element by name
url = 'https://news.ycombinator.com/login?goto=news'

browser = webdriver.Chrome()
browser.get(url)

username = browser.find_element(By.NAME, 'acct')
password = browser.find_element(By.NAME, 'pw')
login_button = browser.find_element(By.XPATH, '/html/body/form[1]/input[2]')

username.clear()
username.send_keys('John Doe')

password.clear()
password.send_keys('1234')

login_button.click()
### Find element by class

url1 = 'https://finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-srch'
class_name = "nr-applet-nav-item"

browser.get(url1)

accept_consent = browser.find_elements(By.XPATH, '//*[@id="consent-page"]/div/div/div/form/div[2]/div[2]/button')
accept_consent[0].click()

element_class1 = browser.find_element(By.CLASS_NAME, class_name)
element_class2 = browser.find_elements(By.CLASS_NAME, class_name)

# print(element_class1)

# print(element_class2)
print(len(element_class2))

###Find element by hyperlink & partial hyperlink text

element_hyper = browser.find_element(By.LINK_TEXT, "Historical Data")
element_partial_hyper = browser.find_element(By.PARTIAL_LINK_TEXT, 'Historical')

element_hyper.click()
browser.back()

###Tag name

browser.get(url)
element_tag_head = browser.find_elements(By.TAG_NAME, 'head')

element_tag_link = browser.find_elements(By.TAG_NAME, 'link')

for link in element_tag_link:
    print(link.text)
    
len(element_tag_link)


###CSS Selector

browser.get('https://www.tripadvisor.com/#')
element_css = browser.find_elements(By.CSS_SELECTOR, 'span.WlYyy.bcUBw')

###xpath

element_xpath = browser.find_element(By.XPATH, '//*[@id="lithium-root"]/header/div/nav/div[2]/a[3]/span')
print(element_xpath.text)