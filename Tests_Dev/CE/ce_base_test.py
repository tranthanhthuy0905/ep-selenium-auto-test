import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Configs.TestData.CEVolumeTestData import CEVolumeTestData
from Locators.CE import CELaunchInstancesWizardPageLocators, CEInstancePageLocators
from Pages.CE.create_volume_page import CECreateVolumePage
from Pages.CE.homepage import CEHomePage
from Pages.CE.instances_page import CEInstancesPage
from Pages.CE.launch_instances_wizard_page import CELaunchInstancesWizardPage
from Tests_Dev.base_test import BaseTest
from Configs import *

class CEBaseTest(BaseTest):
    # General method to pass through step 1 & 2 of launching an instance
    def choose_MI_N_Instance_Type(self):

        time.sleep(2)
        # Access to CE main page
        self.ce_homepage = CEHomePage(self.driver)

        # Direct to CE Instance page
        # Step 1: User selects "Instances => Instances" on left side menu
        self.ce_homepage.access_instances_page()
        self.ce_instances_page = CEInstancesPage(self.driver)
        self.assertEqual(
            self.driver.current_url, self.ce_instances_page.base_url
        )

        time.sleep(2)
        # Step 2: Click on "Launch Instance" button
        # Direct to Launch Instance Wizard page
        self.ce_instances_page.access_launch_instances_wizard_page()
        self.launch_instances_wizard_page = CELaunchInstancesWizardPage(self.driver)
        self.assertEqual(self.driver.current_url, self.launch_instances_wizard_page.base_url)


        # Action 3: Select "Ubuntu20_20.04_Stable" image,
        # Select "2G-2Core-2k2" type
        time.sleep(3)
        self.launch_instances_wizard_page.choose_instance_details()
        self.instance_name = self.launch_instances_wizard_page.instance_name
        # Click on "Review and Launch" button
        self.launch_instances_wizard_page.click_button(CELaunchInstancesWizardPageLocators.REVIEW_N_LAUNCH_BTN)
        self.assertEqual(
            self.driver.current_url, self.launch_instances_wizard_page.base_url
        )

    def launch_instance_01_default_pw(self):
        """
            TEST CASE: Apply default password
        """
        # Passing step 1 (Choose MI) and step 2 (Instance Type)
        self.choose_MI_N_Instance_Type()

        time.sleep(3)
        # Click "Apply this password" button,
        # Click "Launch" button
        self.launch_instances_wizard_page.apply_default_password()
        self.assertEqual(
            self.driver.current_url, self.launch_instances_wizard_page.base_url
        )
        # Check whether after apply default key, it comes back to review page before launching instance
        self.assertTrue(
            self.launch_instances_wizard_page.check_element_existence(
                CELaunchInstancesWizardPageLocators.REVIEW_INSTANCE_LAUNCH)
        )

        # Sleep to wait for the page loading
        time.sleep(2)

        # Check whether successfully creating an instance with simple flow (default password) or not
        self.assertTrue(
            self.launch_instances_wizard_page.check_element_existence(
                (By.XPATH, "//td[contains(.,'" + self.instance_name + "')]")),
            "Should successfully create an instance by adding default password by updating new instance to the list"
        )

        self.instance_id = self.driver.find_element_by_xpath(
            "//td[contains(.,'" + self.instance_name + "')]/parent::*").get_attribute("data-row-key")

        time.sleep(2)
        # TODO: Test the instance state (should be Running)
        WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element
                                             (CELaunchInstancesWizardPageLocators.INSTANCE_STATE_BY_ID(self.instance_id),
                                               "Running"),
                                             "Cannot run the newly created instance")
        self.ce_instances_page.click_button(
            (By.XPATH, '//span[././input/@type="radio" and ancestor::tr/@data-row-key="' + self.instance_id + '"]'))
        self.instance_state = self.ce_instances_page.check_instance_state(CEInstancePageLocators.INSTANCE_STATE)


    def delete_CE_instance(self):
        try:
            url = CE_INSTANCE_API_CLIENT_URL + "destroy"
            params = {
                "id": self.service_slug
            }
            self._call_request_delete(url, params, CE_USER_TOKEN)

        except Exception as e:
            print("Can't delete CE instance", str(e))

    def delete_CE_instance_by_id(self, instance_id):
        try:
            url = CE_INSTANCE_API_CLIENT_URL + "destroy"
            params = {
                "id": instance_id
            }
            self._call_request_delete(url, params, CE_USER_TOKEN)

        except Exception as e:
            print("Can't delete CE instance", str(e))


    def delete_CE_volume_by_id(self, volume_id):
        try:
            url = CE_VOLUME_API_CLIENT_URL + "destroy"
            params = {
                "id": volume_id,
                "expunge" : True
            }
            self._call_request_delete(url, params, CE_USER_TOKEN)
        except Exception as e:
            print("Can't delete CE volume", str(e))

    def delete_CE_keypair_by_name(self, keypair_name):
        try:
            url = CE_KEYPAIR_API_CLIENT_URL + keypair_name
            self._call_request_delete(url, {}, CE_USER_TOKEN)
        except Exception as e:
            print("Can't delete CE keypair", str(e))

    def delete_CE_sg_by_id(self, sg_id):
        try:
            url = CE_SECURITY_GROUP_API_CLIENT_URL
            params = {
                "id": sg_id,
            }
            self._call_request_delete(url, params, CE_USER_TOKEN)
        except Exception as e:
            print("Can't delete CE security group", str(e))


