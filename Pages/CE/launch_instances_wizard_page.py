from Locators.CE import CELaunchInstancesWizardPageLocators
from Pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from Configs.TestData.CEInstanceTestData import CEInstanceTestData
from Configs.TestData.CESecurityGroupTestData import CESecurityGroupTestData
from Configs.TestData.CEVolumeTestData import CEVolumeTestData
from Configs import CE_INSTANCE_CREATE_WIZARD_URL
from selenium.webdriver.common.by import By
import time


class CELaunchInstancesWizardPage(BasePage):
    def __init__(self, driver):
        self.locator = CELaunchInstancesWizardPageLocators
        super(CELaunchInstancesWizardPage, self).__init__(driver, CE_INSTANCE_CREATE_WIZARD_URL)

    def fill_form(self, value, locator):
        try:
            form = self.find_element(*locator)
            form.send_keys(Keys.COMMAND + "a" + Keys.DELETE)
            form.send_keys(value)
            return self
        except TimeoutException:
            self.driver.get_screenshot_as_file(
                'error_snapshot/{filename}.png'.format(filename='fill_form'))
            self.driver.quit()

    def choose_volume_type(self, locator):
        try:
            self.find_element(*locator)
            self.click_button(self.locator.CUSTOM_DISK)
            return self
        except TimeoutException:
            self.driver.get_screenshot_as_file(
                'error_snapshot/{filename}.png'.format(filename='choose_volume_type'))
            self.driver.quit()

    def choose_instance_details(self):
        self\
            .click_button(self.locator.MI_SELECT_BTN)\
            .click_button(self.locator.TYPE_2G_RADIO)\
            .click_button(self.locator.NEXT_BTN)\
            .fill_form(CEInstanceTestData.INSTANCE_NAME, self.locator.INSTANCE_NAME_FORM)
        return self

    def choose_keypair(self):
        self\
            .click_button(self.locator.KEYPAIR_LIST)\
            .choose_keypair_in_selector(self.locator.KEYPAIR_LIST)
        return self

    def fill_keypair_info(self, name, publicKey):
        self\
            .fill_form(name, self.locator.KEYPAIR_NAME)\
            .fill_form(publicKey, self.locator.PUBLIC_KEY)
        return self

    def choose_keypair_in_selector(self, locator):
        try:
            self.find_element(*locator)
            self.click_button((By.XPATH,"//div[text()='bc:89:6b:6d:32:fd:7c:24:dd:e0:7a:da:6d:3a:f3:62']"))
            return self
        except TimeoutException:
            self.driver.get_screenshot_as_file(
                'error_snapshot/{filename}.png'.format(filename='choose_volume_type'))
            self.driver.quit()

    def fill_default_password(self):
        self\
            .fill_form(CEInstanceTestData.DEFAULT_PASSWORD, self.locator.DEFAULT_PASSWORD)\
            .fill_form(CEInstanceTestData.DEFAULT_PASSWORD, self.locator.DEFAULT_PASSWORD_CONFIRM)
        return self

    def review_and_launch_instance(self):
        self\
            .click_button(self.locator.REVIEW_N_LAUNCH_BTN)\
            .click_button(self.locator.LAUNCH_BTN)
        return self

    """
        Define two options: Apply the default password and Edit own password
    """
    def apply_default_password(self):
        self\
            .click_button(self.locator.APPLY_THIS_PASSWORD) \
            .click_button(self.locator.LAUNCH_BTN)

    def edit_password(self):
        self\
            .click_button(self.locator.EDIT_PASSWORD)

    def input_password(self, value1, value2):
        self \
            .fill_form(value1, self.locator.DEFAULT_PASSWORD) \
            .fill_form(value2, self.locator.DEFAULT_PASSWORD_CONFIRM)


    def fill_volume_info(self, volume_name, volume_size):
        self\
            .fill_form(volume_name, self.locator.VOlUME_NAME_FORM) \
            .click_button(self.locator.VOLUME_TYPE_LIST) \
            .choose_volume_type(self.locator.VOLUME_TYPE_LIST) \
            .fill_form(volume_size, self.locator.VOLUME_SIZE_FORM)
        return self
