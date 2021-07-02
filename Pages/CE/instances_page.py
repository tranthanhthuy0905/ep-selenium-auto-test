import time

from selenium.webdriver.common.by import By

from Locators.CE import CEInstancePageLocators, CEVolumePageLocators
from Pages.base_page import BasePage
from Pages.CE.launch_instances_wizard_page import CELaunchInstancesWizardPage
from Configs import CE_INSTANCE_URL


class CEInstancesPage(BasePage):
    def __init__(self, driver):
        self.locator = CEInstancePageLocators
        super().__init__(driver, CE_INSTANCE_URL)

    def access_launch_instances_wizard_page(self):
        launch_instances_wizard_page = self.click_button_and_return_page(self.locator.LAUNCH_INSTANCES_BTN, CELaunchInstancesWizardPage(self.driver))
        return launch_instances_wizard_page

    def check_instance_state(self, locator):
        instance_state = self.driver.find_element(*locator).text
        return instance_state

    def change_instance_states(self, instance_id,state_button, confirm_button):
        self.click_button((By.XPATH, '//input[@type="radio" and ancestor::tr/@data-row-key="' + instance_id + '"]'))\
            .click_button(self.locator.INSTANCE_STATE_BTN)\
            .click_button(state_button)\
            .wait_and_click_button(confirm_button)
        # if message:
        #     self.check_element_existence(message)
        # return self
        self

    def stop_vm(self, instance_id):
        self.change_instance_states(instance_id,
                                  CEInstancePageLocators.STOP_INSTANCE_BTN,
                                  CEInstancePageLocators.STOP_CONFIRM_BTN)

        time.sleep(2)
        self.instance_state = self.check_instance_state(CEInstancePageLocators.INSTANCE_STATE)

        self.assertTrue(self.instance_state == "Stopped",
                        "Should successfully stop an instance")

