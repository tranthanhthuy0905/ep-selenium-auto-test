"""
    Command run test:
        python3 -m unittest Tests_Dev.CE_Volume.test_detach_volume -v

    Test big flow
"""
import os
import time
import unittest

import HtmlTestRunner

from Configs.TestData.CEVolumeTestData import CEVolumeTestData
from Locators.CE import CECreateVolumePageLocators, CEVolumePageLocators
from Tests_Dev.CE_Volume.volume_base_test import VolumeBaseTest


class Test_detach_volume(VolumeBaseTest):

    # def test_detach_volume_running_vm(self):
    #     self.choose_volume(CECreateVolumePageLocators.CUSTOM_DISK,
    #                        False, CEVolumeTestData.SIZE2, True)
    #     self.detach_volume_from_instance()
    #     self.delete_CE_instance_by_id(self.instance_id)
    #     self.delete_CE_volume_by_id(self.volume_id)
    #     time.sleep(2)

    def test_detach_volume_stopped_vm(self):
        self.choose_volume(CECreateVolumePageLocators.CUSTOM_DISK,
                           True, CEVolumeTestData.SIZE2, True)
        time.sleep(2)
        self.detach_volume_from_instance()
        self.delete_CE_instance_by_id(self.instance_id)
        self.delete_CE_volume_by_id(self.volume_id)
        time.sleep(2)

    # def test_detach_volume_no_vm(self):
    #     self.choose_volume(CECreateVolumePageLocators.CUSTOM_DISK,
    #                        False, CEVolumeTestData.SIZE2, True)
    #     self.assertFalse(
    #         self.volume_page.click_button(CEVolumePageLocators.DETACH_VOLUME_BTN),
    #         "Should not be able to detach a volume from no instance"
    #     )
    #     self.delete_CE_instance_by_id(self.instance_id)
    #     self.delete_CE_volume_by_id(self.volume_id)
    #     time.sleep(2)

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
