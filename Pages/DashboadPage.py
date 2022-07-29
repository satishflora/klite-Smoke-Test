from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Config.config import TestData
from selenium.webdriver import ActionChains

class DashboardPage(BasePage):

    """By Locators"""
    Bucket1_label = (By.XPATH, "//div[@class='bucketList'][1]/span")
    Bucket1_arrow = (By.XPATH, "//div[@class='bucketList'][1]//span[@class='ant-select-arrow']")

    """Constructor of the configuration page class"""
    def __init__(self, driver):
        super().__init__(driver)

    def Bucket1_lable_displaying(self):
        return self.is_visible(self.Bucket1_label)

    def Select_Bucket_1(self, bucket1_name):
        Bucket1 = self.driver.find_element_by_xpath("//div[@class='bucketList'][1]//span[@class='ant-select-arrow']")
        self.do_click_by_action(Bucket1)
        bucket1_list = self.driver.find_elements_by_xpath("//div[@class='rc-virtual-list']//div[@class='ant-select-item-option-content']")
        if len(bucket1_list) != 0:
         for i in bucket1_list:
            print(i.text)
            if i.text.__eq__(bucket1_name):
                i.click()
        else:
            print("Bucket list is empty")











