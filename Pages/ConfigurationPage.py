from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Config.config import TestData
from Pages.LoginPage import LoginPage


class ConfigurationPage(BasePage):

    """By Locators"""
    GETSTARTED_BUTTON = (By.ID, "SubmitBtn")

    """Constructor of the configuration page class"""
    def __init__(self, driver):
        super().__init__(driver)

    def open_app_url(self):
        self.driver.maximize_window()
        self.driver.get(TestData.BASE_URL)

    def is_get_started_button_exist(self):
        return self.is_visible(self.GETSTARTED_BUTTON)

    def click_on_getStarted_button(self):
        self.do_click(self.GETSTARTED_BUTTON)


