from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Configs import CE_SNAPSHOT_URL
from Locators.CE import CESnapshotLocators
from Pages.CE.create_snapshot_page import CECreateSnapshotPage
from Pages.base_page import BasePage


class CESnapshotPage(BasePage):
    def __init__(self, driver):
        self.locator = CESnapshotLocators
        super().__init__(driver, CE_SNAPSHOT_URL)

    def click_create_snapshot_btn(self):
        self.driver.find_element(*self.locator.CREATE_SNAPSHOT_BTN).click()
