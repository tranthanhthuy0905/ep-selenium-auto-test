from selenium.webdriver.common.keys import Keys

from Pages.base_page import BasePage
from Configs import DEVICE_FARM_BASE_URL
from Configs.TestData.DeviceFarmTestData import DEVICE_FARM_TestData
from Locators.device_farm import DEVICE_FARM_ProjectLocators
import time

class DEVICE_FARM_DeleteSessionPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, base_url=DEVICE_FARM_BASE_URL)

    def click_delete_session_submit_button(self):
        self.driver.implicitly_wait(10)
        self.find_element(*DEVICE_FARM_ProjectLocators.PROJECT_SELECTOR_LINK)\
            .click()
        time.sleep(2)
        self.find_element(*DEVICE_FARM_ProjectLocators.SESSION_SELECT_BUTTON)\
            .click()
        time.sleep(2)
        self.find_element(*DEVICE_FARM_ProjectLocators.SESSION_ACTION_BUTTON)\
            .click()
        time.sleep(2)
        self.find_element(*DEVICE_FARM_ProjectLocators.SESSION_DELETE_ACTION_BUTTON)\
            .click()
        time.sleep(2)
        self.find_element(*DEVICE_FARM_ProjectLocators.SESSION_DELETE_CONFIRM_BUTTON)\
            .click()
        