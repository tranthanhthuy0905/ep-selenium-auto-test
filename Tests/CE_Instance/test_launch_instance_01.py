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

import os
import time
import unittest
import HtmlTestRunner

from Tests.base_test import BaseTest
from Pages.ec2.dashboard_page import DashboardPage
from Pages.ec2.ec2_instances_page import EC2InstancesPage
from Pages.ec2.ec2_page import EC2Page
from Pages.ec2.ec2_homepage import EC2HomePage
from Pages.ec2.ec2_launch_instances_wizard_page import EC2LaunchInstancesWizardPage
from Locators.ec2 import EC2LaunchInstancesWizardPageLocators

class Test_launch_instance_01(BaseTest):
    """
        TEST CASE: Launch instance with simple flow (Scenario 01)
    """

    # General method to pass through step 1 & 2 of launching an instance
    def choose_MI_N_Instance_Type(self):

        time.sleep(1)
        # Access to CE main page
        self.ec2_homepage = EC2HomePage(self.driver)

        # Direct to CE Instance page
        # Step 1: User selects "Instances => Instances" on left side menu
        self.ec2_homepage.access_instance_page()
        self.ec2_instances_page = EC2InstancesPage(self.driver)
        self.assertEqual(
            self.driver.current_url, self.ec2_instances_page.base_url
        )

        time.sleep(1)
        # Step 2: Click on "Launch Instance" button
        # Direct to Launch Instance Wizard page
        self.ec2_instances_page.access_launch_instances_wizard_page()
        self.ec2_launch_instances_wizard_page = EC2LaunchInstancesWizardPage(self.driver)
        self.assertEqual(self.driver.current_url, self.ec2_launch_instances_wizard_page.base_url)

        time.sleep(1)
        # Action 3: Select "Ubuntu20_20.04_Stable" image,
        # Select "2G-2Core-2k2" type
        self.ec2_launch_instances_wizard_page.choose_instance_details()
        # Click on "Review and Launch" button
        self.ec2_launch_instances_wizard_page.click_button(EC2LaunchInstancesWizardPageLocators.REVIEW_N_LAUNCH_BTN)
        self.assertEqual(
            self.driver.current_url, self.ec2_launch_instances_wizard_page.base_url
        )

    def test_launch_instance_01_default_pw(self):
        """
            TEST CASE: Apply default password
        """
        # Passing step 1 (Choose MI) and step 2 (Instance Type)
        self.choose_MI_N_Instance_Type()

        time.sleep(1)
        # Click "Apply this password" button,
        # Click "Launch" button
        self.ec2_launch_instances_wizard_page.apply_default_password()
        self.assertEqual(
            self.driver.current_url, self.ec2_launch_instances_wizard_page.base_url
        )
        self.assertTrue(
            self.ec2_launch_instances_wizard_page.check_element_existence(
                EC2LaunchInstancesWizardPageLocators.REVIEW_INSTANCE_LAUNCH)
        )

        # Sleep to wait for the page loading
        time.sleep(3)
        self.tearDown()

    def test_launch_instance_01_edit_valid_pw(self):
        """
            TEST CASE: Edit own default password (matched confirmation password)
        """
        # Passing step 1 (Choose MI) and step 2 (Instance Type)
        self.choose_MI_N_Instance_Type()

        time.sleep(1)
        # Edit own password
        self.ec2_launch_instances_wizard_page.edit_password()
        # Check if click on Edit button, whether come back to "Configure Instance" step or not
        self.assertEqual(
            self.driver.current_url, self.ec2_launch_instances_wizard_page.base_url
        )
        self.assertTrue(
            self.ec2_launch_instances_wizard_page.check_element_existence(
                EC2LaunchInstancesWizardPageLocators.CONFIGURE_INSTANCE_DETAILS)
        )
        time.sleep(1)
        self.ec2_launch_instances_wizard_page.input_password("Abc12345", "Abc12345")
        self.ec2_launch_instances_wizard_page.review_and_launch_instance()

        # Sleep to wait for the page loading
        time.sleep(3)
        self.tearDown()

    def test_launch_instance_01_edit_invalid_pw(self):
        """
            TEST CASE: Edit own default password (unmatched confirmation password)
        """
        # Passing step 1 (Choose MI) and step 2 (Instance Type)
        self.choose_MI_N_Instance_Type()

        time.sleep(1)
        # Edit own password
        self.ec2_launch_instances_wizard_page.edit_password()
        # Check if click on Edit button, whether come back to "Configure Instance" step or not
        self.assertEqual(
            self.driver.current_url, self.ec2_launch_instances_wizard_page.base_url
        )
        self.assertTrue(
            self.ec2_launch_instances_wizard_page.check_element_existence(
                EC2LaunchInstancesWizardPageLocators.CONFIGURE_INSTANCE_DETAILS)
        )
        time.sleep(1)
        self.ec2_launch_instances_wizard_page.input_password("Abc12345", "Abcd12345")

        # Check if there is a reminding message or not
        self.assertTrue(
            self.ec2_launch_instances_wizard_page.check_element_existence(
                EC2LaunchInstancesWizardPageLocators.TWO_PASSWORD_NOT_MATCH)
        )

        # Sleep to wait for the page loading
        time.sleep(3)
        self.tearDown()

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
