"""
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

    def attach_volume_with_vm(self, stop_vm):
        ''' Attach volume with a Running VM '''
        # *** Create simple instance ***
        self.launch_instance_01_default_pw()

        # Stop the VM attached
        if (stop_vm):
            self.ce_instances_page.stop_vm(self.instance_id)

        time.sleep(2)
        # *** Access volume page ***
        self.ce_homepage.access_volumes_page()
        self.volume_page = CEVolumePage(self.driver)
        self.assertEqual(self.driver.current_url, self.volume_page.base_url)
        self.assertTrue(
            self.volume_page.check_element_existence(CEVolumePageLocators.CREATE_VOLUME_BTN)
        )
        # *** Create a volume ***
        self.volume_page.create_new_volume(CEVolumeTestData.SIZE1)

        time.sleep(2)
        # Select the newly created volume
        self.volume_id = self.driver.find_element_by_xpath(
            "//td[contains(.,'" + self.volume_page.volume_name + "')]/parent::*").get_attribute("data-row-key")
        self.volume_page.click_button((By.XPATH, '//span[././input/@type="radio" and ancestor::tr/@data-row-key="' + self.volume_id + '"]'))

        time.sleep(2)
        # *** Attach the volume with the running VM ***
        self.volume_page.click_button(CEVolumePageLocators.ATTACH_VOLUME_BTN)
        self.volume_page.attach_volume_to_instance(self.instance_name)

        # *** Check if the volume is attached with VM successfully or not ***
        self.assertTrue(
            self.volume_page.check_element_existence(
                (By.XPATH,
                 '//td[text()="' + self.instance_name + '" and ancestor::tr/@data-row-key="' + self.volume_name + '"]')),
            "Should successfully attach the volume with a " + vm_state + " VM"
        )

    def test_attach_volume_with_running_vm(self):
        self.attach_volume_with_vm(False)
        time.sleep(2)
