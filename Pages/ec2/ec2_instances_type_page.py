from Locators.ec2 import EC2InstanceTypesPageLocators
from Pages.base_page import BasePage


class EC2InstanceTypesPage(BasePage):
    def __init__(self, driver):
        self.locator = EC2InstanceTypesPageLocators
        super(EC2InstanceTypesPage, self).__init__(driver)

