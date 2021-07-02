from selenium.webdriver.common.keys import Keys

from Pages.base_page import BasePage
from Configs import DF_BASE_URL
from Configs.TestData.DFTestData import DFTestData
from Locators.df import DFProjectLocators

import time

class DFDeleteProjectPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, base_url=DF_BASE_URL)

    def click_delete_project_submit_button(self):
        self.driver.implicitly_wait(10)
        _project_name = self.find_element(*DFProjectLocators.PROJECT_NAME_TEXT).text
        self.find_element(*DFProjectLocators.PROJECT_SELECT_BUTTON)\
            .click()
        self.find_element(*DFProjectLocators.PROJECT_ACTION_BUTTON)\
            .click()
        self.find_element(*DFProjectLocators.PROJECT_DELETE_BUTTON)\
            .click()
        self.find_element(*DFProjectLocators.PROJECT_CONFIRM_DELETE_BUTTON)\
            .click()
        return _project_name