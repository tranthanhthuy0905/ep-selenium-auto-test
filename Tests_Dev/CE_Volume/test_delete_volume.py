"""
    Command run test:
        python3 -m unittest Tests_Dev.CE_Volume.test_delete_volume -v

    Test big flow of Delete volume
"""
import os
import time
import unittest
from selenium.webdriver.support import expected_conditions as EC

import HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Configs.TestData.CEVolumeTestData import CEVolumeTestData
from Locators.CE import CEVolumePageLocators, CEInstancePageLocators, CECreateVolumePageLocators
from Pages.CE.create_volume_page import CECreateVolumePage
from Pages.CE.homepage import CEHomePage
from Pages.CE.volume_page import CEVolumePage
from Tests_Dev.CE_Volume.volume_base_test import VolumeBaseTest


class Test_delete_volume(VolumeBaseTest):

    # def test_delete_volume_noVM(self):
    #     '''
    #         TEST CASE: Delete the volume not attached with any instance
    #         Should SUCCEED
    #     '''
    #     # *** Choose one volume not attached with any instance ***
    #     # Flow of work:
    #     # - Create a volume
    #     self.choose_volume(CECreateVolumePageLocators.CUSTOM_DISK,
    #                        False, CEVolumeTestData.SIZE2, False)
    #     # *** Delete the newly created volume ***
    #     # Flow of work:
    #     # - Click on "Actions" button + Choose "Delete volume" option
    #     # - Click on "Delete" button to confirm the deletion
    #     # - Should SUCCEED to delete the volume
    #     self.delete_volume(True)
    #     time.sleep(10)
    #     self.tearDown()
    #
    # def test_delete_volume_running_VM(self):
    #     '''
    #         TEST CASE: Delete the volume attached with a Running instance
    #         Should NOT able to click on "Delete volume" option
    #     '''
    #     # *** Choose one volume attached with a Running instance ***
    #     # Flow of work:
    #     # - Create an instance
    #     # - Create a volume
    #     # - Attach the volume with above instance
    #     self.choose_volume(CECreateVolumePageLocators.CUSTOM_DISK,
    #                        False, CEVolumeTestData.SIZE2, True)
    #     # *** Delete the newly created volume ***
    #     # Flow of work:
    #     # - Click on "Actions" button
    #     # - Should NOT able to click "Delete volume" button
    #     self.delete_volume(False)
    #     time.sleep(10)
    #     self.tearDown()

    def test_delete_volume_stopped_VM(self):
        '''
            TEST CASE: Delete the volume attached with a Stopped instance
            Should NOT able to click on "Delete volume" option
        '''
        # *** Choose one volume attached with a Stopped instance ***
        # Flow of work:
        # - Create an instance + Stop instance
        # - Create a volume
        # - Attach the volume with above instance
        self.choose_volume(CECreateVolumePageLocators.CUSTOM_DISK,
                           True, CEVolumeTestData.SIZE2, True)
        # *** Delete the newly created volume ***
        # Flow of work:
        # - Click on "Actions" button
        # - Should NOT able to click "Delete volume" button
        self.delete_volume(False)
        time.sleep(10)
        self.tearDown()

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
