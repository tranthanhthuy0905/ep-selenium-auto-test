from selenium.webdriver.common.keys import Keys

from Pages.base_page import BasePage
from Configs import DEVICE_FARM_BASE_URL
from Configs.TestData.DeviceFarmTestData import DEVICE_FARM_TestData
from Locators.device_farm import DEVICE_FARM_ProjectLocators


class DEVICE_FARM_DeleteProjectPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, base_url=DEVICE_FARM_BASE_URL)

    def click_delete_project_submit_button(self):
        self.driver.implicitly_wait(10)
        _project_name = self.find_element(*DEVICE_FARM_ProjectLocators.PROJECT_NAME_TEXT).text
        self.find_element(*DEVICE_FARM_ProjectLocators.PROJECT_SELECT_BUTTON)\
            .click()
        self.find_element(*DEVICE_FARM_ProjectLocators.PROJECT_ACTION_BUTTON)\
            .click()
        self.find_element(*DEVICE_FARM_ProjectLocators.PROJECT_DELETE_BUTTON)\
            .click()
        self.find_element(*DEVICE_FARM_ProjectLocators.PROJECT_CONFIRM_DELETE_BUTTON)\
            .click()
        return _project_name