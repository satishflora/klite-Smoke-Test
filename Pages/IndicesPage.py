import time
from telnetlib import EC

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Pages.BasePage import BasePage
from Config.config import TestData
from selenium.webdriver.common.keys import Keys

class IndicesPage(BasePage):

    """By Locators"""
    INDEX_PATTERN = (By.XPATH, "//div[@class='ant-select-selector']/span[@class='ant-select-selection-search']/input[@id='rc_select_0']")
    HEADER_TEXT = (By.XPATH, "//div[@class='ant-col ant-col-13 user-edit']")
    WELCOME_TEXT = (By.XPATH, "//div[@class='ant-col user-header']")




    """Constructor of the configuration page class"""
    def __init__(self, driver):
        super().__init__(driver)

    def check_welecom_text(self):
        text = self.get_element_text(self.WELCOME_TEXT)
        return text

    def check_indices_header_text_displaying(self):
        return self.is_visible(self.HEADER_TEXT)

    def select_index_patten(self):
        self.driver.find_elements_by_xpath("//div[@class='ant-select-selector']/span[@class='ant-select-selection-search']/input")[0].click()
        self.driver.find_elements_by_xpath("//div[@class='ant-select-selector']/span[@class='ant-select-selection-search']/input")[0].send_keys("event_logs")

    def select_image_key(self):
        self.driver.find_elements_by_xpath("//div[@class='ant-select-selector']/span[@class='ant-select-selection-search']/input")[1].send_keys("screenshot_key")

    def index_pattern(self, indexname):
       indexpattern = self.driver.find_elements_by_xpath("//div[@class='ant-select-selector']/span[@class='ant-select-selection-search']/input")[0]
       action = ActionChains(self.driver)
       action.click(on_element=indexpattern)
       action.send_keys(indexname)
       action.pause(3)
       action.perform()
       indexes = self.driver.find_elements_by_xpath("//div[@class='rc-virtual-list-holder-inner']/div[starts-with(@class,'ant-select-item ant-select-item-option')]")
       for i in indexes:
          #print(i.text)
           if i.text.__eq__(indexname):
               i.click()


    def image_key_field(self, imagekeyname):
        imagekey = self.driver.find_elements_by_xpath("//div[@class='ant-select-selector']/span[@class='ant-select-selection-search']/input")[1]
        action = ActionChains(self.driver)
        action.click(on_element=imagekey)
        action.send_keys(imagekeyname)
        action.pause(3)
        action.perform()
        indexes = self.driver.find_elements_by_xpath("//div[@class='rc-virtual-list-holder-inner']/div[starts-with(@class,'ant-select-item ant-select-item-option')]")
        for i in indexes:
            print(i.text)
            if i.text.__eq__(imagekeyname):
                i.click()

    def continue_button(self):
        return self.driver.find_element_by_xpath("//button[@type='button']").get_property('disabled')

    def continue_button_click(self):
        self.driver.find_element_by_xpath("//button[@type='button']").click()

