"""
Scenario 1: Launch instance with simple flow (Ubuntu 20)
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
	And user can see the "Preview and Launch" button
	When user selects "2G-2Core-2k2" type and clicks on "Preview and Launch" button
	Then user can see a modal for setting default password
	And user can see the "Apply this password" button
	When user clicks "Apply this password" button
	Then user can see the review of current instance in the last step of wizard
	And user can see the "Launch" button in the bottom right corner
	When user clicks "Launch" button
	Then user can see the list of instances which belongs to that user
	And user can see the newly created instance on top of that list
	And user can see the state of that instance is "Starting"
	When the state of that instance is "Running"
	Then the instance is created
"""

from Tests_Dev.CE.ce_base_test import CEBaseTest
import os
import time
import unittest
import HtmlTestRunner

from Tests.base_test import BaseTest
from Pages.CE.instances_page import CEInstancesPage
from Pages.CE.homepage import CEHomePage
from Pages.CE.launch_instances_wizard_page import *
from Locators.CE import CEInstancePageLocators, CELaunchInstancesWizardPageLocators

class Test_launch_instance_01(CEBaseTest):
    """
        TEST CASE: Launch instance with simple flow (Scenario 01)
    """
    
    def test_launch_instance_01_default_pw(self):
        """
            TEST CASE: Apply default password
        """
        instance_name = self.passing_first_two_step()

        self.review_launch_wizard = ReviewLaunchWizardPage(self.driver)
        # Go to the last step
        self.review_launch_wizard.click_review_and_launch_btn()
        # Click "Apply this password" button
        self.review_launch_wizard.click_apply_password()
        # Click "Launch" button
        self.review_launch_wizard.click_launch_instance()
        # check if instance launched successfully
        self.instances_page.check_if_instance_launched_successfully()
        # Get instance id for clear data after test
        self.instance_id = self.instances_page.get_instance_id(instance_name)
        # Check if the new instance state is Running
        self.instances_page.check_instance_state(self.instance_id, CEInstancePageLocators.RUNNING_STATUS)
        print("Instance is created successfully!")

        


    def test_launch_instance_01_edit_valid_pw(self):
        """
            TEST CASE: Edit own default password (matched confirmation password)
        """
        instance_name = self.passing_first_two_step()

        self.review_launch_wizard = ReviewLaunchWizardPage(self.driver)
        # Go to the last step
        self.review_launch_wizard.click_review_and_launch_btn()
        # Edit own password
        self.review_launch_wizard.edit_password()
        # Check if click on Edit button, whether come back to "Configure Instance" step or not
        self.assertTrue(
            self.review_launch_wizard.check_element_existence(
                CELaunchInstancesWizardPageLocators.CONFIGURE_INSTANCE_DETAILS)
        )
        self.review_launch_wizard.input_password("Abc12345", "Abc12345")
         # Go to the last step
        self.review_launch_wizard.click_review_and_launch_btn()
        # Click "Launch" button
        self.review_launch_wizard.click_launch_instance()
        # check if instance launched successfully
        self.instances_page.check_if_instance_launched_successfully()
        # Get instance id for clear data after test
        self.instance_id = self.instances_page.get_instance_id(instance_name)
        # Check if the new instance state is Running
        self.instances_page.check_instance_state(self.instance_id, CEInstancePageLocators.RUNNING_STATUS)
        print("Instance is created successfully!")

    def test_launch_instance_01_edit_invalid_pw(self):
        """
            TEST CASE: Edit own default password (unmatched confirmation password)
        """
        self.passing_first_two_step()

        self.review_launch_wizard = ReviewLaunchWizardPage(self.driver)
        # Go to the last step
        self.review_launch_wizard.click_review_and_launch_btn()
        # Edit own password
        self.review_launch_wizard.edit_password()
        # Check if click on Edit button, whether come back to "Configure Instance" step or not
        self.assertTrue(
            self.review_launch_wizard.check_element_existence(
                CELaunchInstancesWizardPageLocators.CONFIGURE_INSTANCE_DETAILS)
        )
       
        self.review_launch_wizard.input_password("Abc12345", "Abcd12345")

        # Check if there is a reminding message or not
        self.assertTrue(
            self.review_launch_wizard.check_element_existence(
                CELaunchInstancesWizardPageLocators.TWO_PASSWORD_NOT_MATCH)
        )


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
