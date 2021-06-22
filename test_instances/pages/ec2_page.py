from utils.locators import *
from pages.base_page import BasePage
from pages.ec2_instances_page import EC2InstancesPage
from pages.ec2_instances_type_page import EC2InstanceTypesPage
from pages.ec2_elastic_block_store_volumnes_page import EC2ElasticBlockStoreVolumnePage


class EC2Page(BasePage):
    def __init__(self, driver):
        self.locator = EC2PageLocators
        super(EC2Page, self).__init__(driver)

    def access_ec2_instances_page(self):
        ec2_instances_page = self\
            .click_button(self.locator.INSTANCES_MENU_BTN)\
            .click_button_and_return_page(self.locator.INSTANCES_SUBMENU_BTN, EC2InstancesPage(self.driver))
        return ec2_instances_page

    def access_ec2_instance_types_page(self):
        instance_types_page = self\
            .click_button(self.locator.INSTANCES_MENU_BTN)\
            .click_button_and_return_page(self.locator.INSTANCE_TYPES_SUBMENU_BTN, EC2InstanceTypesPage(self.driver))
        return instance_types_page

    def access_ec2_elastic_block_store_volumnes_page(self):
        elastic_block_store_volumnes_page = self\
            .click_button(self.locator.ELASTIC_BLOCK_STORE_MENU_BTN)\
            .click_button_and_return_page(self.locator.VOLUMES_SUBMENU_BTN, EC2ElasticBlockStoreVolumnePage(self.driver))
        return elastic_block_store_volumnes_page
