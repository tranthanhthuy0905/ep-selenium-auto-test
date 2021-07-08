
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Configs import EFS_FILESYSTEM_BASE_URL
from Locators.EFS import EFSFileSystemLocators
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

    def allow_ip(self, instance_ip, file_id, read_only):
        self\
            .select_file_system(file_id)\
            .click_button(self.locator.ALLOW_IP_BTN)\
            .click_button(self.locator.ADD_FIELD_BTN)\
            .fill_form(instance_ip, self.locator.INPUT_IP)
        if read_only:
            self.click_button(self.locator.READ_ONLY_CHECKBOX)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locator.ALLOW_IP_OK),
                                             "Test fails due to not being able to click OK to complete Allow IP process")
        self.click_button(self.locator.ALLOW_IP_OK)
        return self

    # def remove_ip(self):
    #     self\
    #         .click_button(self.locator.IP_REMOVE_BTN)\
    #         .click_button(self.locator.OK_BTN)
    #     self

    def delete_filesystem(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locator.ACTIONS_BTN),
                                             "Wait more time to update the volume before deleting it")
        self \
            .click_button(self.locator.ACTIONS_BTN)\
            .click_button(self.locator.DELETE_OPTION)\
            .click_button(self.locator.DELETE_CONFIRM)
        self
