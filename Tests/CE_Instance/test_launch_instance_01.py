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

from Tests.CE.ce_base_test import CEBaseTest
from Pages.CE.instances_page import CEInstancesPage
from Pages.CE.homepage import CEHomePage
from Pages.CE.launch_instances_wizard_page import CELaunchInstancesWizardPage
from Locators.CE import CELaunchInstancesWizardPageLocators

class Test_launch_instance_01(CEBaseTest):
    """
        TEST CASE: Launch instance with simple flow (Scenario 01)
    """

    # General method to pass through step 1 & 2 of launching an instance
    def choose_MI_N_Instance_Type(self):

        time.sleep(1)
        # Access to CE main page
        self.ce_homepage = CEHomePage(self.driver)

        # Direct to CE Instance page
        # Step 1: User selects "Instances => Instances" on left side menu
        self.ce_homepage.access_instances_page()
        self.ce_instances_page = CEInstancesPage(self.driver)
        self.assertEqual(
            self.driver.current_url, self.ce_instances_page.base_url
        )

        time.sleep(1)
        # Step 2: Click on "Launch Instance" button
        # Direct to Launch Instance Wizard page
        self.ce_instances_page.access_launch_instances_wizard_page()
        self.launch_instances_wizard_page = CELaunchInstancesWizardPage(self.driver)
        self.assertEqual(self.driver.current_url, self.launch_instances_wizard_page.base_url)

        time.sleep(1)
        # Action 3: Select "Ubuntu20_20.04_Stable" image,
        # Select "2G-2Core-2k2" type
        self.launch_instances_wizard_page.choose_instance_details()
        # Click on "Review and Launch" button
        self.launch_instances_wizard_page.click_button(CELaunchInstancesWizardPageLocators.REVIEW_N_LAUNCH_BTN)
        self.assertEqual(
            self.driver.current_url, self.launch_instances_wizard_page.base_url
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
        self.launch_instances_wizard_page.apply_default_password()
        self.assertEqual(
            self.driver.current_url, self.launch_instances_wizard_page.base_url
        )
        self.assertTrue(
            self.launch_instances_wizard_page.check_element_existence(
                CELaunchInstancesWizardPageLocators.REVIEW_INSTANCE_LAUNCH)
        )

        # Sleep to wait for the page loading
        time.sleep(3)
        #self.delete_CE_instance()
        self.tearDown()

    def edit_pw(self, value1, value2):
        """
            TEST CASE: Edit own default password (matched confirmation password)
        """
        # Passing step 1 (Choose MI) and step 2 (Instance Type)
        self.choose_MI_N_Instance_Type()

        time.sleep(1)
        # Edit own password
        self.launch_instances_wizard_page.edit_password()
        # Check if click on Edit button, whether come back to "Configure Instance" step or not
        self.assertEqual(
            self.driver.current_url, self.launch_instances_wizard_page.base_url
        )
        self.assertTrue(
            self.launch_instances_wizard_page.check_element_existence(
                CELaunchInstancesWizardPageLocators.CONFIGURE_INSTANCE_DETAILS)
        )
        time.sleep(1)
        self.launch_instances_wizard_page.input_password(value1, value2)

        # Check if there is a reminding message or not
        if (value1 != value2):
            self.assertTrue(
                self.launch_instances_wizard_page.check_element_existence(
                    CELaunchInstancesWizardPageLocators.TWO_PASSWORD_NOT_MATCH)
            )
        # Once two passwords match together, choose to launch instance
        else:
            self.launch_instances_wizard_page.review_and_launch_instance()

        # Sleep to wait for the page loading
        time.sleep(3)
        #self.delete_CE_instance()
        self.tearDown()

    def test_launch_instance_01_edit_valid_pw(self):
        self.edit_pw("Abc12345", "Abc12345")

    def test_launch_instance_01_edit_invalid_pw(self):
        self.edit_pw("Abc12345", "Abcd12345")

    # def test_launch_instance_01_edit_valid_pw(self):
    #     """
    #         TEST CASE: Edit own default password (matched confirmation password)
    #     """
    #     # Passing step 1 (Choose MI) and step 2 (Instance Type)
    #     self.choose_MI_N_Instance_Type()
    #
    #     time.sleep(1)
    #     # Edit own password
    #     self.launch_instances_wizard_page.edit_password()
    #     # Check if click on Edit button, whether come back to "Configure Instance" step or not
    #     self.assertEqual(
    #         self.driver.current_url, self.launch_instances_wizard_page.base_url
    #     )
    #     self.assertTrue(
    #         self.launch_instances_wizard_page.check_element_existence(
    #             CELaunchInstancesWizardPageLocators.CONFIGURE_INSTANCE_DETAILS)
    #     )
    #     time.sleep(1)
    #     self.launch_instances_wizard_page.input_password("Abc12345", "Abc12345")
    #     self.launch_instances_wizard_page.review_and_launch_instance()
    #
    #     # Sleep to wait for the page loading
    #     time.sleep(3)
    #     self.delete_CE_instance()
    #     self.tearDown()

    # def test_launch_instance_01_edit_invalid_pw(self):
    #     """
    #         TEST CASE: Edit own default password (unmatched confirmation password)
    #     """
    #     # Passing step 1 (Choose MI) and step 2 (Instance Type)
    #     self.choose_MI_N_Instance_Type()
    #
    #     time.sleep(1)
    #     # Edit own password
    #     self.launch_instances_wizard_page.edit_password()
    #     # Check if click on Edit button, whether come back to "Configure Instance" step or not
    #     self.assertEqual(
    #         self.driver.current_url, self.launch_instances_wizard_page.base_url
    #     )
    #     self.assertTrue(
    #         self.launch_instances_wizard_page.check_element_existence(
    #             CELaunchInstancesWizardPageLocators.CONFIGURE_INSTANCE_DETAILS)
    #     )
    #     time.sleep(1)
    #     self.launch_instances_wizard_page.input_password("Abc12345", "Abcd12345")
    #
    #     # Check if there is a reminding message or not
    #     self.assertTrue(
    #         self.launch_instances_wizard_page.check_element_existence(
    #             CELaunchInstancesWizardPageLocators.TWO_PASSWORD_NOT_MATCH)
    #     )
    #
    #     # Sleep to wait for the page loading
    #     time.sleep(3)
    #     self.delete_CE_instance()
    #     self.tearDown()

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
