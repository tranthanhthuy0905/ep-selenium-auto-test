from utils.locators import *
from pages.base_page import BasePage
from pages.ec2_page import EC2Page


class DashboardPage(BasePage):
    def __init__(self, driver):
        self.locator = DashboardPageLocators
        super(DashboardPage, self).__init__(driver)

    def access_ec2_page(self):
        ec2_page = self.click_button_and_return_page(self.locator.EC2_BTN, EC2Page(self.driver))
        return ec2_page
