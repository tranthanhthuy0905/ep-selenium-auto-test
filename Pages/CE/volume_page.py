from selenium.webdriver.support.wait import WebDriverWait
from Pages.CE.create_volume_page import CECreateVolumePage
from Locators.CE import CEInstancePageLocators, CEVolumePageLocators
from Pages.base_page import BasePage
from Pages.CE.launch_instances_wizard_page import CELaunchInstancesWizardPage
from selenium.webdriver.support import expected_conditions as EC
from Configs import CE_VOLUME_URL


class CEVolumePage(BasePage):
    def __init__(self, driver):
        self.locator = CEVolumePageLocators
        super().__init__(driver, CE_VOLUME_URL)

    def check_volume_state(self, volume_id, state):
        WebDriverWait(self.driver, 300).until(EC.text_to_be_present_in_element(self.locator.VOLUME_STATE_BY_ID(volume_id), state))

        
    def change_instance_states(self, state_button, confirm_button, message):
        self.click_button(self.locator.RADIO_BTN)\
            .click_button(self.locator.INSTANCE_STATE_BTN)\
            .click_button(state_button)\
            .wait_and_click_button(confirm_button)
        if message:
            self.check_element_existence(message)
        return self

    


