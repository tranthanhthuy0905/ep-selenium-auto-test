"""
    Command run test:
        python3 -m unittest Tests_Dev.CE_Volume.test_attach_volume -v

Scenarios:
    Given a volume not attached (attached) with a Running (Stopped) VM
    When user selects the volume
    Then user can see the "Attach volume" button
    When user clicks on "Attach volume" button
    Then user can see a pop-up Attach volume box
    When user selects one VM in the list suggested in "Select a volume" option
    And user clicks on "OK" button
    Then user can see the VM Name updated in the chosen volume's information
    If user tries to re-attach the volume with the instance
    Then user cannot click the "Attach volume" button
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


class Test_attach_volume(VolumeBaseTest):

    def test_attach_running_vm_to_volume(self):
        '''
            TEST CASE: Attach a Running vm to a volume
        '''
        # Flow of work: Create an instance
        #               Create a volume
        #               Attach volume with the above instance
        self.choose_volume(CECreateVolumePageLocators.CUSTOM_DISK,
                           False, CEVolumeTestData.SIZE2, True)
        # Delete instance in the end of test
        self.delete_CE_instance_by_id(self.instance_id)
        # Delete volume in the end of test
        self.delete_CE_volume_by_id(self.volume_id)
        time.sleep(2)

    # def test_attach_stopped_vm_to_volume(self):
    #     '''
    #         TEST CASE: Attach a Stopped vm to a volume
    #     '''
    #
    #     # Flow of work: Create an instance + Stop the instance
    #     #               Create a volume
    #     #               Attach volume with the above instance
    #     self.choose_volume(CECreateVolumePageLocators.CUSTOM_DISK,
    #                        True, CEVolumeTestData.SIZE2, True)
    #     # Delete instance in the end of test
    #     self.delete_CE_instance_by_id(self.instance_id)
    #     # Delete volume in the end of test
    #     self.delete_CE_volume_by_id(self.volume_id)
    #     time.sleep(2)


    # def test_attach_vm_to_attached_volume(self):
    #     ''' TEST CASE: Attach a Stopped vm to a volume '''
    #
    #     # Flow of work: Create an instance + Stop the instance
    #     #               Create a volume
    #     #               Attach volume with the above instance
    #     self.choose_volume(CECreateVolumePageLocators.CUSTOM_DISK,
    #                        True, CEVolumeTestData.SIZE2, True)
    #     time.sleep(3)
    #     # Choose the newly created volume again
    #     self.volume_page.click_button(
    #         (By.XPATH, '//span[././input/@type="radio" and ancestor::tr/@data-row-key="' + self.volume_id + '"]'))
    #     # Check whether "Attach volume" button is still clickable or not when chosing a volume already attached with an instance
    #     self.assertFalse(
    #         self.volume_page.find_element(*CEVolumePageLocators.ATTACH_VOLUME_BTN).is_enabled(),
    #         "Should fail to attach an instance to a volume already attached with an existing instance"
    #     )
    #     # Delete instance in the end of test
    #     self.delete_CE_instance_by_id(self.instance_id)
    #     # Delete volume in the end of test
    #     self.delete_CE_volume_by_id(self.volume_id)
    #     time.sleep(2)

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
