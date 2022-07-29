import time

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

""" This class is the parent class of all classes"""

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def do_click_by_action(self, by_locator):
        action = ActionChains(self.driver)
        action.click(on_element=by_locator)
        action.perform()

