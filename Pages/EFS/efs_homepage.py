from Configs import EFS_USER_TOKEN, EFS_BASE_URL
from Locators.EFS import EFSHomePageLocators
from Pages.base_page import BasePage


class EFSHomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver, base_url=EFS_BASE_URL)
        self.driver.get(EFS_BASE_URL)
        self.authenticate(EFS_USER_TOKEN)

    def click_file_systems_button(self):
        self.click_button(EFSHomePageLocators.FILES_SYSTEMS)
        return self
    # def access_efs_filesystem_page(self):
    #     efs_filesystem_page = self.click_button_and_return_page(EFSHomePageLocators.FILES_SYSTEMS, EFSFileSystemPage(self.driver))
    #     return efs_filesystem_page
