from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Config.config import TestData

class DashboardPage(BasePage):

    """By Locators"""
    Bucket1 = (By.XPATH, "//div[@class='bucketList'][1]/span")


    """Constructor of the configuration page class"""
    def __init__(self, driver):
        super().__init__(driver)

    def Bucket1_lable_displaying(self):
        return self.is_visible(self.Bucket1)


