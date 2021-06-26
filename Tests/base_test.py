import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Configs import CHROME_DRIVER_PATH

class BaseTest(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument("--test-type")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-first-run")
        chrome_options.add_argument("--no-default-browser-check")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH, options=chrome_options)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
