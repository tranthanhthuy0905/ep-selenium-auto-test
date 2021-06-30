"""
    This test is general to all the scenarios from 3 to 10 to RESIZE volume in CE_EBS
"""

import os
import time
import unittest

import HtmlTestRunner

from Configs.TestData.CEVolumeTestData import CEVolumeTestData
from Locators.CE import CEInstancePageLocators, CEVolumePageLocators, CECreateVolumePageLocators
from Pages.CE.homepage import CEHomePage
from Pages.CE.volume_page import CEVolumePage
from Tests.CE.ce_base_test import CEBaseTest


class Test_Resize_Volume(CEBaseTest):
    """
        TEST CASE: All scenarios relating to RESIZE VOLUME
    """

    def access_resize_volume(self):
        """
            This function includes all steps until user clicks on Resize Volume button:
            - Direct to Volume page
            - Check the information of the chosen volume: its VM's state, initial volume size
            - Click on Resize volume
        """

        # When user clicks on "Volumes" button on the left side
        self.CE_homepage = CEHomePage(self.driver)
        self.CE_homepage.access_volumes_page()

        self.volume_page = CEVolumePage(self.driver)
        self.assertEqual(self.driver.current_url, self.volume_page.base_url)
        self.assertTrue(
            self.volume_page.check_element_existence(CEVolumePageLocators.CREATE_VOLUME_BTN)
        )

        # Choose one volume in the list
        self.volume_page.click_button(CEInstancePageLocators.RADIO_BTN)

        # Check volume's VM state
        time.sleep(2)
        self.vm_state = self.volume_page.check_instance_state()

        # Check volume's initial size
        self.initial_volume_size = self.volume_page.check_size_gb()

        # Click on "Resize volume" button
        self.volume_page.click_button(CEVolumePageLocators.RESIZE_VOLUME_BTN)

        # Check whether popping up "Resize Volume" box or not after clicking on "Resize volume" button
        self.assertTrue(
            self.volume_page.check_element_existence(CEVolumePageLocators.RESIZE_VOLUME_BOX)
        )


    def resize_volume_options(self, disk_option, condition, enter_value):
        """
            This function includes "access_resize_volume" function above and all the steps after
            the Resize volume box popped up:
            - Include access_resize_volume function above
            - Choose Disk offering option
            - Click on Shrink OK or not
            - Click OK and check the status (succeed or fail)
        """

        # Access volume page
        self.access_resize_volume()

        # Wait for the Resize volume box popped up
        time.sleep(2)
        # Choose Disk Offering options
        self.volume_page\
            .click_button(CEVolumePageLocators.DISK_OFFERING)\
            .choose_disk_offering_option(CEVolumePageLocators.DISK_OFFERING, disk_option)

        # Wait for next actions loaded
        time.sleep(2)

        # Once choosing Custom Disk, a size blank should appear
        if (disk_option == CECreateVolumePageLocators.CUSTOM_DISK):
            self.volume_page \
                .fill_form(enter_value, CEVolumePageLocators.SIZE_FORM)

        # Click on Shrink OK or not
        if (condition):
            self.volume_page.choose_Shrink_OK()

        # Click OK
        self.volume_page.click_button(CEVolumePageLocators.OK_BTN)


        time.sleep(2)

        # When the VM is running => Should not resize successfully by all means
        if (self.vm_state == "Running"):
            self.assertTrue(
                self.volume_page.check_size_gb() == self.initial_volume_size,
                "Should fail to resize volume when it is attached to a Running VM"
            )
        # When the VM is stopped
        else:
            # Scenario 8 + 10: Downsize the volume without Shrink OK => Should not resize successfully
            if (enter_value < self.initial_volume_size and condition == False):
                self.assertTrue(
                    self.volume_page.check_size_gb() == self.initial_volume_size,
                    "Should fail to resize volume when downsizing the volume without shrinking it"
                )
            # Other scenarios should be successful by all means
            else:
                self.assertTrue(
                    self.volume_page.check_size_gb() != self.initial_volume_size,
                    "Should successfully resize volume when it is attached to a Stopped VM"
                )

        time.sleep(2)
        self.tearDown()

    """
        TEST CASE A: Click on Shrink OK
    """
    # Choose Custom Disk and click on Shrink OK
    def test_custom_disk_N_shrink(self):
        self.disk_option(CECreateVolumePageLocators.CUSTOM_DISK, True, CEVolumeTestData.SIZE)

    # Choose Default 100G and click on Shrink OK
    def test_default_100G_N_shrink(self):
        self.disk_option(CEVolumePageLocators.DEFAULT_100G, True, 100)

    # Choose 200G and click on Shrink OK
    def test_200G_N_shrink(self):
        self.disk_option(CEVolumePageLocators.OPTION_200G, True, 200)

    # Choose 500G and click on Shrink OK
    def test_500G_N_shrink(self):
        self.disk_option(CEVolumePageLocators.OPTION_500G, True, 500)

    """
        TEST CASE B: Not click on Shrink OK
    """

    # Choose Custom Disk and NOT click on Shrink OK
    def test_custom_disk_no_shrink(self):
        self.disk_option(CECreateVolumePageLocators.CUSTOM_DISK, False, CEVolumeTestData.SIZE)

    # Choose Default 100G and NOT click on Shrink OK
    def test_default_100G_no_shrink(self):
        self.disk_option(CEVolumePageLocators.DEFAULT_100G, False, 100)

    # Choose 200G and NOT click on Shrink OK
    def test_200G_no_shrink(self):
        self.disk_option(CEVolumePageLocators.OPTION_200G, False, 200)

    # Choose 500G and NOT click on Shrink OK
    def test_500G_no_shrink(self):
        self.disk_option(CEVolumePageLocators.OPTION_500G, False, 500)

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
