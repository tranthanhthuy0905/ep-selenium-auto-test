import os
import time
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import HtmlTestRunner


class S3HomePage(unittest.TestCase):
    cookie = {"name": "user-token",
              "value": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MGQ0MjA2ODViZjgwNjAwMTgwNmUwMTQiLCJuYW1lIjoicXVhbmxoMiIsImlhdCI6MTYyNDY4NTYzMiwiZXhwIjoxNjI0NzcyMDMyfQ.kaqLdj31uva3fejghSGzyQVgOymG2cCBV-AT_vTE06o"}

    base_url = "https://staging-s3.engineering.vng.vn/s3"

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        self.driver.implicitly_wait(10)


    def test_load_homepage(self):
        """
            The homepage should be loaded successfully
        """
        self.driver.get(self.base_url)
        self.driver.add_cookie(self.cookie)
        self.driver.implicitly_wait(10)
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)

        self.assertIn("Engineering Platform | EP", self.driver.title)

        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )






# driver.close()