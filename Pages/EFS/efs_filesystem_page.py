from selenium.webdriver.common.by import By

from Configs import EFS_FILESYSTEM_BASE_URL, EFS_USER_TOKEN
from Locators.EFS import EFSFileSystemLocators
from Pages.EFS.efs_homepage import EFSHomePage
from Pages.base_page import BasePage


class EFSFileSystemPage(BasePage):
    def __init__(self, driver):
        self.locator = EFSFileSystemLocators
        super().__init__(driver, EFS_FILESYSTEM_BASE_URL)

    def select_file_system(self, file_id):
        self.click_button((By.XPATH, '//span[././input/@type="radio" and ancestor::tr/@data-row-key="' + file_id + '"]'))
        return self

    def create_file_system(self, file_name):
        self\
            .click_button(self.locator.CREATE_FILE_SYSTEM_BTN)\
            .fill_form(file_name, self.locator.INPUT_FILESYSTEM_NAME)\
            .click_button(self.locator.OK_BTN)
        return self

    def allow_ip(self, instance_ip, file_system_id, read_only):
        self\
            .select_file_system(file_system_id)\
            .click_button(self.locator.ALLOW_IP_BTN)\
            .fill_form(instance_ip, self.locator.IP_INPUT_FORM)
        if read_only:
            self.click_button(self.locator.READ_ONLY_CHECKBOX)
        self.click_button(self.locator.OK_BTN)
        return self

    def remove_ip(self):
        self\
            .click_button(self.locator.IP_REMOVE_BTN)\
            .click_button(self.locator.OK_BTN)
        self

    def delete_filesystem(self, file_id):
        self \
            .select_file_system(file_id) \
            .click_button(self.locator.ACTIONS_BTN)\
            .click_button(self.locator.DELETE_OPTION)\
            .click_button(self.locator.DELETE_CONFIRM)
        self
