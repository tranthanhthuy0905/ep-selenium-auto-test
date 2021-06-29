import os
import logging
import unittest
from datetime import datetime
from selenium import webdriver

from Configs import CHROME_DRIVER_PATH, LOG_FILE_PATH
from Tests.utils import APIService

class BaseTest(unittest.TestCase, APIService):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument("--test-type")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-first-run")
        chrome_options.add_argument("--no-default-browser-check")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH, options=chrome_options)
        # logging.basicConfig(filename=os.path.join(LOG_FILE_PATH, str(datetime.now())),
        #                     filemode='a',
        #                     format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
        #                     datefmt='%H:%M:%S',
        #                     level=logging.INFO) 

    def clear_test_instances(self):
        # self.delete_s3_buckets()
        self._call_api_delete_instance()

    def tearDown(self):
        self.clear_test_instances()
        self.driver.quit()
        print("Test completed")

if __name__ == "__main__":
    unittest.main()
