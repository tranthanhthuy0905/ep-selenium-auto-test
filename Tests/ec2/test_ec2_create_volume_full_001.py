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

'''
Screnario 2: Create Volume without "Launch Instance" process
    Given a certain user
    When user clicks on "Volumes" button on the left side
    Then user can see the list of available Volumes 
    When user clicks on "Create Volume" button on the top right
    Then user can see a pop-up "Create New Volume" box
    When user clicks on "Create" button
    Then user can see the newly created volume updated in the list of volumes (status: Allocated) 
'''

class TestVolume(CEBaseTest):
    def test_create_volume(self):
        """
            TEST CASE: Volume should be created successfully
        """

        # When user clicks on "Volumes" button on the left side
        self.EC2_homepage = EC2HomePage(self.driver)
        self.EC2_homepage.access_ec2_volumnes_page()

        self.ec2_volume_page = EC2VolumePage(self.driver)
        self.assertEqual(self.driver.current_url, self.ec2_volume_page.base_url)
        self.assertTrue(
            self.ec2_volume_page.check_element_existence(EC2VolumnePageLocators.CREATE_VOLUME_BTN)
        )

        # When user clicks on "Create Volume" button on the top right
        self.ec2_volume_page.access_create_volume_page()
        self.ec2_create_volume_page = EC2CreateVolumePage(self.driver)
        self.assertEqual(self.driver.current_url, self.ec2_create_volume_page.base_url)
    
        # When user clicks on "Create" button
        volume_name = CEVolumeTestData.VOLUME_NAME
        self.ec2_create_volume_page.create_volume(volume_name=volume_name, volume_size=CEVolumeTestData.SIZE)
        self.volume_name = volume_name


        # Then user can see the newly created volume updated in the list of volumes (status: Allocated) 
        WebDriverWait(self.driver, 10).until(EC.url_to_be(self.ec2_volume_page.base_url))
        self.assertTrue(
            self.ec2_volume_page.check_element_existence((By.XPATH, "//td[contains(.,'" + volume_name +"')]"))
        )

        # TODO: clear volume data
        self.volume_id = self.driver.find_element_by_xpath("//td[contains(.,'" + volume_name +"')]/parent::*").get_attribute("data-row-key")
        
    

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )