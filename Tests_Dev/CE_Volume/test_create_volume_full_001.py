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
    Then user can move to "Create New Volume" page
    And user can fill in Volume name
    And user can select Volume type
    When user clicks on "Create Volume" button
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
        # Then user can see the list of available Volumes
        self.volume_page = CEVolumePage(self.driver)
        self.assertEqual(self.driver.current_url, self.volume_page.base_url)
        self.assertTrue(self.volume_page.check_element_existence(CEVolumePageLocators.CREATE_VOLUME_BTN))
        self.assertTrue(self.volume_page.check_element_existence(CEVolumePageLocators.VOLUMES_LIST))

        # When user clicks on "Create Volume" button on the top right
        self.volume_page.click_button(CEVolumePageLocators.CREATE_VOLUME_BTN)
        #Then user can move to "Create New Volume" page
        self.create_volume_page = CECreateVolumePage(self.driver)
        self.assertEqual(self.driver.current_url, self.create_volume_page.base_url)
        # And user can fill in Volume name
        # And user can select Volume type
        volume_name = CEVolumeTestData.VOLUME_NAME
        self.create_volume_page.fill_volume_info(volume_name=volume_name, volume_size=CEVolumeTestData.SIZE)
        self.volume_name = volume_name

        # When user clicks on "Create Volume" button
        self.create_volume_page.click_button(CECreateVolumePageLocators.CREATE_VOLUME_BTN)
        # Then user can see the newly created volume updated in the list of volumes (status: Allocated)
        WebDriverWait(self.driver, 10).until(EC.url_to_be(self.volume_page.base_url))
        volume_row = self.driver.find_element(*CECreateVolumePageLocators.PARRENT_BY_VOLUME_NAME(_volume_name=volume_name))
        self.volume_id = volume_row.get_attribute("data-row-key")
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "ant-badge-status-text"), "Allocated"))

        # Clear test data
        self.delete_CE_volume_by_id(self.volume_id)

# python3 -m unittest Tests.CE_Volume.test_create_volume_full_001 -v

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
