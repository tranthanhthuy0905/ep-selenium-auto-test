from Pages.CE.create_volume_page import CECreateVolumePage
from Locators.CE import CEInstancePageLocators, CEVolumePageLocators, CECreateVolumePageLocators
from Pages.base_page import BasePage
from Pages.CE.launch_instances_wizard_page import CELaunchInstancesWizardPage
from Configs import CE_VOLUME_URL
from selenium.common.exceptions import TimeoutException


class CEVolumePage(BasePage):
    def __init__(self, driver):
        self.locator = CEVolumePageLocators
        super().__init__(driver, CE_VOLUME_URL)


    def click_create_volume_btn(self):
        self.driver.find_element(*self.locator.CREATE_VOLUME_BTN).click()

    def choose_custom_disk(self, locator):
        try:
            self.find_element(*locator)
            self.click_button(CECreateVolumePageLocators.CUSTOM_DISK)
            return self
        except TimeoutException:
            self.driver.get_screenshot_as_file(
                'error_snapshot/{filename}.png'.format(filename='choose_custom_disk'))
            self.driver.quit()

    def choose_default_100G(self, locator):
        try:
            self.find_element(*locator)
            self.click_button(CEVolumePageLocators.DEFAULT_100G)
            return self
        except TimeoutException:
            self.driver.get_screenshot_as_file(
                'error_snapshot/{filename}.png'.format(filename='choose_default_100G'))
            self.driver.quit()

    def choose_Shrink_OK(self):
        self\
            .click_button(self.locator.SHRINK_OK_BTN)\
            .click_button(self.locator.OK_BTN)
        self

    def change_instance_states(self, state_button, confirm_button, message):
        self.click_button(self.locator.RADIO_BTN)\
            .click_button(self.locator.INSTANCE_STATE_BTN)\
            .click_button(state_button)\
            .wait_and_click_button(confirm_button)
        if message:
            self.check_element_existence(message)
        return self


