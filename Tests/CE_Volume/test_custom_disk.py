import os
import time
import unittest

import HtmlTestRunner

from Configs.TestData.CEVolumeTestData import CEVolumeTestData
from Locators.CE import CEInstancePageLocators, CEVolumePageLocators, CECreateVolumePageLocators
from Pages.CE.homepage import CEHomePage
from Pages.CE.volume_page import CEVolumePage
from Tests.CE.ce_base_test import CEBaseTest


class Test_Custom_Disk(CEBaseTest):

    def resize_volume(self):
        # When user clicks on "Volumes" button on the left side
        self.CE_homepage = CEHomePage(self.driver)
        self.CE_homepage.access_volumes_page()

        self.volume_page = CEVolumePage(self.driver)
        self.assertEqual(self.driver.current_url, self.volume_page.base_url)
        self.assertTrue(
            self.volume_page.check_element_existence(CEVolumePageLocators.CREATE_VOLUME_BTN)
        )

        # Checking the size of chosen volume
        # self.volume_size = CEVolumePageLocators.SIZE_GB.value
        # print("Volume size is: ", self.volume_size)

        self.volume_page \
            .click_button(CEInstancePageLocators.RADIO_BTN) \
            .click_button(CEVolumePageLocators.RESIZE_VOLUME_BTN)
        # Check whether popping up "Resize Volume" box or not
        self.assertTrue(
            self.volume_page.check_element_existence(CEVolumePageLocators.RESIZE_VOLUME_BOX)
        )

    def test_custom_disk_shrink_ok(self):

        # Accessing volume page
        self.resize_volume()

        # Choosing Custom Disk option
        time.sleep(2)
        self.volume_page\
            .click_button(CEVolumePageLocators.DISK_OFFERING)\
            .choose_custom_disk(CEVolumePageLocators.DISK_OFFERING)
        self.assertTrue(
            self.volume_page.check_element_existence(CEVolumePageLocators.SIZE_FORM)
        )

        time.sleep(5)
        self.volume_page \
            .fill_form(CEVolumeTestData.SIZE, CEVolumePageLocators.SIZE_FORM)\
            .choose_Shrink_OK()

        # Check whether successfully or not (BUT STILL NOT AVAILABLE TO USE due to the locator)
        self.assertTrue(
            self.volume_page.check_element_existence(CEVolumePageLocators.SUCCESS_RESIZE)
        )
        time.sleep(5)
        self.tearDown()

    def test_default_100G_shrink_ok(self):

        # Accessing volume page
        self.resize_volume()

        # Choosing Custom Disk option
        time.sleep(2)
        self.volume_page\
            .click_button(CEVolumePageLocators.DISK_OFFERING)\
            .choose_default_100G(CEVolumePageLocators.DISK_OFFERING)
        self.assertTrue(
            self.volume_page.check_element_existence(CEVolumePageLocators.DEFAULT_100G)
        )

        time.sleep(2)
        self.volume_page \
            .choose_Shrink_OK()
        self.assertTrue(
            self.volume_page.check_element_existence(CEVolumePageLocators.SUCCESS_RESIZE)
        )
        time.sleep(2)
        self.tearDown()

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
