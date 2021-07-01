"""
    This test is general to all the scenarios from 3 to 10 to RESIZE volume in CE_EBS
"""
import time

from Locators.CE import CEInstancePageLocators, CEVolumePageLocators
from Pages.CE.homepage import CEHomePage
from Pages.CE.volume_page import CEVolumePage
from Tests.CE.ce_base_test import CEBaseTest


class VolumeBaseTest(CEBaseTest):
    """
        TEST CASE: All scenarios relating to RESIZE VOLUME
    """

    # def _create_volume(self):
    #     pass
    #
    # def create_attached_volume(self):
    #     instance_name = self.create_simple_instance()
    #     volume_name = self._create_volume()
    #     self.attach_volume_to_instance(volume_name)
    #
    # def create_unattached_volume(self):
    #     pass

    def access_volume_page(self):
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
    #
    # def check_info_volume(self):
    #     # list = self.driver.find_element(*CEVolumePageLocators.VOLUME_LIST).text
    #     # print("List volume is: ", list)
    #     # self.assertTrue(
    #     #     self.driver.find_element(*CEVolumePageLocators.VOLUME_LIST).text != None,
    #     #     "Cannot resize volume once there is no existing volume"
    #     # )
    #     # if (self.driver.find_element(*CEVolumePageLocators.VOLUME_LIST).text != None):

        # Choose one volume in the list
        self.volume_page.click_button(CEInstancePageLocators.RADIO_BTN)

        # Check volume to be attached with VM or not
        time.sleep(2)
        self.vm_id = self.driver.find_element(*CEVolumePageLocators.VM_ID).text

        if (self.vm_id != "-"):
            # Check volume's VM state
            self.vm_state = self.volume_page.check_instance_state()

        # Check volume's initial size
        self.initial_volume_size = self.volume_page.check_size_gb()


