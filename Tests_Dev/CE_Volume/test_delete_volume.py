"""
    Command run test:
        python3 -m unittest Tests_Dev.CE_Volume.test_delete_volume -v

    Test big flow
"""
import os
import time
import unittest

import HtmlTestRunner
from selenium.webdriver.common.by import By

from Configs.TestData.CEVolumeTestData import CEVolumeTestData
from Locators.CE import CEVolumePageLocators, CEInstancePageLocators, CECreateVolumePageLocators
from Pages.CE.create_volume_page import CECreateVolumePage
from Pages.CE.homepage import CEHomePage
from Pages.CE.volume_page import CEVolumePage
from Tests_Dev.CE_Volume.volume_base_test import VolumeBaseTest


class Test_delete_volume(VolumeBaseTest):

    def test_delete_volume_noVM(self):
        self.choose_volume(CECreateVolumePageLocators.CUSTOM_DISK,
                           False, CEVolumeTestData.SIZE2, False)
        self.delete_volume()
        self.delete_CE_instance_by_id(self.instance_id)
        time.sleep(2)

    def test_delete_volume_running_VM(self):
        self.choose_volume(CECreateVolumePageLocators.CUSTOM_DISK,
                           False, CEVolumeTestData.SIZE2, True)
        self.assertFalse(
            self.volume_page.click_button(CEVolumePageLocators.DELETE_VOLUME_BTN),
            "Should fail to delete a volume already attached with an existing Running instance"
        )
        # self.assertTrue(
        #     self.launch_instances_wizard_page.check_element_existence(
        #         (By.XPATH, "//td[contains(.,'" + self.instance_name + "')]")),
        #     "Should successfully create an instance by adding default password by updating new instance to the list"
        # )
        self.delete_CE_instance_by_id(self.instance_id)
        self.delete_CE_volume_by_id(self.volume_id)
        time.sleep(2)

    def test_delete_volume_stopped_VM(self):
        self.choose_volume(CECreateVolumePageLocators.CUSTOM_DISK,
                           True, CEVolumeTestData.SIZE2, True)
        self.assertFalse(
            self.volume_page.click_button(CEVolumePageLocators.DELETE_VOLUME_BTN),
            "Should fail to delete a volume already attached with an existing Stopped instance"
        )
        self.delete_CE_instance_by_id(self.instance_id)
        self.delete_CE_volume_by_id(self.volume_id)
        time.sleep(2)

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
