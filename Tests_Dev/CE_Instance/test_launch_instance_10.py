'''
Scenario 10. Launch instance with existing volume then click on "Preview and Launch"
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
	When user selects a Volume in the list
	Then the selected volume is attached to the instance
	When user clicks on "Review and Launch" button in the bottom right corner
	Then user can see the review of current instance in the last step of wizard
	And the current instance is assigned to default security group
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
from Pages.CE.volume_page import CEVolumePage
from Pages.CE.create_volume_page import CECreateVolumePage
from Pages.CE.launch_instances_wizard_page import *
from Configs.TestData.CEInstanceTestData import CEInstanceTestData
from Configs.TestData.CEVolumeTestData import CEVolumeTestData
from Configs.TestData.CEKeypairTestData import CEKeypairTestData
from Locators.CE import *

import time


class TestInstances(CEBaseTest):
    def test_create_vm_with_existing_volume_then_launch(self):
        """
            TEST CASE: Launch instance with existing volume then click on "Preview and Launch"
        """
        self.CE_homepage = CEHomePage(self.driver)
        # first create a volume
        self.CE_homepage.access_volumes_page()
        # Then user can see the list of available Volumes
        self.volume_page = CEVolumePage(self.driver)
        self.assertEqual(self.driver.current_url, self.volume_page.base_url)
        self.assertTrue(self.volume_page.check_element_existence(CEVolumePageLocators.CREATE_VOLUME_BTN))
        self.assertTrue(self.volume_page.check_element_existence(CEVolumePageLocators.VOLUMES_LIST))

        # When user clicks on "Create Volume" button on the top right
        self.volume_page.click_button(CEVolumePageLocators.CREATE_VOLUME_BTN)
        #Then user can move to "Create New Volume" page
        self.create_volume_page = CECreateVolumePage(self.driver)
        self.assertEqual(self.driver.current_url, self.create_volume_page.base_url)
        # And user can fill in Volume name and select volume type
        self.volume_name = CEVolumeTestData.VOLUME_NAME
        self.create_volume_page.fill_volume_info(self.volume_name, volume_size=CEVolumeTestData.SIZE)

        # When user clicks on "Create Volume" button
        self.create_volume_page.click_button(CECreateVolumePageLocators.CREATE_VOLUME_BTN)
        # Then user can see the newly created volume updated in the list of volumes (status: Allocated)
        WebDriverWait(self.driver, 10).until(EC.url_to_be(self.volume_page.base_url))
        volume_row = self.driver.find_element(*CECreateVolumePageLocators.PARRENT_BY_VOLUME_NAME(self.volume_name))
        self.volume_id = volume_row.get_attribute("data-row-key")
        self.volume_page.check_volume_state(self.volume_id, CEVolumeTestData.ALLOCATED)
        self.driver.find_element(*(CEVolumePageLocators.CLOSE_MESSAGE_BTN)).click()

        # Move to instance page
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

    # Step 2: Choose an Instance Type
        self.instances_type_wizard = InstanceTypeWizardPage(self.driver)
        self.instances_type_wizard.choose_instance_type()
        self.instances_type_wizard.click_next_btn()

    # Step 3: Configure Instance Details
        self.configure_instance_wizard = ConfigureInstanceWizardPage(self.driver)
        # Set instance name
        instance_name = CEInstanceTestData.INSTANCE_NAME
        self.configure_instance_wizard.fill_instance_name(instance_name)

        # Create keypair
        self.keypair_name = CEKeypairTestData.KEYPAIR_NAME
        self.configure_instance_wizard.create_new_keypair(self.keypair_name, "")

        # Set default password
        self.configure_instance_wizard.fill_default_password(CEInstanceTestData.DEFAULT_PASSWORD, CEInstanceTestData.DEFAULT_PASSWORD)

        self.configure_instance_wizard.click_next_btn()

    # Step 4: Add Storage
        self.add_storage_wizard = AddStorageWizardPage(self.driver)

        # Select volume to attach to instance
        self.add_storage_wizard.select_volume(self.volume_id)

        self.add_storage_wizard.click_button(CELaunchInstancesWizardPageLocators.REVIEW_N_LAUNCH_BTN)



    # Step 6: Review Instance & Launch
        self.review_launch_wizard = ReviewLaunchWizardPage(self.driver)
        self.review_launch_wizard.launch_instance()

        # Get instance id for clear data after test
        WebDriverWait(self.driver, 10).until(EC.url_to_be(self.instances_page.base_url))
        instance_row = self.driver.find_element(*CELaunchInstancesWizardPageLocators.PARRENT_BY_INSTANCE_NAME(instance_name))
        self.instance_id = instance_row.get_attribute("data-row-key")

        self.instances_page.check_element_existence(CEInstancePageLocators.ANNOUNCEMENT)
        self.instances_page.check_element_existence(CEInstancePageLocators.LAUNCH_VM_SUCCESS_MESSAGE)

        # Check if the new instance state is Running
        self.instances_page.check_instance_state(self.instance_id, CEInstancePageLocators.RUNNING_STATUS)
        print("Instance is created successfully!")



# python3 -m unittest Tests.CE_Instance.test_launch_instance_10 -v




if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
