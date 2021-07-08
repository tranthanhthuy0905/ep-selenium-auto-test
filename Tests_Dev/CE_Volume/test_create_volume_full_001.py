"""
    Command run test:
        python3 -m unittest Tests_Dev.CE_Volume.test_create_volume_full_001 -v
"""

import os
import unittest

import HtmlTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.CE.homepage import CEHomePage
from Pages.CE.volume_page import CEVolumePage
from Pages.CE.create_volume_page import CECreateVolumePage
from Configs.TestData.CEVolumeTestData import CEVolumeTestData
from Locators.CE import *

import time

from Tests_Dev.CE_Volume.volume_base_test import VolumeBaseTest

'''
Scenario 2: Create Volume without "Launch Instance" process
    Given a certain user
    When user clicks on "Volumes" button on the left side
    Then user can see the list of available Volumes 
    When user clicks on "Create Volume" button on the top right
    Then user can move to "Create New Volume" page
    And user can fill in Volume name
    And user can select Volume type
    When user clicks on "Create" button
    Then user can see the newly created volume updated in the list of volumes (status: Allocated)
'''

class TestVolume(VolumeBaseTest):
    def test_create_volume_custom_disk(self):
        """
            TEST CASE: Create volume in Volumes page, choosing Custom disk option
            Should SUCCEED
        """
        self.choose_volume(CECreateVolumePageLocators.CUSTOM_DISK, False, CEVolumeTestData.SIZE2, False)
        self.tearDown()

    def test_create_volume_default_100G(self):
        """
            TEST CASE: Create volume in Volumes page, choosing Default 100G option
            Should SUCCEED
        """
        self.choose_volume(CECreateVolumePageLocators.DEFAULT_100G, False, 100, False)
        self.tearDown()

    def test_create_volume_200G(self):
        """
            TEST CASE: Create volume in Volumes page, choosing 200G option
            Should SUCCEED
        """
        self.choose_volume(CECreateVolumePageLocators.OPTION_200G, False, 200, False)
        self.tearDown()

    def test_create_volume_500G(self):
        """
            TEST CASE: Create volume in Volumes page, choosing 500G option
            Should SUCCEED
        """
        self.choose_volume(CECreateVolumePageLocators.OPTION_500G, False, 500, False)
        self.tearDown()

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
