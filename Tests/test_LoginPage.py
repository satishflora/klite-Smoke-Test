from Pages.IndicesPage import IndicesPage
from Tests.Base import BaseTest
from Pages.LoginPage import LoginPage
from Pages.ConfigurationPage import ConfigurationPage
from Config.config import TestData


class Test_Login(BaseTest):
#login test cases
    def test_login_page_opening_successfully(self):
        self.configpage = ConfigurationPage(self.driver)
        self.loginpage = LoginPage(self.driver)
        self.configpage.click_on_getStarted_button()
        self.headertext = self.loginpage.is_login_header_text_displaying()
        assert self.headertext == 'Please login to Fortress IQ'

    def test_user_login_to_app_successfully(self):
        self.configpage = ConfigurationPage(self.driver)
        self.loginpage = LoginPage(self.driver)
        self.configpage.click_on_getStarted_button()
        self.loginpage.do_login(TestData.USERNAME, TestData.PASSWORD)
        self.indicespage = IndicesPage(self.driver)
        self.welcome_text = self.indicespage.check_welecom_text()
        assert "Welcome" in self.welcome_text

    def test_login_page_not_be_accessible_after_login(self):
        self.configpage = ConfigurationPage(self.driver)
        self.loginpage = LoginPage(self.driver)
        self.configpage.click_on_getStarted_button()
        self.login_url = self.driver.current_url
        self.loginpage.do_login(TestData.USERNAME, TestData.PASSWORD)
        self.indicespage = IndicesPage(self.driver)
        self.welcome_text = self.indicespage.check_welecom_text()
        assert "Welcome" in self.welcome_text
        self.driver.get(self.login_url)
        self.headertext = self.indicespage.check_indices_header_text_displaying()
        assert self.headertext








