from Locators.CE import CEInstancePageLocators
from Pages.base_page import BasePage
from Pages.CE.launch_instances_wizard_page import CELaunchInstancesWizardPage
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

    def select_instance(self, instance_id):
        self.find_element(*self.locator.INSTANCE_RADIO_BY_ID(instance_id)).click()
        return self 

    def change_instance_states(self, state_button, confirm_button):
        self\
            .wait_and_click_button(self.locator.INSTANCE_STATE_BTN)\
            .wait_and_click_button(state_button)\
            .wait_and_click_button(confirm_button)
        return self


