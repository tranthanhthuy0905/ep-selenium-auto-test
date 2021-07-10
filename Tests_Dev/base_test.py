import os
import time
import logging
import unittest
from datetime import datetime
from selenium import webdriver

from Configs import CHROME_DRIVER_PATH, LOG_FILE_PATH
from Tests.utils import APIService

class BaseTest(unittest.TestCase, APIService):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('--headless')
        chrome_options.add_argument("--test-type")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-first-run")
        chrome_options.add_argument("--no-default-browser-check")
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--window-size=1920,1080")
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH, options=chrome_options)
        # self.driver.set_window_position(x=2050, y=282)
        os.makedirs(LOG_FILE_PATH, exist_ok=True)
        logging.basicConfig(filename=os.path.join(LOG_FILE_PATH, str(datetime.now())),
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.INFO)
        logging.info(f"TEST START: Start testing: {self.__class__.__name__}")

    def clear_test_instances(self):
        pass

    def tearDown(self):
        self.clear_test_instances()
        self.driver.quit()
        logging.info(f"TEST COMPLETE: Test {self.__class__.__name__} completed!\n")

    def keep_trying(self, function, attempts=60, fallback=None, unsatisfactory=None):
        """Continues to try the function without errors for a number of attempts before continuing. This solves
        The problem of Selenium being inconsistent and erroring out because a browser is slow.
        Parameters
        ----------
        assertion : lambda
            A lambda function that should at some point execute successfully.
        attempts : Integer
            The number of attempts to keep trying before letting the test continue
        unsatisfactory : Any
            Value that is unsatisfactory as a return value
        fallback : Any
            The fallback return value if the function did return a satisfactory value within the given
            number of attempts.
        Returns the return value of the function we are trying.
        """
        for i in range(attempts):
            try:
                result = function()
                # It will only return if the assertion does not throw an error
                if (result is not unsatisfactory):
                    return result
            except Exception as e:
                print("wtffff", e)
                pass
            time.sleep(1)  # This makes the function wait a second between attempts

        return fallback

if __name__ == "__main__":
    unittest.main()
