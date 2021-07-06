"""
    Command run test:
        python3 -m unittest Tests_Dev.CE_Volume.test_resize_volume -v

    Test big flow Resize_volume
"""
import os
import time
import unittest

import HtmlTestRunner
from selenium.webdriver.common.by import By

from Configs.TestData.CEVolumeTestData import CEVolumeTestData
from Locators.CE import CEVolumePageLocators, CECreateVolumePageLocators
from Pages.CE.volume_page import CEVolumePage
from Tests_Dev.CE_Volume.volume_base_test import VolumeBaseTest


class Test_custom_volume(VolumeBaseTest):

    ''' TEST CASE: All the scenarios relating to Resize Volume'''

    def resize_volume(self, disk_option, shrink_ok, stop_vm, attach_vm, initial_size, enter_value):
        ''' General method to resize volume '''

    # *** Choose one existing volume attached with instance ***
        # Flow of work: Create an instance ( + Stop the instance)
        #               Create a volume
        #               Attach volume with the above instance
    # OR
    # *** Choose an independent existing volume ***
        # Flow of work: Create a volume
        self.choose_volume(disk_option=disk_option, stop_vm=stop_vm, initial_size=initial_size, attach_vm=attach_vm)
        time.sleep(2)
        # When user clicks on "Resize volume" button on the top right
        # self.volume_page.click_button(
        #     (By.XPATH, '//span[././input/@type="radio" and ancestor::tr/@data-row-key="' + self.volume_id + '"]'))
        self.volume_page.click_button(CEVolumePageLocators.RESIZE_VOLUME_BTN)

        # Wait for the Resize volume box popped up
        time.sleep(2)
        # Choose Disk Offering options
        self.volume_page \
            .click_button(CEVolumePageLocators.DISK_OFFERING) \
            .choose_disk_offering_option(CEVolumePageLocators.DISK_OFFERING, disk_option)

        time.sleep(3)
        # If user chooses Custom Disk, a size blank should appear
        if (disk_option == CECreateVolumePageLocators.CUSTOM_DISK):
            self.volume_page \
                .fill_form(enter_value, CEVolumePageLocators.SIZE_FORM)

        # If user clicks on Shrink OK
        if (shrink_ok == "with"):
            self.volume_page.choose_Shrink_OK()

        # When user clicks on "OK" button
        self.volume_page.click_button(CEVolumePageLocators.OK_BTN)

        time.sleep(5)

        # If a VM is attached to volume
        if (attach_vm):
            # When the volume is attached with an instance => Only upsizing the volume without Shrinking it is workable
            if (enter_value >= initial_size and shrink_ok == "without"):
                self.assertTrue(
                    self.volume_page.check_size_gb() != initial_size,
                    "Should succeed to upsize volume when it is attached to both a Running VM and a Stopped vM"
                )
            else:
                self.assertTrue(
                    self.volume_page.check_size_gb() == initial_size,
                    "Should fail to downsize volume when it is attached to a VM or upsize volume but click on Shrink OK"
                )

        # If no VM is attached to volume
        else:
            # Scenario 8 + 10: Downsize the volume without Shrink OK => Should not resize successfully
            if (enter_value < initial_size and shrink_ok == "without"):
                self.assertTrue(
                    self.volume_page.check_size_gb() == initial_size,
                    "Should fail to downsize volume not attached with any VM without shrinking it"
                )
            # Other scenarios should be successful by all means
            else:
                self.assertTrue(
                    self.volume_page.check_size_gb() != initial_size,
                    "Should successfully resize volume not attached with any VM " + shrink_ok +" Shrink OK"
                )
        time.sleep(2)
        # TODO: Delete Volume and Instance
        self.delete_CE_volume_by_id(self.volume_id)
        if (attach_vm):
            self.delete_CE_instance_by_id(self.instance_id)

        self.tearDown()

    def test_upsize_shrink_running_VM_custom_disk(self):
        ''' TEST CASE: Upsize Volume no VM, click on Shrink OK and choose Custom Disk option'''
        self.resize_volume(CECreateVolumePageLocators.CUSTOM_DISK, "without",
                           False, True, CEVolumeTestData.SIZE1, CEVolumeTestData.SIZE2)

# TODO: Update scenarios below
# *** Choosing 200G just to generalize for 100G, 500G option ***
#     def test_upsize_shrink_running_VM_200G(self):
#         ''' TEST CASE: Upsize Volume attached with Running VM, click on Shrink OK and choose 200G option'''
#         self.resize_volume(CEVolumePageLocators.OPTION_200G, "with",
#                            False, 200, int(CEVolumeTestData.SIZE1))
#     def test_upsize_shrink_stopped_VM_custom_disk(self):
#         ''' TEST CASE: Upsize Volume attached with Stopped VM, click on Shrink OK and choose Custom Disk option'''
#         self.resize_volume(CECreateVolumePageLocators.CUSTOM_DISK, "with",
#                            True, CEVolumeTestData.SIZE1, CEVolumeTestData.SIZE2)
    #
    # def test_upsize_shrink_stopped_VM_200G(self):
    #     ''' TEST CASE: Upsize Volume attached with Stopped VM, click on Shrink OK and choose 200G option'''
    #     self.resize_volume(CEVolumePageLocators.OPTION_200G, "with",
    #                        True, True, 200, int(CEVolumeTestData.SIZE1))
    # def test_upsize_noShrink_running_VM_custom_disk(self):
    #     ''' TEST CASE: Upsize Volume attached with Running VM, NOT click on Shrink OK and choose Custom Disk option'''
    #     self.resize_volume(CECreateVolumePageLocators.CUSTOM_DISK, "without",
    #                        False, CEVolumeTestData.SIZE1, CEVolumeTestData.SIZE2)
    #
    # def test_upsize_noShrink_stopped_VM_custom_disk(self):
    #     ''' TEST CASE: Upsize Volume attached with Stopped VM, NOT click on Shrink OK and choose Custom Disk option'''
    #     self.resize_volume(CECreateVolumePageLocators.CUSTOM_DISK, "without",
    #                        True, CEVolumeTestData.SIZE1, CEVolumeTestData.SIZE2)

    # def test_upsize_noShrink_running_VM_200G(self):
    #     ''' TEST CASE: Upsize Volume attached with Running VM, NOT click on Shrink OK and choose Custom Disk option'''
    #     self.resize_volume(CECreateVolumePageLocators.CUSTOM_DISK, "without",
    #                        False, CEVolumeTestData.SIZE1, 200)

    # def test_upsize_noShrink_stopped_VM_200G(self):
    #     ''' TEST CASE: Upsize Volume attached with Stopped VM, NOT click on Shrink OK and choose Custom Disk option'''
    #     self.resize_volume(CECreateVolumePageLocators.CUSTOM_DISK, "without",
    #                        True, CEVolumeTestData.SIZE1, 200)

    ''' TEST CASE: Downsize'''
        #def test_downsize_shrink_running_VM_custom_disk(self):
        #     ''' TEST CASE: Downsize Volume attached with Running VM, click on Shrink OK and choose Custom Disk option'''
        #     self.resize_volume(CECreateVolumePageLocators.CUSTOM_DISK, "with",
        #                        False, CEVolumeTestData.SIZE2, CEVolumeTestData.SIZE1)

        # *** Choosing 200G just to generalize for 100G, 500G option ***
        #     def test_downsize_shrink_running_VM_500G(self):
        #         ''' TEST CASE: Downsize Volume attached with Running VM, click on Shrink OK and choose 500G option'''
        #         self.resize_volume(CEVolumePageLocators.OPTION_500G, "with",
        #                            False, 500, int(CEVolumeTestData.SIZE1))
        #     def test_downsize_shrink_stopped_VM_custom_disk(self):
        #         ''' TEST CASE: Downsize Volume attached with Stopped VM, click on Shrink OK and choose Custom Disk option'''
        #         self.resize_volume(CECreateVolumePageLocators.CUSTOM_DISK, "with",
        #                            True, CEVolumeTestData.SIZE2, CEVolumeTestData.SIZE1)
        #
        # def test_downsize_shrink_stopped_VM_500G(self):
        #     ''' TEST CASE: Downsize Volume attached with Stopped VM, click on Shrink OK and choose 500G option'''
        #     self.resize_volume(CEVolumePageLocators.OPTION_500G, "with",
        #                        True , 500, int(CEVolumeTestData.SIZE1))
        # def test_downsize_noShrink_running_VM_custom_disk(self):
        #     ''' TEST CASE: Downsize Volume attached with Running VM, NOT click on Shrink OK and choose Custom Disk option'''
        #     self.resize_volume(CECreateVolumePageLocators.CUSTOM_DISK, "without",
        #                        False, CEVolumeTestData.SIZE2, CEVolumeTestData.SIZE1)
        #
        # def test_downsize_noShrink_stopped_VM_custom_disk(self):
        #     ''' TEST CASE: Downsize Volume attached with Stopped VM, NOT click on Shrink OK and choose Custom Disk option'''
        #     self.resize_volume(CECreateVolumePageLocators.CUSTOM_DISK, "without",
        #                        True, CEVolumeTestData.SIZE2, CEVolumeTestData.SIZE1)

        # def test_downsize_noShrink_stopped_VM_500G(self):
        #     ''' TEST CASE: Downsize Volume attached with Stopped VM, NOT click on Shrink OK and choose 500G option'''
        #     self.resize_volume(CECreateVolumePageLocators.OPTION_500G, "without",
        #                        True, 500, CEVolumeTestData.SIZE1)

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
