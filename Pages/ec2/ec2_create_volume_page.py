from Locators.ec2 import EC2CreateVolumnePageLocators
from Pages.base_page import BasePage
from Pages.ec2.ec2_launch_instances_wizard_page import EC2LaunchInstancesWizardPage
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from Configs import EC2_CREATE_VOLUME_URL
import time

class EC2CreateVolumePage(BasePage):
    def __init__(self, driver):
        self.locator = EC2CreateVolumnePageLocators
        super(EC2CreateVolumePage, self).__init__(driver, EC2_CREATE_VOLUME_URL)

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
        
    def create_volume(self, volume_name, volume_size):
        self\
            .click_button(self.locator.VOLUME_TYPE_LIST) \
            .choose_volume_type(self.locator.VOLUME_TYPE_LIST) \
            .fill_form(volume_size, self.locator.VOLUME_SIZE_FORM) \
            .click_button(self.locator.CREATE_VOlUMNE_BTN) \
            .check_element_existence(self.locator.CREATE_VOLUMNE_SUCCESS_MESSAGE)
        return self


