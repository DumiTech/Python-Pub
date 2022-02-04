from selenium import webdriver
from selenium.webdriver.common.by import By


class TrainingGroundPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://techstepacademy.com/training-ground'

    def go(self):
        self.driver.get(self.url)

    def type_into_input(self, text):
        intake = self.driver.find_element(By.ID,'ipt1')
        intake.clear()
        intake.send_keys(text)
        return None

    def get_input_text(self):
        intake = self.driver.find_element(By.ID,'ipt1')
        element_text = intake.get_attribute('value')
        return element_text

    def click_button_1(self):
        button = self.driver.find_element(By.ID, 'b1')
        button.click()
        return None