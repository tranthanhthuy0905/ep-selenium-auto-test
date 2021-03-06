from Locators.CE import CEPageLocators
from Pages.CE.snapshot_page import CESnapshotPage
from Pages.base_page import BasePage
from Pages.CE.instances_page import CEInstancesPage
from Pages.CE.elastic_block_store_volumes_page import CEVolumePage
from Locators.CE import CEPageLocators
from Configs import CE_BASE_URL, CE_USER_TOKEN
import time

class CEHomePage(BasePage):
    def  __init__(self, driver):
        super().__init__(driver=driver, base_url=CE_BASE_URL)
        self.driver.get(CE_BASE_URL)
        self.authenticate(CE_USER_TOKEN)

    def access_instances_page(self):
        instances_page = self.click_button_and_return_page(CEPageLocators.INSTANCES_SUBMENU_BTN, CEInstancesPage(self.driver))
        return instances_page

    def access_keypair_page(self):
        keypair_page = self\
            .click_button_and_return_page(CEPageLocators.KEYPAIR_SUBMENU_BTN, CEInstancesPage(self.driver))
        return keypair_page

    def access_volumes_page(self):
        elastic_block_store_volumes_page = self\
            .click_button_and_return_page(CEPageLocators.VOLUMES_SUBMENU_BTN, CEVolumePage(self.driver))
        return elastic_block_store_volumes_page

    def access_snapshot_page(self):
        snapshot_page = self.click_button_and_return_page(CEPageLocators.SNAPSHOTS_SUBMENU_BTN, CESnapshotPage(self.driver))
        return snapshot_page