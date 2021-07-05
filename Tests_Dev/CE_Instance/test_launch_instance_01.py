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

from selenium.webdriver.common.by import By
from Tests_Dev.CE.ce_base_test import CEBaseTest
from Pages.CE.instances_page import CEInstancesPage
from Pages.CE.homepage import CEHomePage
from Pages.CE.launch_instances_wizard_page import *
from Locators.CE import CELaunchInstancesWizardPageLocators

class Test_launch_instance_01(CEBaseTest):
    """
        TEST CASE: Launch instance with simple flow (Scenario 01)
    """

    def test_launch_instance_01_default_pw(self):
        """
            TEST CASE: Apply default password
        """
        self.launch_instance_01_default_pw()
        self.delete_CE_instance()
        time.sleep(2)

    # def edit_pw(self, value1, value2):
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
    #     self.launch_instances_wizard_page.input_password(value1, value2)
    #
    #     # Check if there is a reminding message or not
    #     if (value1 != value2):
    #         self.assertTrue(
    #             self.launch_instances_wizard_page.check_element_existence(
    #                 CELaunchInstancesWizardPageLocators.TWO_PASSWORD_NOT_MATCH)
    #         )
    #     # Once two passwords match together, choose to launch instance
    #     else:
    #         self.launch_instances_wizard_page.review_and_launch_instance()
    #         # Check whether successfully creating an instance with simple flow (own password) or not
    #         time.sleep(2)
    #         self.assertTrue(
    #             self.launch_instances_wizard_page.check_element_existence(
    #                 (By.XPATH, "//td[contains(.,'" + self.instance_name + "')]")),
    #             "Should successfully create an instance by editing own password"
    #         )
    #     # Sleep to wait for the page loading
    #     time.sleep(3)
    #     #self.delete_CE_instance()
    #     self.tearDown()
    #
    # def test_launch_instance_01_edit_valid_pw(self):
    #     """
    #         TEST CASE: Edit own default password (matched confirmation password)
    #     """
    #     self.edit_pw("Abc12345", "Abc12345")
    #
    # def test_launch_instance_01_edit_invalid_pw(self):
    #     """
    #         TEST CASE: Edit own default password (unmatched confirmation password)
    #     """
    #     self.edit_pw("Abc12345", "Abcd12345")

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
