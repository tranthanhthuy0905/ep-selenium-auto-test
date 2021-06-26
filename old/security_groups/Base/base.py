import os
import time
import json
import requests
import logging
import unittest
import random

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from pprint import pprint

from Locators.locators import SecurityGroupHomeLocators

class EPAudit:
    def __init__(self, service_name, headless=True):
        self.url = self.get_url(service_name)
        self.cookie = {
            "name": "user-token",
            "value": self.get_user_token()
        }
        if headless:
            options = Options()
            options.headless = True
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        else:
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.url)
        self.driver.add_cookie(self.cookie)
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        self.report = {}

    def get_user_token(self):
        return SecurityGroupHomeLocators.AUTOTEST_USER_TOKEN

    def get_url(self, service_name):
        if service_name == 'security_groups':
            return SecurityGroupHomeLocators.EC2_URL

    def add_report(self, key, condition):
        self.report.update({
            key: "success" if condition else "failed"
        })

    def is_element_exists(self, *locator, custom_params=None):
        try:
            print(custom_params)
            if custom_params:
                custom_locator = tuple([locator[0][0], locator[0][1].format(**custom_params)])
                print("Custom locator: ", custom_locator)
                self.driver.find_elements(*custom_locator)
            else:
                self.driver.find_elements(*locator)
            return True
        except Exception as e:
            print(e)
            return False

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
                if (result is not unsatisfactory): return result
            except:
                pass
            time.sleep(1)  # This makes the function wait a second between attempts

        return fallback