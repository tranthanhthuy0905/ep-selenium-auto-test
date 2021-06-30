import os
import unittest

import HtmlTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tests.CE.ce_base_test import CEBaseTest
from Pages.CE.homepage import CEHomePage
from Pages.CE.volume_page import CEVolumePage
from Pages.CE.create_volume_page import CECreateVolumePage
from Configs.TestData.CEVolumeTestData import CEVolumeTestData
from Locators.CE import *

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
        self.CE_homepage = CEHomePage(self.driver)
        self.CE_homepage.access_volumes_page()

        self.volume_page = CEVolumePage(self.driver)
        self.assertEqual(self.driver.current_url, self.volume_page.base_url)
        self.assertTrue(
            self.volume_page.check_element_existence(CEVolumnePageLocators.CREATE_VOLUME_BTN)
        )

        # When user clicks on "Create Volume" button on the top right
        self.volume_page.click_create_volume_btn()
        self.create_volume_page = CECreateVolumePage(self.driver)
        self.assertEqual(self.driver.current_url, self.create_volume_page.base_url)

        # When user clicks on "Create" button
        volume_name = CEVolumeTestData.VOLUME_NAME
        self.create_volume_page.create_volume(volume_name=volume_name, volume_size=CEVolumeTestData.SIZE)
        self.volume_name = volume_name


        # Then user can see the newly created volume updated in the list of volumes (status: Allocated)
        WebDriverWait(self.driver, 10).until(EC.url_to_be(self.volume_page.base_url))
        self.assertTrue(
            self.volume_page.check_element_existence((By.XPATH, "//td[contains(.,'" + volume_name +"')]"))
        )

        # Clear test data
        self.volume_id = self.driver.find_element_by_xpath("//td[contains(.,'" + volume_name +"')]/parent::*").get_attribute("data-row-key")
        self.delete_CE_volume()
    
# python3 -m unittest Tests.CE_Volume.test_create_volume_full_001 -v

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
