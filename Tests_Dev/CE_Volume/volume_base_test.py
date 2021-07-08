"""
    This is the base test for volume (in CE_EBS)
"""
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from Configs.TestData.CEVolumeTestData import CEVolumeTestData
from Locators.CE import CEInstancePageLocators, CEVolumePageLocators, CELaunchInstancesWizardPageLocators
from Pages.CE.create_volume_page import CECreateVolumePage
from Pages.CE.homepage import CEHomePage
from Pages.CE.instances_page import CEInstancesPage
from Pages.CE.launch_instances_wizard_page import CELaunchInstancesWizardPage
from Pages.CE.volume_page import CEVolumePage
from Tests.CE.ce_base_test import CEBaseTest


class VolumeBaseTest(CEBaseTest):
    """
        All the methods relating to Volume should come here
    """

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

        # Click "Apply this password" button,
        # Click "Launch" button
        wait = WebDriverWait(self.driver, 50)
        wait.until(EC.element_to_be_clickable(CELaunchInstancesWizardPageLocators.APPLY_THIS_PASSWORD),
                   'Cannot apply default password because "Apply this password" button is not clickable. Maybe it requires more time to wait')
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
        time.sleep(5)

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
                                             (CEInstancePageLocators.INSTANCE_STATE_BY_ID(
                                                 self.instance_id),
                                              "Running"),
                                             "Cannot run the newly created instance")
        self.ce_instances_page.click_button(
            (By.XPATH, '//span[././input/@type="radio" and ancestor::tr/@data-row-key="' + self.instance_id + '"]'))
        self.instance_state = self.ce_instances_page.check_instance_state(CEInstancePageLocators.INSTANCE_STATE)

    def choose_volume(self, disk_option, stop_vm, initial_size, attach_vm):
        initial_size = int(initial_size)
        if (attach_vm):
        # *** Create simple instance in case user wants to attach volume with an instance ***
            self.launch_instance_01_default_pw()
            time.sleep(2)
            # Stop the VM attached
            if (stop_vm):
                self.ce_instances_page.stop_vm(self.instance_id)

        # *** Direct to CE homepage without creating an instance incase user does not want to attach volume with an instance ***
        else:
            self.ce_homepage = CEHomePage(self.driver)

        # *** Access volume page ***
        self.ce_homepage.access_volumes_page()
        self.volume_page = CEVolumePage(self.driver)
        # Check whether directing to volume page is correct or not
        self.assertEqual(self.driver.current_url, self.volume_page.base_url)
        self.assertTrue(
            self.volume_page.check_element_existence(CEVolumePageLocators.CREATE_VOLUME_BTN)
        )

        # *** Create a volume ***
        time.sleep(2)
        self.volume_page.create_new_volume(initial_size, disk_option)
        # Check whether the information of newly created volume is updated in the list
        self.volume_name = self.volume_page.volume_name
        self.assertTrue(
            self.driver.find_element_by_xpath("//td[contains(.,'" + self.volume_name + "')]/parent::*"),
            "Should successfully update newly created volume to the list"
        )

        time.sleep(2)
        # Select the newly created volume
        self.volume_id = self.driver.find_element_by_xpath(
            "//td[contains(.,'" + self.volume_page.volume_name + "')]/parent::*").get_attribute("data-row-key")
        self.volume_page.click_button(
            (By.XPATH, '//span[././input/@type="radio" and ancestor::tr/@data-row-key="' + self.volume_id + '"]'))

        time.sleep(2)
        if (attach_vm):
        # Incase user wants to attach volume with instance
        #       Then user should:
        #           - Click on "Attach volume" button on the top right
        #           - Select an existing instance
        #           - Click on OK button
            self.attach_volume_to_instance(self.instance_name)
            # *** Check if the volume is attached with VM successfully or not ***
            time.sleep(10)
            self.volume_page.click_button(
                (By.XPATH, '//span[././input/@type="radio" and ancestor::tr/@data-row-key="' + self.volume_id + '"]'))
            WebDriverWait(self.driver, 30).until(EC.text_to_be_present_in_element
                                                 (CEVolumePageLocators.VM_ID,
                                                  self.instance_id),
                                                 "Fail to attach the volume with a " + self.instance_state + " VM")


    def attach_volume_to_instance(self, instance_name):
        # *** Attach the volume with VM ***
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(CEVolumePageLocators.ATTACH_VOLUME_BTN))
        # When user clicks on "Attach volume" button

        self.volume_page.click_button(CEVolumePageLocators.ATTACH_VOLUME_BTN)

        # Then user can see a pop-up Attach volume box
        # When user selects one VM in the list suggested in "Select a volume" option
        self.volume_page.find_element(*CEVolumePageLocators.SELECT_AN_INSTANCE) \
            .send_keys(instance_name)
        self.volume_page.find_element(*CEVolumePageLocators.SELECT_AN_INSTANCE) \
            .send_keys(Keys.ENTER)
        # And user clicks on "OK" button
        self.volume_page.click_button(CEVolumePageLocators.ATTACH_OK_BUTTON)

    def detach_volume_from_instance(self, instance_state):
        # When user clicks on "Actions" button on the top right
        # When user clicks on the "Detach volume" option
        # And user clicks on "Detach" button pop-up
        self.volume_page.click_button(CEVolumePageLocators.VOLUME_ACTIONS_BTN)
        time.sleep(2)
        if instance_state == "":
            WebDriverWait(self.driver, 10).until(
                EC.invisibility_of_element_located(CEVolumePageLocators.DETACH_VOLUME_BTN),
                "Should FAIL to detach the volume NOT attached to any instance")
        else:
            self.volume_page\
                .click_button(CEVolumePageLocators.DETACH_VOLUME_BTN) \
                .click_button(CEVolumePageLocators.DETACH_CONFIRM_BTN)

            time.sleep(10)
            # Check whether detach successfully or not
            self.volume_page.click_button((By.XPATH, '//span[././input/@type="radio" and ancestor::tr/@data-row-key="' + self.volume_id + '"]'))
            instance_name = self.driver.find_element_by_xpath("//span//span[ancestor::div/div/div/div/div/text()='VM name']").text
            self.assertTrue(
                instance_name == "-",
                "Fail to detach the volume from its " + instance_state + " instance"
            )
        return self

    def delete_volume(self, no_vm):
        # When user clicks on "Actions" button on the top right
        # When user clicks on the "Delete volume" option
        # And user clicks on "Delete" button to confirm
        self.volume_page.click_button(CEVolumePageLocators.VOLUME_ACTIONS_BTN)
        if no_vm:
            self.volume_page\
                .click_button(CEVolumePageLocators.DELETE_VOLUME_BTN)\
                .click_button(CEVolumePageLocators.DELETE_CONFIRM_BUTTON)

            time.sleep(3)
            # Check whether delete successfully or not
            # TODO: Check whether delete successfully
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH,
                                                                                     "//td[contains(.,'" + self.volume_name + "')]/parent::*")),
                                                 "Should SUCCEED to delete volume NOT attached to any instance")
        else:
            WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(CEVolumePageLocators.DELETE_VOLUME_BTN),
                "Should FAIL to delete the volume attached with an instance")
        return self
