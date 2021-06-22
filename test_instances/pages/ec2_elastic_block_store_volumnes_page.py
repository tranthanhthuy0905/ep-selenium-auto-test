from utils.locators import *
from pages.base_page import BasePage


class EC2ElasticBlockStoreVolumnePage(BasePage):
    def __init__(self, driver):
        self.locator = EC2ElasticBlockStoreVolumnePageLocators
        super(EC2ElasticBlockStoreVolumnePage, self).__init__(driver)

