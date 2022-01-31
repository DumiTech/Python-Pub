from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://techstepacademy.com/training-ground")

input1_css_locator = 'input[id="ipt1"]'
button4_xpath_locator = '//button[@id="b4"]'

#Assign elements
input1_el = browser.find_element_by_css_selector(input1_css_locator)
btn4_el = browser.find_element_by_xpath(button4_xpath_locator)

#Manipulate elements
input1_el.send_keys('Python The King')
btn4_el.click()

browser.quit()