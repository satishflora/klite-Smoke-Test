import time

from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Config.config import TestData
from Pages.LoginPage import LoginPage

class Page404(BasePage):

    """By Locators"""
    IMAGE_404 = (By.XPATH, "//img[contains(@src,'./fortress-logo-login.png')]")
    GoToLoginButton = (By.PARTIAL_LINK_TEXT, "Go to ")

    """Constructor of the configuration page class"""
    def __init__(self, driver):
        super().__init__(driver)

    def access_non_exist_page(self):
        time.sleep(3)
        self.curr_url = self.driver.current_url
        print(self.curr_url)
        self.wrong_url = self.curr_url + 'test'
        time.sleep(3)
        print(self.wrong_url)
        self.driver.get(self.wrong_url)
        return self.is_visible(self.IMAGE_404)

    def click_go_to_login_button(self):
        self.do_click(self.GoToLoginButton)

    def click_go_to_indices_button(self):
        self.do_click(self.GoToLoginButton)



