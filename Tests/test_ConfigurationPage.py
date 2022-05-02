import pytest
from Tests.Base import BaseTest
from Pages.ConfigurationPage import ConfigurationPage

class Test_Configuration(BaseTest):

    def test_application_url_opening_successfully(self):
        self.configpage = ConfigurationPage(self.driver)
        flag = self.configpage.is_get_started_button_exist()
        assert flag

