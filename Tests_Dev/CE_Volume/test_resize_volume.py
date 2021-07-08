"""
    Command run test:
        python3 -m unittest Tests_Dev.CE_Volume.test_resize_volume -v

    Test big flow Resize_volume
"""
import os
import time
import unittest
from selenium.webdriver.support import expected_conditions as EC

import HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Configs.TestData.CEVolumeTestData import CEVolumeTestData
from Locators.CE import CEVolumePageLocators, CECreateVolumePageLocators
from Tests_Dev.CE_Volume.volume_base_test import VolumeBaseTest


class Test_custom_volume(VolumeBaseTest):
    """ TEST CASE: All the scenarios relating to Resize Volume"""

    def resize_volume(self, initial_disk_option, initial_size, disk_option, enter_value, shrink_ok, stop_vm, attach_vm):
        """ General method to resize volume """

        # *** Choose one existing volume attached with instance ***
        # Flow of work: Create an instance ( + Stop the instance)
        #               Create a volume
        #               Attach volume with the above instance
        # OR
        # *** Choose an independent existing volume ***
        # Flow of work: Create a volume
        self.choose_volume(disk_option=initial_disk_option, stop_vm=stop_vm,
                           initial_size=initial_size, attach_vm=attach_vm)
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
        if disk_option == CECreateVolumePageLocators.CUSTOM_DISK:
            self.volume_page \
                .fill_form(enter_value, CEVolumePageLocators.SIZE_FORM)

        # If user clicks on Shrink OK
        if shrink_ok == "with":
            self.volume_page.choose_Shrink_OK()

        # When user clicks on "OK" button
        self.volume_page.click_button(CEVolumePageLocators.OK_BTN)

        time.sleep(3)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[././input/@type="radio" and ancestor::tr/@data-row-key="' + self.volume_id + '"]')))
        self.volume_page.click_button(
            (By.XPATH, '//span[././input/@type="radio" and ancestor::tr/@data-row-key="' + self.volume_id + '"]'))
        time.sleep(5)
        # If a VM is attached to volume
        print("Size_GB is: ", self.volume_page.check_size_gb())
        print("Initial size is: ", initial_size)
        if attach_vm:
            # When the volume is attached with an instance => Only upsizing the volume without Shrinking it is workable
            if enter_value > initial_size:
                if shrink_ok == "without":
                    self.assertTrue(
                        self.volume_page.check_size_gb() != initial_size,
                        "Should SUCCEED to upsize volume without clicking on Shrink OK when it is attached with a " + self.instance_state + " VM"
                    )
                else:
                    self.assertTrue(
                        self.volume_page.check_size_gb() == initial_size,
                        "Should FAIL to upsize volume with clicking on Shrink OK when it is attached with a " + self.instance_state + " VM"
                    )
            elif enter_value == initial_size:
                self.assertTrue(
                    self.volume_page.check_size_gb() == initial_size,
                    "Should have NO change in volume size of the one attached with a " + self.instance_state + " VM when entering the same volume " + shrink_ok + " clicking on Shrink OK"
                )
            else:
                self.assertTrue(
                    self.volume_page.check_size_gb() == initial_size,
                    "Should FAIL to downsize volume " + shrink_ok + " clicking on Shrink OK when it is attached with a " + self.instance_state + " VM"
                )

        # If no VM is attached to volume
        else:
            if enter_value > initial_size:
                if shrink_ok == "without":
                    self.assertTrue(
                        self.volume_page.check_size_gb() != initial_size,
                        "Should SUCCEED to upsize volume NOT attached with a " + self.instance_state + " VM without clicking on Shrink OK"
                    )
                else:
                    self.assertTrue(
                        self.volume_page.check_size_gb() == initial_size,
                        "Should FAIL to upsize volume NOT attached with a " + self.instance_state + " VM with clicking on Shrink OK"
                    )
            elif enter_value == initial_size:
                self.assertTrue(
                    self.volume_page.check_size_gb() == initial_size,
                    "Should have NO change in volume size of the one NOT attached with a VM, entering the same volume " + shrink_ok + " clicking on Shrink OK"
                )
            else:
                if shrink_ok == "with":
                    self.assertTrue(
                        self.volume_page.check_size_gb() != initial_size,
                        "Should SUCCEED to downsize volume NOT attached with a " + self.instance_state + " VM with clicking on Shrink OK"
                    )
                else:
                    self.assertTrue(
                        self.volume_page.check_size_gb() == initial_size,
                        "Should FAIL to downsize volume NOT attached with a " + self.instance_state + " VM without clicking on Shrink OK"
                    )
        time.sleep(2)
        # TODO: Delete Volume and Instance
        self.delete_CE_volume_by_id(self.volume_id)
        if attach_vm:
            self.delete_CE_instance_by_id(self.instance_id)

        self.tearDown()

    """ TEST UPSIZE """
# *** Click on Shrink OK ***
    def test_upsize_shrink_running_VM_custom_disk(self):
        """ TEST CASE: Upsize Volume attached with a Running VM, click on Shrink OK and choose Custom Disk option"""
        self.resize_volume(CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE1),
                           CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE2), "with", False, True)

    def test_upsize_shrink_stopped_VM_custom_disk(self):
        """ TEST CASE: Upsize Volume attached with Stopped VM, click on Shrink OK and choose Custom Disk option"""
        self.resize_volume(CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE1),
                           CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE2), "with", True, True)

    def test_upsize_shrink_noVM_custom_disk(self):
        """ TEST CASE: Upsize Volume no VM, click on Shrink OK and choose Custom Disk option"""
        self.resize_volume(CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE1),
                           CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE2), "with", False, False)

# *** NOT click on Shrink OK ***
    def test_upsize_not_shrink_noVM_custom_disk(self):
        """ TEST CASE: Upsize Volume no VM, NOT click on Shrink OK and choose Custom Disk option"""
        self.resize_volume(CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE1),
                           CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE2), "without", False,
                           False)

    def test_upsize_not_shrink_stopped_VM_custom_disk(self):
        """ TEST CASE: Upsize Volume attached with Stopped VM, NOT click on Shrink OK and choose Custom Disk option"""
        self.resize_volume(CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE1),
                           CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE2), "without", True, True)

    def test_upsize_not_shrink_running_VM_custom_disk(self):
        """ TEST CASE: Upsize Volume attached with a Running VM, NOT click on Shrink OK and choose Custom Disk option"""
        self.resize_volume(CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE1),
                           CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE2), "without", False, True)

        """ TEST DOWNSIZE """
# *** Click on Shrink OK ***
    def test_downsize_shrink_running_VM_custom_disk(self):
        """ TEST CASE: Downsize Volume attached with a Running VM, click on Shrink OK and choose Custom Disk option"""
        self.resize_volume(CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE2),
                           CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE1), "with", False, True)

    def test_downsize_shrink_stopped_VM_custom_disk(self):
        """ TEST CASE: Downsize Volume attached with Stopped VM, click on Shrink OK and choose Custom Disk option"""
        self.resize_volume(CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE2),
                           CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE1), "with", True, True)

    def test_downsize_shrink_noVM_custom_disk(self):
        """ TEST CASE: Downsize Volume no VM, click on Shrink OK and choose Custom Disk option"""
        self.resize_volume(CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE2),
                           CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE1), "with", False, False)

# *** NOT click on Shrink OK ***
    def test_downsize_not_shrink_running_VM_custom_disk(self):
        """ TEST CASE: Downsize Volume attached with a Running VM, NOT click on Shrink OK and choose Custom Disk option"""
        self.resize_volume(CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE2),
                           CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE1), "without", False, True)

    def test_downsize_not_shrink_stopped_VM_custom_disk(self):
        """ TEST CASE: Downsize Volume attached with Stopped VM, NOT click on Shrink OK and choose Custom Disk option"""
        self.resize_volume(CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE2),
                           CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE1), "without", True, True)

    def test_downsize_not_shrink_noVM_custom_disk(self):
        """ TEST CASE: Downsize Volume no VM, NOT click on Shrink OK and choose Custom Disk option"""
        self.resize_volume(CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE2),
                           CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE1), "without", False,
                           False)


# TODO: If user would like to test the above cases with other disk options (Default 100G, 200G or 500G),
# TODO: Uncomment below tests
    # """ TEST UPSIZE"""
    # *** Click on Shrink OK ***
    # def test_upsize_shrink_running_VM_200G(self):
    #     ''' TEST CASE: Upsize Volume attached with Running VM, click on Shrink OK and choose 200G option'''
    #     self.resize_volume(CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE1),
    #                        CEVolumePageLocators.OPTION_200G, 200, "with", False, True)

    # def test_upsize_shrink_stopped_VM_200G(self):
    #     """ TEST CASE: Upsize Volume attached with Stopped VM, click on Shrink OK and choose 200G option"""
    #     self.resize_volume(CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE1),
    #                        CEVolumePageLocators.OPTION_200G, 200, "with", True, True)
    #
    # def test_upsize_shrink_noVM_200G(self):
    #     """ TEST CASE: Upsize Volume no VM, click on Shrink OK and choose 200G option"""
    #     self.resize_volume(CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE1),
    #                        CEVolumePageLocators.OPTION_200G, 200, "with", False, False)
    #
    # # *** NOT click on Shrink OK ***
    # def test_upsize_not_shrink_running_VM_200G(self):
    #     ''' TEST CASE: Upsize Volume attached with Running VM, NOT click on Shrink OK and choose 200G option'''
    #     self.resize_volume(CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE1),
    #                        CEVolumePageLocators.OPTION_200G, 200, "without", False, True)
    #
    # def test_upsize_not_shrink_stopped_VM_200G(self):
    #     """ TEST CASE: Upsize Volume attached with Stopped VM, NOT click on Shrink OK and choose 200G option"""
    #     self.resize_volume(CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE1),
    #                        CEVolumePageLocators.OPTION_200G, 200, "without", True, True)
    #
    # def test_upsize_not_shrink_noVM_200G(self):
    #     """ TEST CASE: Upsize Volume no VM, NOT click on Shrink OK and choose 200G option"""
    #     self.resize_volume(CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE1),
    #                        CEVolumePageLocators.OPTION_200G, 200, "without", False, False)
    #
    # """ TEST DOWNSIZE """
    #
    # # *** Click on Shrink OK ***
    # def test_downsize_shrink_running_VM_200G(self):
    #     ''' TEST CASE: Downsize Volume attached with Running VM, click on Shrink OK and choose 200G option'''
    #     self.resize_volume(CEVolumePageLocators.OPTION_200G, 200,
    #                        CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE1), "with", False, True)
    #
    # def test_downsize_shrink_stopped_VM_200G(self):
    #     """ TEST CASE: Downsize Volume attached with Stopped VM, click on Shrink OK and choose 200G option"""
    #     self.resize_volume(CEVolumePageLocators.OPTION_200G, 200,
    #                        CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE1), "with", True, True)
    #
    # def test_downsize_shrink_noVM_200G(self):
    #     """ TEST CASE: Downsize Volume no VM, click on Shrink OK and choose 200G option"""
    #     self.resize_volume(CEVolumePageLocators.OPTION_200G, 200,
    #                        CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE1), "with", False, False)
    #
    # # *** NOT click on Shrink OK ***
    # def test_downsize_not_shrink_running_VM_200G(self):
    #     ''' TEST CASE: Downsize Volume attached with Running VM, NOT click on Shrink OK and choose 200G option'''
    #     self.resize_volume(CEVolumePageLocators.OPTION_200G, 200,
    #                        CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE1), "without", False, True)
    #
    # def test_downsize_not_shrink_stopped_VM_200G(self):
    #     """ TEST CASE: Downsize Volume attached with Stopped VM, NOT click on Shrink OK and choose 200G option"""
    #     self.resize_volume(CEVolumePageLocators.OPTION_200G, 200,
    #                        CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE1), "without", True, True)
    #
    # def test_downsize_not_shrink_noVM_200G(self):
    #     """ TEST CASE: Downsize Volume no VM, NOT click on Shrink OK and choose 200G option"""
    #     self.resize_volume(CEVolumePageLocators.OPTION_200G, 200,
    #                        CECreateVolumePageLocators.CUSTOM_DISK, int(CEVolumeTestData.SIZE1), "without", False, False)


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
