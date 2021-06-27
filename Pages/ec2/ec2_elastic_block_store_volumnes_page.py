from Locators.ec2 import EC2ElasticBlockStoreVolumnePageLocators
from Pages.base_page import BasePage
from Configs import EC2_BASE_URL


class EC2ElasticBlockStoreVolumnePage(BasePage):
    def __init__(self, driver):
        self.locator = EC2ElasticBlockStoreVolumnePageLocators
        super(EC2ElasticBlockStoreVolumnePage, self).__init__(driver, EC2_BASE_URL)