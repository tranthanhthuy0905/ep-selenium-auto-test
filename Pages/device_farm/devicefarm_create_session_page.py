from selenium.webdriver.common.keys import Keys

from Pages.base_page import BasePage
from Configs import DEVICE_FARM_BASE_URL
from Configs.TestData.DeviceFarmTestData import DEVICE_FARM_TestData
from Locators.device_farm import DEVICE_FARM_ProjectLocators
import time

class DEVICE_FARM_CreateSessionPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, base_url=DEVICE_FARM_BASE_URL)

    def click_create_session_submit_button(self):
        self.driver.implicitly_wait(10)
        self.find_element(*DEVICE_FARM_ProjectLocators.PROJECT_SELECTOR_LINK)\
            .click()
        time.sleep(2) #must have sleep because waiting
        self.driver.implicitly_wait(10)
        self.find_element(*DEVICE_FARM_ProjectLocators.SESSION_CREATE_BUTTON)\
            .click()

    def click_create_session_lg(self):
        self.driver.implicitly_wait(10)
        _session_name = self.find_element(*DEVICE_FARM_ProjectLocators.SESSION_NAME_TEXT).text
        self.find_element(*DEVICE_FARM_ProjectLocators.LG_G5_SE_BUTTON)\
            .click()
        self.find_element(*DEVICE_FARM_ProjectLocators.CONFIRM_START_SESSION_BUTTON)\
            .click()
        self.driver.implicitly_wait(10)
        return _session_name

    def click_create_session_live(self):
        self.driver.implicitly_wait(10)
        _session_name = self.find_element(*DEVICE_FARM_ProjectLocators.SESSION_NAME_TEXT).text
        self.find_element(*DEVICE_FARM_ProjectLocators.LIVE_BUTTON)\
            .click()
        self.find_element(*DEVICE_FARM_ProjectLocators.CONFIRM_START_SESSION_BUTTON)\
            .click()
        self.driver.implicitly_wait(10)
        return _session_name

    def click_create_session_pixel(self):
        self.driver.implicitly_wait(10)
        _session_name = self.find_element(*DEVICE_FARM_ProjectLocators.SESSION_NAME_TEXT).text
        self.find_element(*DEVICE_FARM_ProjectLocators.PIXEL_BUTTON)\
            .click()
        self.find_element(*DEVICE_FARM_ProjectLocators.CONFIRM_START_SESSION_BUTTON)\
            .click()
        self.driver.implicitly_wait(10)
        return _session_name

    def click_create_session_galaxy(self):
        self.driver.implicitly_wait(10)
        _session_name = self.find_element(*DEVICE_FARM_ProjectLocators.SESSION_NAME_TEXT).text
        self.find_element(*DEVICE_FARM_ProjectLocators.GALAXY_TAB_E)\
            .click()
        self.find_element(*DEVICE_FARM_ProjectLocators.CONFIRM_START_SESSION_BUTTON)\
            .click()
        self.driver.implicitly_wait(10)
        return _session_name

    def click_create_session_xperia(self):
        self.driver.implicitly_wait(10)
        _session_name = self.find_element(*DEVICE_FARM_ProjectLocators.SESSION_NAME_TEXT).text
        self.find_element(*DEVICE_FARM_ProjectLocators.XPERIA_AQUA)\
            .click()
        self.find_element(*DEVICE_FARM_ProjectLocators.CONFIRM_START_SESSION_BUTTON)\
            .click()
        self.driver.implicitly_wait(10)
        return _session_name

    def click_create_session_pixel3(self):
        self.driver.implicitly_wait(10)
        _session_name = self.find_element(*DEVICE_FARM_ProjectLocators.SESSION_NAME_TEXT).text
        self.find_element(*DEVICE_FARM_ProjectLocators.PIXEL_3)\
            .click()
        self.find_element(*DEVICE_FARM_ProjectLocators.CONFIRM_START_SESSION_BUTTON)\
            .click()
        self.driver.implicitly_wait(10)
        return _session_name