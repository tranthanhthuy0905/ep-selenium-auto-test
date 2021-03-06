'''
Scenarior 4. Launch instance without selecting keypair
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

from Tests_Dev.CE.ce_base_test import CEBaseTest
from Pages.CE.homepage import CEHomePage
from Pages.CE.instances_page import CEInstancesPage
from Pages.CE.launch_instances_wizard_page import *
from Configs.TestData.CEInstanceTestData import CEInstanceTestData
from Configs.TestData.CEVolumeTestData import CEVolumeTestData
from Configs.TestData.CEKeypairTestData import CEKeypairTestData
from Locators.CE import *

import time


class TestInstances04(CEBaseTest):
    def test_create_vm_without_selecting_keypair(self):
        """
            TEST CASE: Launch instance without selecting keypair
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
        self.machine_image_wizard = MachineImageWizardPage(self.driver)
        self.machine_image_wizard.choose_machine_image()
        time.sleep(3)
        

    # Step 2: Choose an Instance Type
        self.instances_type_wizard = InstanceTypeWizardPage(self.driver)
        self.instances_type_wizard.choose_instance_type()
        self.instances_type_wizard.click_next_btn()

    # Step 3: Configure Instance Details
        self.configure_instance_wizard = ConfigureInstanceWizardPage(self.driver)
        # Set instance name
        instance_name = CEInstanceTestData.gen_instance_name()
        self.configure_instance_wizard.fill_instance_name(instance_name)

        # Without Creating keypair

        # Set default password
        self.configure_instance_wizard.fill_default_password(CEInstanceTestData.DEFAULT_PASSWORD, CEInstanceTestData.DEFAULT_PASSWORD)

        self.configure_instance_wizard.click_next_btn()

    # Step 4: Add Storage
        volume_name = CEVolumeTestData.gen_volume_name()
        self.add_storage_wizard = AddStorageWizardPage(self.driver)
        self.add_storage_wizard.add_new_volume(volume_name, CEVolumeTestData.SIZE)

        # Get Volume ID for delete data after test
        self.volume_id = self.add_storage_wizard.get_volume_id(volume_name)

        # Select volume to attach to instance
        self.add_storage_wizard.select_volume(self.volume_id)

        self.add_storage_wizard.click_next_btn()

    # Step 5: Configure Security Group
        self.configure_security_wizard = SecurityGroupWizardPage(self.driver)
        self.configure_security_wizard.create_new_security_group(CESecurityGroupTestData.gen_SG_name(), CESecurityGroupTestData.DESCRIPTION)
        self.configure_security_wizard.apply_sg_for_instance()

        # Get SG ID for delete data after test
        self.sg_id = self.driver.find_element(*CELaunchInstancesWizardPageLocators.SG_DETAILS_ID).text
        self.configure_security_wizard.click_button(CELaunchInstancesWizardPageLocators.REVIEW_N_LAUNCH_BTN)

    # Step 6: Review Instance & Launch
        self.review_launch_wizard = ReviewLaunchWizardPage(self.driver)
        self.review_launch_wizard.click_launch_instance()

        self.instances_page.check_if_instance_launched_successfully()

        # Get instance id for clear data after test
        self.instance_id = self.instances_page.get_instance_id(instance_name)

        # Check if the new instance state is Running
        self.instances_page.check_instance_state(self.instance_id, CEInstancePageLocators.RUNNING_STATUS)
        print("Instance is created successfully!")

        # Test completed, stop instance for cleaning test data
        self.instances_page.stop_instance(self.instance_id)



# python3 -m unittest Tests.CE_Instance.test_launch_instance_04 -v

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
