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

from Configs.TestData.CESecurityGroupTestData import CESecurityGroupTestData
import os
import unittest

import HtmlTestRunner
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tests.CE.ce_base_test import CEBaseTest
from Pages.CE.homepage import CEHomePage
from Pages.CE.instances_page import CEInstancesPage
from Pages.CE.launch_instances_wizard_page import CELaunchInstancesWizardPage
from Configs.TestData.CEInstanceTestData import CEInstanceTestData
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
        self.assertTrue(self.instances_page.check_element_existence(CEInstancePageLocators.LAUNCH_INSTANCES_BTN))
        # When user clicks on that "Launch instance" button
        self.instances_page.access_launch_instances_wizard_page()
        self.launch_instances_wizard_page = CELaunchInstancesWizardPage(self.driver)
        # Then user can see the wizard form for creating a new instance
        self.assertEqual(self.driver.current_url, self.launch_instances_wizard_page.base_url)
        self.assertTrue(self.launch_instances_wizard_page.check_element_existence(CELaunchInstancesWizardPageLocators.MI_SELECT_BTN))
        
    # Step 1: Choose an Machine Image 
        self.launch_instances_wizard_page.choose_machine_image()

    # Step 2: Choose an Instance Type
        self.launch_instances_wizard_page.choose_instance_type()
        self.launch_instances_wizard_page.click_next_btn()

    # Step 3: Configure Instance Details
        # Set instance name
        instance_name = CEInstanceTestData.INSTANCE_NAME
        self.launch_instances_wizard_page.fill_instance_name(instance_name)
        # Click on "Create new Keypair"
        self.launch_instances_wizard_page.click_button(CELaunchInstancesWizardPageLocators.CREATE_NEW_KEYPAIR_BTN)
        # Fill in the form for creating keypair then click ok
        keypair_name = CEKeypairTestData.KEYPAIR_NAME
        self.launch_instances_wizard_page.fill_keypair_info(keypair_name, "")
        self.launch_instances_wizard_page.click_button(CELaunchInstancesWizardPageLocators.CREATE_NEW_KEYPAIR_OK_BTN)
        # Check the new keypair is created successfully
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CELaunchInstancesWizardPageLocators.CREATE_NEW_KEYPAIR_SUCCESS_MESSAGE))
        # Click on "Close" and 
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CELaunchInstancesWizardPageLocators.CREATE_NEW_KEYPAIR_CLOSE_BTN))
        self.launch_instances_wizard_page.click_button(CELaunchInstancesWizardPageLocators.CREATE_NEW_KEYPAIR_CLOSE_BTN)
        # Fill in "Default Password" and "Confirm Password" 
        self.launch_instances_wizard_page.fill_default_password(CEInstanceTestData.DEFAULT_PASSWORD, CEInstanceTestData.DEFAULT_PASSWORD)
        # Close popup message
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CELaunchInstancesWizardPageLocators.CLOSE_MESSAGE_BTN))
        self.launch_instances_wizard_page.click_button(CELaunchInstancesWizardPageLocators.CLOSE_MESSAGE_BTN)
        # Click on "Next" button
        self.launch_instances_wizard_page.click_next_btn()

    # Step 4: Add Storage
        # Click "Add new Volume" button
        self.launch_instances_wizard_page.click_button(CELaunchInstancesWizardPageLocators.ADD_NEW_VOLUME_BTN)
        # Fill the form and select type of volume
        volume_name = CEVolumeTestData.VOLUME_NAME
        self.launch_instances_wizard_page.fill_volume_info(volume_name=volume_name, volume_size=CEVolumeTestData.SIZE)
        # Click on "Create" button on modal
        self.launch_instances_wizard_page.click_button(CELaunchInstancesWizardPageLocators.CREATE_VOLUME_BTN)
        # Then the new volume is created
        volume_row = self.driver.find_element(*CELaunchInstancesWizardPageLocators.PARRENT_BY_VOLUME_NAME(_volume_name=volume_name))
        volume_id = volume_row.get_attribute("data-row-key")
        self.launch_instances_wizard_page.check_element_existence(CELaunchInstancesWizardPageLocators.CREATE_VOLUME_SUCCESS_MESSAGE)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CELaunchInstancesWizardPageLocators.CLOSE_MESSAGE_BTN))
        # Check if the new volume state is Allocated
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(CELaunchInstancesWizardPageLocators.STATE_BY_ID(volume_id), "Allocated"))
        # Select volume
        self.launch_instances_wizard_page.click_button(CELaunchInstancesWizardPageLocators.RADIO_BY_NAME(volume_id))
        # Close popup message
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CELaunchInstancesWizardPageLocators.CLOSE_MESSAGE_BTN))
        self.launch_instances_wizard_page.click_button(CELaunchInstancesWizardPageLocators.CLOSE_MESSAGE_BTN)
        # Click on "Next" button
        self.launch_instances_wizard_page.click_next_btn()

    # Step 5: Configure Security Group
        # Click on "Create new SG radio"
        self.launch_instances_wizard_page.click_button(CELaunchInstancesWizardPageLocators.CREATE_NEW_SG_RADIO)
        # Fill SG name and description
        self.launch_instances_wizard_page.fill_security_group_info(CESecurityGroupTestData.SECURITY_GROUP_NAME, CESecurityGroupTestData.DESCRIPTION)
        # Click on add SG button
        self.launch_instances_wizard_page.click_button(CELaunchInstancesWizardPageLocators.ADD_SG_BTN)
        # Check if SG created successfully
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CELaunchInstancesWizardPageLocators.CREATE_SG_SUCCESS_MESSAGE))
        # Check on "Apply for this instance"
        self.launch_instances_wizard_page.click_button(CELaunchInstancesWizardPageLocators.SG_APPLY_CHECKBOX)
        # Get SG ID for delete data after test
        sg_id = self.driver.find_element(*CELaunchInstancesWizardPageLocators.SG_DETAILS_ID).text
        # Close popup message
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CELaunchInstancesWizardPageLocators.CLOSE_MESSAGE_BTN))
        self.launch_instances_wizard_page.click_button(CELaunchInstancesWizardPageLocators.CLOSE_MESSAGE_BTN)
        # Click on "Review and launch"
        self.launch_instances_wizard_page.click_button(CELaunchInstancesWizardPageLocators.REVIEW_N_LAUNCH_BTN)

    # Step 6: Review Instance & Launch
        self.launch_instances_wizard_page.click_button(CELaunchInstancesWizardPageLocators.LAUNCH_BTN)

        WebDriverWait(self.driver, 10).until(EC.url_to_be(self.instances_page.base_url))
        instance_row = self.driver.find_element(*CELaunchInstancesWizardPageLocators.PARRENT_BY_INSTANCE_NAME(instance_name))
        instance_id = instance_row.get_attribute("data-row-key")

    
        self.instances_page.check_element_existence(CEInstancePageLocators.ANNOUNCEMENT)
        self.instances_page.check_element_existence(CEInstancePageLocators.LAUNCH_VM_SUCCESS_MESSAGE)

        #TODO Check if the new instance state is Running
        try:
            WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(CELaunchInstancesWizardPageLocators.STATE_BY_ID(instance_id), "Running"))
        except Exception as e:
            print(e)

        #TODO clear test data
        self.delete_CE_instance_by_id(instance_id)
        self.delete_CE_volume_by_id(volume_id)
        self.delete_CE_keypair_by_name(keypair_name)
        self.driver.implicitly_wait(10)
        self.delete_CE_sg_by_id(sg_id)


# python3 -m unittest Tests.CE_Instance.test_launch_instance_02 -v

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )