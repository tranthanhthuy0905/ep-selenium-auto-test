"""
    This is the base test for volume (in CE_EBS)
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
        All the methods relating to Volume should come here
    """

    def choose_volume(self, disk_option, stop_vm, initial_size, attach_vm):
        if (attach_vm):
        # *** Create simple instance in case user wants to attach volume with an instance ***
            self.launch_instance_01_default_pw()
            time.sleep(2)
            # Stop the VM attached
            if (stop_vm):
                self.ce_instances_page.stop_vm(self.instance_id)

        # *** Direct to CE homepage without creating an instance incase user does not want to attach volume with an instance ***
        else:
            self.ce_homepage = CEHomePage(self.driver)

        # *** Access volume page ***
        self.ce_homepage.access_volumes_page()
        self.volume_page = CEVolumePage(self.driver)
        # Check whether directing to volume page is correct or not
        self.assertEqual(self.driver.current_url, self.volume_page.base_url)
        self.assertTrue(
            self.volume_page.check_element_existence(CEVolumePageLocators.CREATE_VOLUME_BTN)
        )

        # *** Create a volume ***
        time.sleep(2)
        self.volume_page.create_new_volume(initial_size, disk_option)
        # Check whether the information of newly created volume is updated in the list
        self.volume_name = self.volume_page.volume_name
        self.assertTrue(
            self.driver.find_element_by_xpath("//td[contains(.,'" + self.volume_name + "')]/parent::*"),
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
        # Incase user wants to attach volume with instance
        #       Then user should:
        #           - Click on "Attach volume" button on the top right
        #           - Select an existing instance
        #           - Click on OK button
            self.attach_volume_to_instance(self.instance_name)
            # *** Check if the volume is attached with VM successfully or not ***
            time.sleep(10)
            self.volume_page.click_button(
                (By.XPATH, '//span[././input/@type="radio" and ancestor::tr/@data-row-key="' + self.volume_id + '"]'))
            WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element
                                                 (CEVolumePageLocators.VM_ID,
                                                  self.instance_id),
                                                 "Fail to attach the volume with a " + self.instance_state + " VM")


    def attach_volume_to_instance(self, instance_name):
        # *** Attach the volume with VM ***
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(CEVolumePageLocators.ATTACH_VOLUME_BTN))
        # When user clicks on "Attach volume" button

        self.volume_page.click_button(CEVolumePageLocators.ATTACH_VOLUME_BTN)

        # Then user can see a pop-up Attach volume box
        # When user selects one VM in the list suggested in "Select a volume" option
        self.volume_page.find_element(*CEVolumePageLocators.SELECT_AN_INSTANCE) \
            .send_keys(instance_name)
        self.volume_page.find_element(*CEVolumePageLocators.SELECT_AN_INSTANCE) \
            .send_keys(Keys.ENTER)
        # And user clicks on "OK" button
        self.volume_page.click_button(CEVolumePageLocators.ATTACH_OK_BUTTON)

    def detach_volume_from_instance(self, instance_state):
        # When user clicks on "Actions" button on the top right
        # When user clicks on the "Detach volume" option
        # And user clicks on "Detach" button pop-up
        self.volume_page\
            .click_button(CEVolumePageLocators.VOLUME_ACTIONS_BTN)\
            .click_button(CEVolumePageLocators.DETACH_VOLUME_BTN) \
            .click_button(CEVolumePageLocators.DETACH_CONFIRM_BTN)

        # Check whether detach successfully or not
        self.volume_page.click_button((By.XPATH, '//span[././input/@type="radio" and ancestor::tr/@data-row-key="' + self.volume_id + '"]'))
        self.assertTrue(
            self.volume_page.find_element(*CEVolumePageLocators.VM_NAME).text == "-",
            "Fail to detach the volume from its " + instance_state + " instance"
        )
        return self

    def delete_volume(self):
        # When user clicks on "Actions" button on the top right
        # When user clicks on the "Delete volume" option
        # And user clicks on "Delete" button to confirm
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
