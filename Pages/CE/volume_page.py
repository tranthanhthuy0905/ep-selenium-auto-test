import time

from Configs.TestData.CEVolumeTestData import CEVolumeTestData
from selenium.webdriver.support.wait import WebDriverWait
from Pages.CE.create_volume_page import CECreateVolumePage
from Locators.CE import CEVolumePageLocators
from Pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
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
        self.create_volume_page.create_volume(volume_name=self.volume_name, volume_size=volume_size,disk_option=disk_option)

    def choose_disk_offering_option(self, locator, disk_option):
        try:
            self.find_element(*locator)
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable(disk_option), "Fail to select the disk option")
            self.click_button(disk_option)
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
        size_gb = int(self.driver.find_element(*self.locator.SIZE_GB).text)
        return size_gb

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




