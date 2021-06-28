import requests
import unittest
from selenium import webdriver

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

    def clear_test_instances(self):
        self._call_api_delete_s3_bucket()
        self._call_api_delete_ec2_instance()

    def _call_api_delete_s3_bucket(self):
        pass

    def _call_api_delete_ec2_instance(self):
        pass

    def _call_request_delete(self, url, params, user_token):
        headers = {
            "cookie": f"user-token={user_token}",
            "accept": "application/json"
        }
        r = requests.delete(url, headers=headers, params=params)
        if r.status_code == 200:
            print(f"Succeeded calling {url}")
        else:
            print(f"FAILED calling {url}")
        print(f"Delete response: {r.content}. Params: {params}")


    def tearDown(self):
        self.clear_test_instances()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
