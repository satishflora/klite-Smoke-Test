import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.utils import ChromeType
from Config.config import TestData


@pytest.fixture(params=["chrome"], scope='function')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(service=Service(executable_path=TestData.CHROME_EXECUTABLE_PATH))
        # chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
        # chrome_options = Options()
        # options = [
        #     "--headless",
        #     "--disable-gpu",
        #     "--window-size=1920,1200",
        #     "--ignore-certificate-errors",
        #     "--disable-extensions",
        #     "--no-sandbox",
        #     "--disable-dev-shm-usage"
        # ]
        # for option in options:
        #     chrome_options.add_argument(option)
        # web_driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        web_driver.implicitly_wait(10)
        web_driver.delete_all_cookies()
        web_driver.maximize_window()
        web_driver.get(TestData.BASE_URL)
        request.cls.driver = web_driver
        yield
        web_driver.quit()
