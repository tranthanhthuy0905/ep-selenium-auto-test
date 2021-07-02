"""
    This test is general to all the scenarios from 3 to 10 to RESIZE volume in CE_EBS
"""
import time

from selenium.webdriver.common.by import By

from Configs.TestData.CEVolumeTestData import CEVolumeTestData
from Locators.CE import CEInstancePageLocators, CEVolumePageLocators
from Pages.CE.create_volume_page import CECreateVolumePage
from Pages.CE.homepage import CEHomePage
from Pages.CE.volume_page import CEVolumePage
from Tests.CE.ce_base_test import CEBaseTest


class VolumeBaseTest(CEBaseTest):
    """
        TEST CASE: All scenarios relating to RESIZE VOLUME
    """

    # def direct_to_volume_page(self):
    #     """
    #         This function includes all steps until user clicks on Resize Volume button:
    #         - Direct to Volume page
    #         - Check the information of the chosen volume: its VM's state, initial volume size
    #         - Click on Resize volume
    #     """
    #
    #     # When user clicks on "Volumes" button on the left side
    #     self.access_volumes_page()
    #
    #     self.volume_page = CEVolumePage(self.driver)
    #     self.assertEqual(self.driver.current_url, self.volume_page.base_url)
    #     self.assertTrue(
    #         self.volume_page.check_element_existence(CEVolumePageLocators.CREATE_VOLUME_BTN)
    #     )
    #
    # def create_volume(self, volume_size):
    #     self\
    #         .direct_to_volume_page()\
    #         .volume_page.click_create_volume_btn()
    #     self.create_volume_page = CECreateVolumePage(self.driver)
    #     self.assertEqual(self.driver.current_url, self.create_volume_page.base_url)
    #
    #     # When user clicks on "Create" button
    #     self.volume_name = CEVolumeTestData.VOLUME_NAME
    #     self.create_volume_page.create_volume(volume_name=self.volume_name, volume_size=volume_size)

    def choose_volume(self, disk_option, stop_vm, initial_size, attach_vm):
    # *** Create simple instance ***
        if (attach_vm):
            self.launch_instance_01_default_pw()
            time.sleep(2)
            # Stop the VM attached
            if (stop_vm):
                self.ce_instances_page.stop_vm(self.instance_id)
        #self.instance_name = launch_instance.instance_name
        else:
            self.ce_homepage = CEHomePage(self.driver)

        time.sleep(2)
        # *** Access volume page ***
        self.ce_homepage.access_volumes_page()
        self.volume_page = CEVolumePage(self.driver)
        self.assertEqual(self.driver.current_url, self.volume_page.base_url)
        self.assertTrue(
            self.volume_page.check_element_existence(CEVolumePageLocators.CREATE_VOLUME_BTN)
        )
        # *** Create a volume ***
        time.sleep(2)
        self.volume_page.create_new_volume(initial_size, disk_option)

        time.sleep(2)
        # Select the newly created volume
        self.volume_id = self.driver.find_element_by_xpath(
            "//td[contains(.,'" + self.volume_page.volume_name + "')]/parent::*").get_attribute("data-row-key")
        self.volume_page.click_button(
            (By.XPATH, '//span[././input/@type="radio" and ancestor::tr/@data-row-key="' + self.volume_id + '"]'))

        time.sleep(2)
        if (attach_vm):
        #     print("Instance name is: ", self.instance_name)
        #     print("Instance state is: ", self.instance_state)
            time.sleep(3)
            self.volume_page.attach_volume_to_instance(self.instance_name, self.instance_state)
