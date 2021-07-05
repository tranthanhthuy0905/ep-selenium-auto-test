from selenium.webdriver.common.keys import Keys

from Pages.base_page import BasePage
from Configs import DEVICE_FARM_BASE_URL
from Configs.TestData.DeviceFarmTestData import DEVICE_FARM_TestData
from Locators.Mobile_Farm import DEVICE_FARM_ProjectLocators

class DEVICE_FARM_CreateProjectPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, base_url=DEVICE_FARM_BASE_URL)

    def fill_project_create_information(self):
        _project_name = DEVICE_FARM_TestData.PROJECT_NAME
        self.find_element(*DEVICE_FARM_ProjectLocators.PROJECT_NAME_TEXTBOX) \
            .clear()
        self.find_element(*DEVICE_FARM_ProjectLocators.PROJECT_NAME_TEXTBOX)\
            .send_keys(_project_name)
        return _project_name

    def click_create_project_submit_button(self):
        self.driver.implicitly_wait(10)
        self.find_element(*DEVICE_FARM_ProjectLocators.PROJECT_CREATE_BUTTON)\
            .click()