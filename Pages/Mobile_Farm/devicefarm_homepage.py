from Pages.base_page import BasePage
from Pages.Mobile_Farm.devicefarm_create_project_page import DEVICE_FARM_CreateProjectPage
from Configs import DEVICE_FARM_BASE_URL, DEVICE_FARM_USER_TOKEN
from Locators.Mobile_Farm import DEVICE_FARM_ProjectLocators

class DEVICE_FARM_HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, base_url=DEVICE_FARM_BASE_URL)
        self.driver.get(DEVICE_FARM_BASE_URL)
        self.authenticate(DEVICE_FARM_USER_TOKEN)

    def click_create_project(self):
        self.driver.find_element(*DEVICE_FARM_ProjectLocators.CREATE_PROJECT_HOME_BUTTON).click()
        