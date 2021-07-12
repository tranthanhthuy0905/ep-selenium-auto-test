'''
Scenario 15. 
'''

from Configs.TestData.CESecurityGroupTestData import CESecurityGroupTestData
import os
import unittest

import HtmlTestRunner
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tests_Dev.CE.ce_base_test import CEBaseTest
from Pages.CE.homepage import CEHomePage
from Pages.CE.instances_page import CEInstancesPage
from Pages.CE.security_group_page import SGHomePage, SGCreatePage, SGDetailsPage
from Pages.CE.launch_instances_wizard_page import *
from Configs.TestData.CEInstanceTestData import CEInstanceTestData
from Configs.TestData.CEVolumeTestData import CEVolumeTestData
from Configs.TestData.CEKeypairTestData import CEKeypairTestData
from Locators.CE import *

import time


class TestInstances15(CEBaseTest):
    def test_stop_instance(self):
        """
            TEST CASE: Launch instance and reboot	
        """
        # Create an simple instance
        instance_name = self.create_simple_instance()
    
        # Get instance id for clear data after test
        self.instance_id = self.instances_page.get_instance_id(instance_name)

        # Check if the new instance state is Running
        self.instances_page.check_instance_state(self.instance_id, CEInstancePageLocators.RUNNING_STATUS)
        print("Instance is created successfully!")

        # Reboot instance
        self.instances_page.reboot_instance(self.instance_id)

        


# python3 -m unittest Tests.CE_Instance.test_launch_instance_13 -v


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )