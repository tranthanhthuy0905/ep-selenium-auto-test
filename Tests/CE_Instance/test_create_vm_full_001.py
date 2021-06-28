import os
import unittest

import HtmlTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tests.CE.ce_base_test import CEBaseTest
from Pages.CE.ec2_homepage import EC2HomePage
from Pages.CE.ec2_instances_page import EC2InstancesPage
from Pages.CE.ec2_launch_instances_wizard_page import EC2LaunchInstancesWizardPage
from Configs.TestData.CEVolumeTestData import CEVolumeTestData
from Configs.TestData.CEKeypairTestData import CEKeypairTestData
from Locators.CE import *

import time


class TestInstances(CEBaseTest):
    def test_a_create_vm_fullInfo(self):
        """
            TEST CASE: Instance should be created successfully
        """
        self.EC2_homepage = EC2HomePage(self.driver)
        self.EC2_homepage.access_ec2_instances_page()

        self.ec2_instances_page = EC2InstancesPage(self.driver)
        self.assertEqual(self.driver.current_url, self.ec2_instances_page.base_url)
        self.assertTrue(
            self.ec2_instances_page.check_element_existence(EC2InstancePageLocators.LAUNCH_INSTANCES_BTN)
        )
        self.ec2_instances_page.access_launch_instances_wizard_page()
        self.ec2_launch_instances_wizard_page = EC2LaunchInstancesWizardPage(self.driver)
        self.assertEqual(self.driver.current_url, self.ec2_launch_instances_wizard_page.base_url)

        
        self.assertTrue(
            self.ec2_launch_instances_wizard_page.check_element_existence(EC2LaunchInstancesWizardPageLocators.MI_SELECT_BTN)
        )

        self.ec2_launch_instances_wizard_page.choose_instance_details()
        #self.ec2_launch_instances_wizard_page.choose_keypair()
        keypair_name = CEKeypairTestData.KEYPAIR_NAME
        self.ec2_launch_instances_wizard_page.create_keypair(keypair_name, "")
        self.keypair_name = keypair_name

        self.ec2_launch_instances_wizard_page.fill_default_password()
        time.sleep(5)
        self.ec2_launch_instances_wizard_page.click_button(EC2LaunchInstancesWizardPageLocators.NEXT_BTN)

        volume_name = CEVolumeTestData.VOLUME_NAME
        self.ec2_launch_instances_wizard_page.create_volume(volume_name=volume_name, volume_size=CEVolumeTestData.SIZE)
        self.volume_name = volume_name

        # ec2_instances_page.check_element_existence(EC2InstancePageLocators.ANNOUNCEMENT)
        # ec2_instances_page.check_element_existence(EC2InstancePageLocators.LAUNCH_VM_SUCCESS_MESSAGE)


# python3 -m unittest Tests.CE_Instance.test_create_vm_full_001 -v

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )