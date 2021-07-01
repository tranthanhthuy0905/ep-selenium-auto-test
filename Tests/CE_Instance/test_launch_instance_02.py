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
    And user can fill the form and select type of volume
    When user clicks on "Create" button on modal
    Then the new volume is created
    When user selects a volume in Volumes list
    Then the volume is attached to the instance
    When user clicks on "Next" button in the bottom right corner
    Then user can see the Security Group Setting page
    And user can create a security group or select an existing security group
    When user fill the form and clicks on "Add Security Group" button
    Then user can set Ingress and Egress rule
    When user clicks on "Review and Launch" button in the bottom right corner
    Then user can see the review of current instance in the last step of wizard
    And user can see the "Launch" button in the bottom right corner
    When user clicks "Launch" button
    Then user can see the list of instances which belongs to that user
    And user can see the newly created instance on top of that list
    And user can see the state of that instance is "Starting"
    And state of that instance will be "Running" after a few seconds
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
    def test_create_vm_fullInfo(self):
        """
            TEST CASE: Instance should be created successfully with full flow
        """
        self.CE_homepage = CEHomePage(self.driver)
        self.CE_homepage.access_instances_page()

        # When user selects "Instances => Instances" on left side menu
        self.instances_page = CEInstancesPage(self.driver)
        self.assertEqual(self.driver.current_url, self.instances_page.base_url)
        self.assertTrue(
            self.instances_page.check_element_existence(CEInstancePageLocators.LAUNCH_INSTANCES_BTN)
        )
#TODO And user can see the list of instances which belongs to that user

        # When user clicks on that "Launch instance" button
        self.instances_page.access_launch_instances_wizard_page()
        self.launch_instances_wizard_page = CELaunchInstancesWizardPage(self.driver)
        # Then user can see the wizard form for creating a new instance
        self.assertEqual(self.driver.current_url, self.launch_instances_wizard_page.base_url)
        self.assertTrue(
            self.launch_instances_wizard_page.check_element_existence(CELaunchInstancesWizardPageLocators.MI_SELECT_BTN)
        )

        # When user selects "Ubuntu20_20.04_Stable" image
        self.launch_instances_wizard_page.choose_instance_details()
#TODO Then user can see the list of Instance Types in the step 2 of wizard
    

        # When user clicks on "Create new Keypair"
        self.launch_instances_wizard_page.click_button(CELaunchInstancesWizardPageLocators.CREATE_NEW_KEYPAIR_BTN)
#TODO Then user can see a modal form for creating new keypair
        

        # When user fills in the form and clicks on "Ok" button on modal
        keypair_name = CEKeypairTestData.KEYPAIR_NAME
        self.launch_instances_wizard_page.fill_keypair_info(keypair_name, "")
        self.launch_instances_wizard_page.click_button(CELaunchInstancesWizardPageLocators.CREATE_NEW_KEYPAIR_OK_BTN)
        # Then the new keypair is created and added to the instance
        self.assertTrue(self.launch_instances_wizard_page.check_element_existence(CELaunchInstancesWizardPageLocators.CREATE_NEW_KEYPAIR_SUCCESS_MESSAGE))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CELaunchInstancesWizardPageLocators.CREATE_NEW_KEYPAIR_CLOSE_BTN))
        self.launch_instances_wizard_page.click_button(CELaunchInstancesWizardPageLocators.CREATE_NEW_KEYPAIR_CLOSE_BTN)
        self.keypair_name = keypair_name


        # When user fills in "Default Password" and "Confirm Password" 
        self.launch_instances_wizard_page.fill_default_password()
#TODO Then the password for root account is set

        # When user clicks on "Next" button in the bottom right corner
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CELaunchInstancesWizardPageLocators.CLOSE_MESSAGE_BTN))
        self.launch_instances_wizard_page.click_button(CELaunchInstancesWizardPageLocators.CLOSE_MESSAGE_BTN)
        self.launch_instances_wizard_page.click_button(CELaunchInstancesWizardPageLocators.NEXT_BTN)
#TODO Then user can see the list of Volumes in the step 4 of wizard

        # When user clicks "Add new Volume" button
        self.launch_instances_wizard_page.click_button(CELaunchInstancesWizardPageLocators.ADD_NEW_VOLUME_BTN)
#TODO Then user can see a modal form for creating new volume
        # And user can fill the form and select type of volume
        volume_name = CEVolumeTestData.VOLUME_NAME
        self.launch_instances_wizard_page.fill_volume_info(volume_name=volume_name, volume_size=CEVolumeTestData.SIZE)
       
        # When user clicks on "Create" button on modal
        self.launch_instances_wizard_page.click_button(CELaunchInstancesWizardPageLocators.CREATE_VOLUME_BTN)
        # Then the new volume is created
        self.launch_instances_wizard_page.check_element_existence(CELaunchInstancesWizardPageLocators.CREATE_VOLUME_SUCCESS_MESSAGE)
        self.volume_id = self.driver.find_element_by_xpath("//td[contains(.,'" + volume_name +"')]/parent::*").get_attribute("data-row-key")
#TODO When user selects a volume in Volumes list
#TODO Then the volume is attached to the instance 

        # When user clicks on "Next" button in the bottom right corner
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CELaunchInstancesWizardPageLocators.CLOSE_MESSAGE_BTN))
        self.launch_instances_wizard_page.click_button(CELaunchInstancesWizardPageLocators.CLOSE_MESSAGE_BTN)
        self.launch_instances_wizard_page.click_button(CELaunchInstancesWizardPageLocators.NEXT_BTN)
        # instances_page.check_element_existence(CEInstancePageLocators.ANNOUNCEMENT)
        # instances_page.check_element_existence(CEInstancePageLocators.LAUNCH_VM_SUCCESS_MESSAGE)

        time.sleep(3)
        self.delete_CE_volume()
        self.delete_CE_keypair()


# python3 -m unittest Tests.CE_Instance.test_create_vm_full_001 -v

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )