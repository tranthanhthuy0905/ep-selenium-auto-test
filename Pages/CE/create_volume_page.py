from selenium.webdriver.support import expected_conditions as EC
from Locators.CE import CECreateVolumePageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from Configs import CE_CREATE_VOLUME_URL
from Locators.CE import CECreateVolumePageLocators, CEVolumePageLocators, CELaunchInstancesWizardPageLocators
from Pages.base_page import BasePage


class CECreateVolumePage(BasePage):
    def __init__(self, driver):
        self.locator = CECreateVolumePageLocators
        super().__init__(driver=driver, base_url=CE_CREATE_VOLUME_URL)

    def show(self):
        print(self.base_url)

    def choose_volume_type(self, locator, disk_option):
        try:
            self.find_element(*locator)
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable(disk_option), "Fail to select the volume type")
            self.click_button(disk_option)
            return self
        except TimeoutException:
            self.driver.get_screenshot_as_file(
                'error_snapshot/{filename}.png'.format(filename='choose_volume_type'))
            self.driver.quit()

    def create_volume(self, volume_name, volume_size, disk_option):
        self\
            .fill_form(volume_name, self.locator.VOLUME_NAME_FORM) \
            .click_button(self.locator.VOLUME_TYPE_LIST)\
            .choose_volume_type(self.locator.VOLUME_TYPE_LIST, disk_option)

        if disk_option == self.locator.CUSTOM_DISK:
            self.fill_form(volume_size, CECreateVolumePageLocators.VOLUME_SIZE_FORM)

        self.click_button(self.locator.CREATE_VOLUME_BTN)
        return self


