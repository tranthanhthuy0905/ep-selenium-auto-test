from Locators.CE import CEPageLocators
from Pages.base_page import BasePage
from Pages.CE.instances_page import CEInstancesPage
from Pages.CE.elastic_block_store_volumnes_page import CEVolumePage
from Locators.CE import CEPageLocators
from Configs import CE_BASE_URL, CE_USER_TOKEN


class CEHomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, base_url=CE_BASE_URL)
        self.driver.get(CE_BASE_URL)
        self.authenticate(CE_USER_TOKEN)

    def access_instances_page(self):
        instances_page = self\
            .click_button_and_return_page(CEPageLocators.INSTANCES_SUBMENU_BTN, CEInstancesPage(self.driver))
        return instances_page

    def access_volumes_page(self):
        elastic_block_store_volumes_page = self\
            .click_button_and_return_page(CEPageLocators.VOLUMES_SUBMENU_BTN, CEVolumePage(self.driver))
        return elastic_block_store_volumes_page
