from selenium.webdriver.common.by import By

from Locators.CE import CEInstancePageLocators, CEVolumePageLocators, CELaunchInstancesWizardPageLocators
from Pages.base_page import BasePage
from Pages.CE.launch_instances_wizard_page import CELaunchInstancesWizardPage, InstanceTypeWizardPage, MachineImageWizardPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Configs import CE_INSTANCE_URL


class CEInstancesPage(BasePage):
    def __init__(self, driver):
        self.locator = CEInstancePageLocators
        super().__init__(driver, CE_INSTANCE_URL)

    def access_launch_instances_wizard_page(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.locator.LAUNCH_INSTANCES_BTN))
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locator.LAUNCH_INSTANCES_BTN))
        launch_instances_wizard_page = self.click_button_and_return_page(self.locator.LAUNCH_INSTANCES_BTN, CELaunchInstancesWizardPage(self.driver))
        return launch_instances_wizard_page

    def check_instance_state(self, instance_id, state):
        WebDriverWait(self.driver, 300).until(EC.text_to_be_present_in_element(self.locator.INSTANCE_STATE_BY_ID(instance_id), state))

    # def check_instance_state(self, locator):
    #     instance_state = self.driver.find_element(*locator).text
    #     return instance_state

    def select_instance(self, instance_id):
        self.find_element(*self.locator.INSTANCE_RADIO_BY_ID(instance_id)).click()
        return self 

    def change_instance_states(self, state_button, confirm_button):
        self.wait_and_click_button(self.locator.INSTANCE_STATE_BTN)
        self.wait_and_click_button(state_button)
        self.wait_and_click_button(confirm_button)
        return self
    
    def stop_instance(self, instance_id):
        # Test completed, stop instance for cleaning test data
        self.select_instance(instance_id)
        self.change_instance_states(self.locator.STOP_INSTANCE_BTN, self.locator.STOP_CONFIRM_BTN)
        print("Instance is stopping")

        # Check if the new instance state is Stopped
        self.check_instance_state(instance_id, CEInstancePageLocators.STOPPED_STATUS)

    def terminate_instance(self, instance_id):
        # Test completed, stop instance for cleaning test data
        self.select_instance(instance_id)
        self.change_instance_states(self.locator.TERMINATE_INSTANCE_BTN, self.locator.TERMINATE_CONFIRM_BTN)
        print("Instance is terminating")

        # Check if the new instance state is terminated
        WebDriverWait(self.driver, 300).until(EC.invisibility_of_element_located(
            CEInstancePageLocators.INSTANCE_STATE_BY_ID(instance_id)))
        if (hasattr(self, "instance_id")):
            delattr(self, "instance_id")


    def stop_vm(self, instance_id):
        self.change_instance_states(instance_id,
                                  CEInstancePageLocators.STOP_INSTANCE_BTN,
                                  CEInstancePageLocators.STOP_CONFIRM_BTN)

        # TODO: Test the instance state (should be Running)
        WebDriverWait(self.driver, 300).until(EC.text_to_be_present_in_element
                                             (CEInstancePageLocators.INSTANCE_STATE_BY_ID(
                                                 instance_id),
                                              "Stopped"),
                                             "Cannot stop the chosen instance")
        self.instance_state =  self.check_instance_state(CEInstancePageLocators.INSTANCE_STATE)

    def select_instance(self, instance_id):
        self.find_element(*self.locator.INSTANCE_RADIO_BY_ID(instance_id)).click()
        return self



    # General method to pass through step 1 & 2 of launching an instance
    def choose_MI_N_Instance_Type(self):

        # Click on "Launch Instance" button
        # Direct to Launch Instance Wizard page
        self.access_launch_instances_wizard_page()
        self.launch_instances_wizard_page = CELaunchInstancesWizardPage(self.driver)

        # Step 1: Choose an Machine Image 
        self.machine_image_wizard = MachineImageWizardPage(self.driver)
        self.machine_image_wizard.choose_machine_image()

        # Step 2: Choose an Instance Type
        self.instances_type_wizard = InstanceTypeWizardPage(self.driver)
        self.instances_type_wizard.choose_instance_type()
        self.instances_type_wizard.click_next_btn()

    def check_if_instance_launched_successfully(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(self.base_url))
        self.check_element_existence(CEInstancePageLocators.ANNOUNCEMENT)
        self.check_element_existence(CEInstancePageLocators.LAUNCH_VM_SUCCESS_MESSAGE)

    def check_if_instance_launched_failed(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CELaunchInstancesWizardPageLocators.FAILED_TO_LAUNCH_NOTI))

    def get_instance_id(self, instance_name):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(self.base_url))
        instance_row = self.driver.find_element(*CELaunchInstancesWizardPageLocators.PARRENT_BY_INSTANCE_NAME(instance_name))
        return instance_row.get_attribute("data-row-key")


    



    




