from Pages.DashboadPage import DashboardPage
from Pages.IndicesPage import IndicesPage
from Pages.Page404 import Page404
from Tests.Base import BaseTest
from Pages.LoginPage import LoginPage
from Pages.ConfigurationPage import ConfigurationPage
from Config.config import TestData

#test
class Test_Page404(BaseTest):

    def test_404_page_displaying_before_login_and_redirected_back_to_login(self):
          self.configpage = ConfigurationPage(self.driver)
          self.configpage.click_on_getStarted_button()
          self.page404 = Page404(self.driver)
          assert self.page404.access_non_exist_page()
          self.page404.click_go_to_login_button()
          self.loginpage = LoginPage(self.driver)
          assert self.loginpage.is_login_header_text_displaying()

    def test_404_page_displaying_after_login_on_indices_and_redirected_back_to_indices(self):
          self.configpage = ConfigurationPage(self.driver)
          self.loginpage = LoginPage(self.driver)
          self.configpage.click_on_getStarted_button()
          self.loginpage.do_login(TestData.USERNAME, TestData.PASSWORD)
          self.page404 = Page404(self.driver)
          assert self.page404.access_non_exist_page()
          self.page404.click_go_to_login_button()
          self.indicespage = IndicesPage(self.driver)
          assert self.indicespage.check_indices_header_text_displaying()

    def test_404_page_displaying_after_login_on_dashboard_and_redirected_back_to_dashboard(self):
         self.configpage = ConfigurationPage(self.driver)
         self.loginpage = LoginPage(self.driver)
         self.configpage.click_on_getStarted_button()
         self.loginpage.do_login(TestData.USERNAME, TestData.PASSWORD)
         self.indicespage = IndicesPage(self.driver)
         self.indicespage.index_pattern(TestData.INDEXPATTERN)
         self.indicespage.image_key_field(TestData.IMAGEKEYFIELD)
         self.indicespage.continue_button_click()
         self.page404 = Page404(self.driver)
         assert self.page404.access_non_exist_page()
         self.page404.click_go_to_login_button()
         self.dashboard = DashboardPage(self.driver)
         assert self.dashboard.Bucket1_lable_displaying()














