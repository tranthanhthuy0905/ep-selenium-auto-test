from Configs import RDS_CREATE_URL
from Configs.TestData.RDSTestData import RDSTestData
from Locators.RDS import RDSCreatePageLocators
from Pages.base_page import BasePage


class RDSCreatePage(BasePage):
    def __init__(self, driver):
        self.locator = RDSCreatePageLocators
        super().__init__(driver, RDS_CREATE_URL)

    def create_database(self, master_password, confirm_password, config_option, no_of_replica):
        self.cluster_name = RDSTestData.CLUSTER_NAME
        if config_option == "Custom":
            self\
                .click_button(self.locator.CUSTOM_CONFIGS)\
                .click_button(self.locator.DB_INSTANCE_CLASS)\
                .click_button(self.locator.FIRST_CPU_OPTION)\
                .fill_form(no_of_replica, self.locator.NO_OF_REPLICA)
        self\
            .fill_form(self.cluster_name)\
            .fill_form(master_password, self.locator.MASTER_PASSWORD)\
            .fill_form(confirm_password, self.locator.CONFIRM_PASSWORD)
        return self
