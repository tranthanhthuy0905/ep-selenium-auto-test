from Pages.CE.create_volume_page import CECreateVolumePage
from Locators.CE import CEInstancePageLocators, CEVolumnePageLocators
from Pages.base_page import BasePage
from Pages.CE.launch_instances_wizard_page import CELaunchInstancesWizardPage
from Configs import CE_VOLUME_URL


class CEVolumePage(BasePage):
    def __init__(self, driver):
        self.locator = CEVolumnePageLocators
        super().__init__(driver, CE_VOLUME_URL)


    def click_create_volume_btn(self):
        self.driver.find_element(*self.locator.CREATE_VOLUME_BTN).click()


    def change_instance_states(self, state_button, confirm_button, message):
        self.click_button(self.locator.RADIO_BTN)\
            .click_button(self.locator.INSTANCE_STATE_BTN)\
            .click_button(state_button)\
            .wait_and_click_button(confirm_button)
        if message:
            self.check_element_existence(message)
        return self


