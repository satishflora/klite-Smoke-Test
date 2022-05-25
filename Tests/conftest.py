import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Config.config import TestData


@pytest.fixture(params=["chrome"], scope='function')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(service=Service(executable_path=TestData.CHROME_EXECUTABLE_PATH))
        #web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        web_driver.implicitly_wait(10)
        web_driver.delete_all_cookies()
        web_driver.maximize_window()
        web_driver.get(TestData.BASE_URL)
        request.cls.driver = web_driver
        yield
        web_driver.quit()

