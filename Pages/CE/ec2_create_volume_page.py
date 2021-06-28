from Locators.CE import EC2CreateVolumnePageLocators
from Pages.base_page import BasePage
from Pages.CE.ec2_launch_instances_wizard_page import EC2LaunchInstancesWizardPage
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from Configs import EC2_CREATE_VOLUME_URL
import time

class EC2CreateVolumePage(BasePage):
    def __init__(self, driver):
        self.locator = EC2CreateVolumnePageLocators
        super(EC2CreateVolumePage, self).__init__(driver, EC2_CREATE_VOLUME_URL)

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
            .fill_form(volume_name, self.locator.VOLUME_NAME_FORM) \
            .click_button(self.locator.VOLUME_TYPE_LIST) \
            .choose_volume_type(self.locator.VOLUME_TYPE_LIST) \
            .fill_form(volume_size, self.locator.VOLUME_SIZE_FORM) \
            .click_button(self.locator.CREATE_VOlUMNE_BTN)
        return self


