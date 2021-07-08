"""
    Command run test:
        python3 -m unittest Tests_Dev.CE_Volume.test_detach_volume -v

    Test big flow of Detach volume from its instance
"""
import os
import time
import unittest

import HtmlTestRunner

from Configs.TestData.CEVolumeTestData import CEVolumeTestData
from Locators.CE import CECreateVolumePageLocators, CEVolumePageLocators
from Tests_Dev.CE_Volume.volume_base_test import VolumeBaseTest


class Test_detach_volume(VolumeBaseTest):

    def test_detach_volume_running_vm(self):
        """
            TEST CASE: Detach the volume from its Running instance
            Should SUCCEED
        """
        # *** Choose one volume attached with a Running instance ***
        # Flow of work:
        # - Create an instance
        # - Create a volume
        # - Attach volume to above instance
        self.choose_volume(CECreateVolumePageLocators.CUSTOM_DISK,
                           False, CEVolumeTestData.SIZE2, True)
        # *** Detach volume from its instance
        # Flow of work:
        # - Click on "Actions" button + Choose Detach volume option
        # - Click "Detach" button to confirm
        # - Should SUCCEED detach the volume from its Running instance
        time.sleep(2)
        self.detach_volume_from_instance("Running")
        time.sleep(2)
        self.tearDown()

    def test_detach_volume_stopped_vm(self):
        """
            TEST CASE: Detach the volume from its Stopped instance
            Should SUCCEED
        """
        # *** Choose one volume attached with a Stopped instance ***
        # Flow of work:
        # - Create an instance + Stop the instance
        # - Create a volume
        # - Attach volume to above instance
        self.choose_volume(CECreateVolumePageLocators.CUSTOM_DISK,
                           True, CEVolumeTestData.SIZE2, True)
        time.sleep(2)
        # *** Detach volume from its instance
        # Flow of work:
        # - Click on "Actions" button + Choose Detach volume option
        # - Click "Detach" button to confirm
        # - Should SUCCEED detach the volume from its Stopped instance
        self.detach_volume_from_instance("Stopped")
        time.sleep(2)
        self.tearDown()

    def test_detach_volume_no_vm(self):
        """
            TEST CASE: Detach the volume from no instance
            Should NOT be able to click "Detach volume" button
        """
        # *** Choose one volume not attached with any instance ***
        # Flow of work:
        # - Create a volume
        self.choose_volume(CECreateVolumePageLocators.CUSTOM_DISK,
                           False, CEVolumeTestData.SIZE2, False)
        # *** Detach volume from no instance
        # Flow of work:
        # - Click on "Actions" button
        # - Should NOT able to click on "Detach volume" button
        self.detach_volume_from_instance("")
        time.sleep(2)
        self.tearDown()

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
