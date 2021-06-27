from Locators.ec2 import EC2LaunchInstancesWizardPageLocators
from Pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from Configs import EC2_BASE_URL
import time


class EC2LaunchInstancesWizardPage(BasePage):
    def __init__(self, driver):
        self.locator = EC2LaunchInstancesWizardPageLocators
        super(EC2LaunchInstancesWizardPage, self).__init__(driver, EC2_BASE_URL)

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
            time.sleep(5)
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
            .fill_form('hahv3-autotest-VM-01', self.locator.INSTANCE_NAME_FORM)\
            .click_button(self.locator.NEXT_BTN)
         return self

    def review_and_launch_intance(self):
        self\
            .click_button(self.locator.REVIEW_N_LAUNCH_BTN)\
            .click_button(self.locator.LAUNCH_BTN)
        return self

    def create_volume(self, volume_name, volume_size):
        self\
            .click_button(self.locator.ADD_NEW_VOLUME_BTN)\
            .fill_form(volume_name, self.locator.VOlUME_NAME_FORM) \
            .click_button(self.locator.VOLUME_TYPE_LIST) \
            .choose_volume_type(self.locator.VOLUME_TYPE_LIST) \
            .fill_form(volume_size, self.locator.VOLUME_SIZE_FORM) \
            .click_button(self.locator.CREATE_VOlUMNE_BTN) \
            .check_element_existence(self.locator.CREATE_VOLUMNE_SUCCESS_MESSAGE)
        time.sleep(5)
        self.click_button(self.locator.NEXT_BTN)
        return self
