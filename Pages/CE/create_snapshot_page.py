import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Configs import CE_CREATE_SNAPSHOT_URL
from Configs.TestData.CESnapshotTestData import CESnapshotTestData
from Locators.CE import CESnapshotLocators
from Pages.base_page import BasePage


class CECreateSnapshotPage(BasePage):
    def __init__(self, driver):
        self.locator = CESnapshotLocators
        super().__init__(driver, CE_CREATE_SNAPSHOT_URL)

    def input_snapshot_name(self):
        self.snapshot_name = CESnapshotTestData.SNAPSHOT_NAME
        self.fill_form(self.snapshot_name, self.locator.SNAPSHOT_NAME_FORM)
        return self

    def input_volume_choice(self, volume_name):
        self.find_element(*self.locator.SELECT_VOLUME) \
            .send_keys(volume_name)
        self.find_element(*self.locator.SELECT_VOLUME) \
            .send_keys(Keys.ENTER)
        # Click on Create Snapshot button to confirm the creation
        self.click_button(self.locator.CREATE_SNAPSHOT_CONFIRM)
        return self
