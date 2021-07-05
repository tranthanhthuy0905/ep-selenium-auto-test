import time

from Configs.TestData.CEVolumeTestData import CEVolumeTestData

from Locators.CE import CEVolumePageLocators
from Pages.CE.create_volume_page import CECreateVolumePage
from Pages.base_page import BasePage
from Configs import CE_VOLUME_URL
from selenium.common.exceptions import TimeoutException


class CEVolumePage(BasePage):
    def __init__(self, driver):
        self.locator = CEVolumePageLocators
        super().__init__(driver, CE_VOLUME_URL)

    def click_create_volume_btn(self):
        self.driver.find_element(*self.locator.CREATE_VOLUME_BTN).click()

    def create_new_volume(self, volume_size, disk_option):
        # *** Create a volume ***
        # When user clicks on "Create Volume" button on the top right
        self.click_create_volume_btn()
        self.create_volume_page = CECreateVolumePage(self.driver)

        # When user clicks on "Create" button
        self.volume_name = CEVolumeTestData.VOLUME_NAME
        time.sleep(2)
        self.create_volume_page.create_volume(volume_name=self.volume_name, volume_size=volume_size, disk_option=disk_option)

    def detach_volume_from_vm(self):
        self\
            .click_button(self.locator.VOLUME_ACTIONS_BTN)
        # self.ass
    def choose_disk_offering_option(self, locator, option):
        try:
            self.find_element(*locator)
            self.click_button(option)
            return self
        except TimeoutException:
            self.driver.get_screenshot_as_file(
                'error_snapshot/{filename}.png'.format(filename='choose_disk_offering_option'))
            self.driver.quit()


    def choose_Shrink_OK(self):
        self\
            .click_button(self.locator.SHRINK_OK_BTN)
        self

    def check_size_gb(self):
        size_gb = self.driver.find_element(*self.locator.SIZE_GB).text
        return size_gb



