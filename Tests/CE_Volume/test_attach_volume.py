"""
    Command run test:
        python3 -m unittest Tests.CE_Volume.test_attach_volume -v

    Test big flow
"""
import time

from selenium.webdriver.common.by import By

from Configs.TestData.CEVolumeTestData import CEVolumeTestData
from Locators.CE import CEVolumePageLocators, CEInstancePageLocators, CECreateVolumePageLocators
from Pages.CE.create_volume_page import CECreateVolumePage
from Pages.CE.homepage import CEHomePage
from Pages.CE.volume_page import CEVolumePage
from Tests.CE_Volume.volume_base_test import VolumeBaseTest


class Test_attach_volume(VolumeBaseTest):

    # def test_attach_running_vm_to_volume(self):
    #     self.choose_volume(CECreateVolumePageLocators.CUSTOM_DISK,
    #                        False, CEVolumeTestData.SIZE2, True)
    #     self.delete_CE_instance_by_id(self.instance_id)
    #     self.delete_CE_volume_by_id(self.volume_id)
    #     time.sleep(2)

    # def test_attach_stopped_vm_to_volume(self):
    #     self.choose_volume(CECreateVolumePageLocators.CUSTOM_DISK,
    #                        True, CEVolumeTestData.SIZE2, True)
    #     self.delete_CE_instance_by_id(self.instance_id)
    #     self.delete_CE_volume_by_id(self.volume_id)
    #     time.sleep(2)

    def test_attach_vm_to_attached_volume(self):
        self.choose_volume(CECreateVolumePageLocators.CUSTOM_DISK,
                           True, CEVolumeTestData.SIZE2, True)
        self.assertFalse(
            self.volume_page.find_element(*CEVolumePageLocators.ATTACH_VOLUME_BTN).click(),
            "Should fail to attach an instance to a volume already attached with an existing instance"
        )
        self.delete_CE_instance_by_id(self.instance_id)
        self.delete_CE_volume_by_id(self.volume_id)
        time.sleep(2)
