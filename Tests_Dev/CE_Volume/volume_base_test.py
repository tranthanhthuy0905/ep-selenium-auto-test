"""
    This test is general to all the scenarios from 3 to 10 to RESIZE volume in CE_EBS
"""
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from Configs.TestData.CEVolumeTestData import CEVolumeTestData
from Locators.CE import CEInstancePageLocators, CEVolumePageLocators
from Pages.CE.create_volume_page import CECreateVolumePage
from Pages.CE.homepage import CEHomePage
from Pages.CE.volume_page import CEVolumePage
from Tests_Dev.CE.ce_base_test import CEBaseTest


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

        self.assertTrue(
            self.driver.find_element_by_xpath("//td[contains(.,'" + self.volume_page.volume_name + "')]/parent::*"),
            "Should successfully update newly created volume to the list"
        )

        time.sleep(2)
        # Select the newly created volume
        self.volume_id = self.driver.find_element_by_xpath(
            "//td[contains(.,'" + self.volume_page.volume_name + "')]/parent::*").get_attribute("data-row-key")
        self.volume_page.click_button(
            (By.XPATH, '//span[././input/@type="radio" and ancestor::tr/@data-row-key="' + self.volume_id + '"]'))

        time.sleep(2)
        if (attach_vm):
            self.attach_volume_to_instance(self.instance_name)
            time.sleep(2)
            # *** Check if the volume is attached with VM successfully or not ***
            # self.assertTrue(
            #     self.volume_page.check_element_existence(
            #         (By.XPATH,
            #          '//td[text()="' + self.instance_name + '" and ancestor::tr/@data-row-key="' + self.volume_page.volume_name + '"]')),
            #     "Should successfully attach the volume with a " + self.instance_state + " VM"
            # )
            # self.volume_page.click_button(
            #     (By.XPATH, '//span[././input/@type="radio" and ancestor::tr/@data-row-key="' + self.volume_id + '"]'))
            # self.assertTrue(
            #     self.volume_page.find_element(*CEVolumePageLocators.VM_ID).text == self.instance_id,
            #     "Fail to attach the volume with a " + self.instance_state + " VM"
            # )
            # TODO: Check whether the vm is attached successfully or not

    def attach_volume_to_instance(self, instance_name):
        # *** Attach the volume with the running VM ***
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(CEVolumePageLocators.ATTACH_VOLUME_BTN))
        self.volume_page.click_button(CEVolumePageLocators.ATTACH_VOLUME_BTN)

        self.volume_page.find_element(*CEVolumePageLocators.SELECT_AN_INSTANCE) \
            .send_keys(instance_name)
        self.volume_page.find_element(*CEVolumePageLocators.SELECT_AN_INSTANCE) \
            .send_keys(Keys.ENTER)
        self.volume_page.click_button(CEVolumePageLocators.ATTACH_OK_BUTTON)

    def detach_volume_from_instance(self):
        self.volume_page\
            .click_button(CEVolumePageLocators.VOLUME_ACTIONS_BTN)\
            .click_button(CEVolumePageLocators.DETACH_VOLUME_BTN) \
            .click_button(CEVolumePageLocators.DETACH_CONFIRM_BTN)

        # Check whether detach successfully or not
        self.volume_page.click_button((By.XPATH, '//span[././input/@type="radio" and ancestor::tr/@data-row-key="' + self.volume_id + '"]'))
        self.assertTrue(
            self.volume_page.find_element(*CEVolumePageLocators.VM_NAME).text == "-",
            "Fail to detach the volume from its current instance"
        )
        return self

    def delete_volume(self):
        self.volume_page.click_button(
            (By.XPATH, '//span[././input/@type="radio" and ancestor::tr/@data-row-key="' + self.volume_id + '"]')) \
            .click_button(CEVolumePageLocators.VOLUME_ACTIONS_BTN)\
            .click_button(CEVolumePageLocators.DELETE_VOLUME_BTN)\
            .click_button(CEVolumePageLocators.DELETE_CONFIRM_BUTTON)
        # Check whether delete successfully or not
        self.assertFalse(
            self.volume_page.click_button(
                (By.XPATH, '//span[././input/@type="radio" and ancestor::tr/@data-row-key="' + self.volume_id + '"]')),
            "Fail to delete the chosen volume"
        )
        return self
