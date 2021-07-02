from selenium.webdriver.common.keys import Keys

from Pages.base_page import BasePage
from Configs import DF_BASE_URL
from Configs.TestData.DFTestData import DFTestData
from Locators.df import DFProjectLocators

class DFCreateProjectPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, base_url=DF_BASE_URL)

    def fill_project_create_information(self):
        _project_name = DFTestData.PROJECT_NAME
        self.find_element(*DFProjectLocators.PROJECT_NAME_TEXTBOX) \
            .clear()
        self.find_element(*DFProjectLocators.PROJECT_NAME_TEXTBOX)\
            .send_keys(_project_name)
        return _project_name

    def click_create_project_submit_button(self):
        self.driver.implicitly_wait(10)
        self.find_element(*DFProjectLocators.PROJECT_CREATE_BUTTON)\
            .click()