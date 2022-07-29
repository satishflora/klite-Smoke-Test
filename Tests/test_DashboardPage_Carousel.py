from Pages.DashboadPage import DashboardPage
from Pages.IndicesPage import IndicesPage
from Pages.Page404 import Page404
from Tests.Base import BaseTest
from Pages.LoginPage import LoginPage
from Pages.ConfigurationPage import ConfigurationPage
from Config.config import TestData

class Test_Carousel(BaseTest):

  def test_carousel_loaded_with_images_successfully(self):
      self.configpage = ConfigurationPage(self.driver)
      self.loginpage = LoginPage(self.driver)
      self.configpage.click_on_getStarted_button()
      self.loginpage.do_login(TestData.USERNAME, TestData.PASSWORD)
      self.indicespage = IndicesPage(self.driver)
      self.indicespage.index_pattern(TestData.INDEXPATTERN)
      self.indicespage.image_key_field(TestData.IMAGEKEYFIELD)
      self.indicespage.continue_button_click()
      self.dashboard = DashboardPage(self.driver)
      self.dashboard.Select_Bucket_1(TestData.BUCKET1_NAME)




