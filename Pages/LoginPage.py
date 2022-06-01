from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class LoginPage(BasePage):

    """By Locators"""
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    LOGIN_TEXT = (By.XPATH, "//div[@class='loginHead']/h1")
    MESSAGE = (By.XPATH, "//div[@class='ant-notification ant-notification-topRight']//div[@class='ant-notification-notice-message']")

    """Constructor of the login page class"""
    def __init__(self, driver):
        super().__init__(driver)

    """this is used to check the login page header text"""
    def is_login_header_text_displaying(self):
        return self.get_element_text(self.LOGIN_TEXT)

    """ this is used to login to app """
    def do_login(self, username, password):
        self.do_send_keys(self.USERNAME, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)

    def check_message_diplaying(self):
        return self.get_element_text(self.MESSAGE)


