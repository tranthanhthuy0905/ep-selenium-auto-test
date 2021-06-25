import unittest
from selenium import webdriver
from locators.cookies import cookie
from webdriver_manager.chrome import ChromeDriverManager
import time

from configs.base import Config
from locators.sg_locators import SecurityGroupHomeLocators


class BaseTest(unittest.TestCase):
    def setUp(self):
        config = Config()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--test-type")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-first-run")
        chrome_options.add_argument("--no-default-browser-check")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--window-size=1920,1080")


        self.url = self.get_url()
        self.cookie = {
            "name": "user-token",
            "value": self.get_user_token()
        }

        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        self.driver.get(config.EP_CONSOLE_URL)
        self.driver.add_cookie(cookie)
        self.driver.get(config.EP_CONSOLE_URL)
        self.driver.implicitly_wait(15)

    def tearDown(self):
        time.sleep(10)
        self.driver.close()

    def get_user_token(self):
        return SecurityGroupHomeLocators.AUTOTEST_USER_TOKEN

    def get_url(self, service_name = "security_groups"):
        if service_name == 'security_groups':
            return SecurityGroupHomeLocators.EC2_URL


if __name__ == "__main__":
    unittest.main()
