import os
import unittest

import HtmlTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tests.ec2.ce_base_test import CEBaseTest
from Pages.ec2.ec2_homepage import EC2HomePage
from Pages.ec2.ec2_volume_page import EC2VolumePage
from Pages.ec2.ec2_create_volume_page import EC2CreateVolumePage
from Configs.TestData.CEVolumeTestData import CEVolumeTestData
from Locators.ec2 import *

import time


class TestVolume(CEBaseTest):
    def test_a_create_volume(self):
        """
            TEST CASE: Volume should be created successfully
        """
        self.EC2_homepage = EC2HomePage(self.driver)
        self.EC2_homepage.access_ec2_volumnes_page()

        self.ec2_volume_page = EC2VolumePage(self.driver)
        self.assertEqual(self.driver.current_url, self.ec2_volume_page.base_url)
        # time.sleep(2)
        self.assertTrue(
            self.ec2_volume_page.check_element_existence(EC2VolumnePageLocators.CREATE_VOLUME_BTN)
        )

        self.ec2_volume_page.access_create_volume_page()
        self.ec2_create_volume_page = EC2CreateVolumePage(self.driver)
        self.assertEqual(self.driver.current_url, self.ec2_create_volume_page.base_url)
    
        volume_name = CEVolumeTestData.VOLUME_NAME
        self.ec2_create_volume_page.create_volume(volume_name=volume_name, volume_size=CEVolumeTestData.SIZE)
        self.volume_name = volume_name

        

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )