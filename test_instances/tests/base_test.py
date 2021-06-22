import unittest
from selenium import webdriver
from utils.cookies import cookie
import time


class BaseTest(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--test-type")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-first-run")
        chrome_options.add_argument("--no-default-browser-check")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--window-size=1920,1080");
        self.driver = webdriver.Chrome('chromedriver', options=chrome_options)
        self.driver.get('https://console.engineering.vng.vn')
        self.driver.add_cookie(cookie)
        self.driver.get('https://console.engineering.vng.vn')
        self.driver.implicitly_wait(15)

    def tearDown(self):
        time.sleep(10)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
