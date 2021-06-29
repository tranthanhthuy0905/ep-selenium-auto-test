'''
Scenario 2: Launch instance with full flow  (Ubuntu 20)
    Given a certain user
    When user wants to launch an instance
    Then user selects "Instances => Instances" on left side menu
    And user can see the list of instances which belongs to that user
    And user can see the "Launch instance" button on top right corner
    When user clicks on that "Launch instance" button
    Then user can see the wizard form for creating a new instance
    And user can see the list of OS images in the step 1 of wizard
    When user selects "Ubuntu20_20.04_Stable" image
    Then user can see the list of Instance Types in the step 2 of wizard
    And user can see the "Next" button in the bottom right corner
    When user selects "2G-2Core-2k2" type and clicks on "Next" button
    Then user can see the Configure Instance Details form in the step 3 of wizard
    And user can change details of the current instance
    When user clicks on "Create new Keypair"
    Then user can see a modal form for creating new keypair
    When user fills in the form and clicks on "Ok" button on modal
    Then the new keypair is created and added to the instance
    When user fills in "Default Password" and "Confirm Password" 
    Then the password for root account is set
    When user clicks on "Next" button in the bottom right corner
    Then user can see the list of Volumes in the step 4 of wizard
    When user clicks "Add new Volume" button
    Then user can see a modal form for creating new volume
    When user clicks on "Create" button on modal
    Then the new volume is created and attached to the instance
    When user clicks on "Next" button in the bottom right corner
    Then user can see the Security Group Setting page
    And user can create a security group or choose from select an existing security group
    When user clicks on "Review and Launch" button in the bottom right corner
    Then user can see the review of current instance in the last step of wizard
    And user can see the "Launch" button in the bottom right corner
    When user clicks "Launch" button
    Then user can see the list of instances which belongs to that user
    And user can see the newly created instance on top of that list
    And user can see the state of that instance is "Starting"
    When the state of that instance is "Running"
    Then the instance is created
'''

import os
import unittest

import HtmlTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tests.CE.ce_base_test import CEBaseTest
from Pages.CE.homepage import CEHomePage
from Pages.CE.instances_page import CEInstancesPage
from Pages.CE.launch_instances_wizard_page import CELaunchInstancesWizardPage
from Configs.TestData.CEVolumeTestData import CEVolumeTestData
from Configs.TestData.CEKeypairTestData import CEKeypairTestData
from Locators.CE import *

import time


class TestInstances(CEBaseTest):
    def test_a_create_vm_fullInfo(self):
        """
            TEST CASE: Instance should be created successfully
        """
        self.CE_homepage = CEHomePage(self.driver)
        self.CE_homepage.access_instances_page()

        # When user selects "Instances => Instances" on left side menu
        self.instances_page = CEInstancesPage(self.driver)
        self.assertEqual(self.driver.current_url, self.instances_page.base_url)
        self.assertTrue(
            self.instances_page.check_element_existence(CEInstancePageLocators.LAUNCH_INSTANCES_BTN)
        )

        # When user clicks on that "Launch instance" button
        self.instances_page.access_launch_instances_wizard_page()
        self.launch_instances_wizard_page = CELaunchInstancesWizardPage(self.driver)
        self.assertEqual(self.driver.current_url, self.launch_instances_wizard_page.base_url)

        
        self.assertTrue(
            self.launch_instances_wizard_page.check_element_existence(CELaunchInstancesWizardPageLocators.MI_SELECT_BTN)
        )
        # When user selects "Ubuntu20_20.04_Stable" image
        self.launch_instances_wizard_page.choose_instance_details()

        # TODO: 
        # keypair_name = CEKeypairTestData.KEYPAIR_NAME
        # self.launch_instances_wizard_page.create_keypair(keypair_name, "")
        # self.assertTrue(
        #     self.launch_instances_wizard_page.check_element_existence(CELaunchInstancesWizardPageLocators.CREATE_NEW_KEYPAIR_SUCCESS_MESSAGE)
        # )
        # self.launch_instances_wizard_page.click_button(CELaunchInstancesWizardPageLocators.CREATE_NEW_KEYPAIR_CLOSE_BTN)
        # self.keypair_name = keypair_name

        # self.launch_instances_wizard_page.fill_default_password()
        # time.sleep(2)

        # self.launch_instances_wizard_page.click_button(CELaunchInstancesWizardPageLocators.NEXT_BTN)

        # volume_name = CEVolumeTestData.VOLUME_NAME
        # self.launch_instances_wizard_page.create_volume(volume_name=volume_name, volume_size=CEVolumeTestData.SIZE)
        # self.volume_name = volume_name

        # instances_page.check_element_existence(CEInstancePageLocators.ANNOUNCEMENT)
        # instances_page.check_element_existence(CEInstancePageLocators.LAUNCH_VM_SUCCESS_MESSAGE)


# python3 -m unittest Tests.CE_Instance.test_create_vm_full_001 -v

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )