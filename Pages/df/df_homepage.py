from Pages.base_page import BasePage
from Pages.df.df_create_project_page import DFCreateProjectPage
from Configs import DF_BASE_URL
from Locators.df import DFProjectLocators

class DFHomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, base_url=DF_BASE_URL)
        self.driver.get(DF_BASE_URL)
        self.authenticate()

    def click_create_project(self):
        self.driver.find_element(*DFProjectLocators.CREATE_PROJECT_HOME_BUTTON).click()
        