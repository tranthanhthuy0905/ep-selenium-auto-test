from Locators.CE import DashboardPageLocators
from Pages.base_page import BasePage
from Pages.CE.ec2_page import EC2Page
from Configs import EC2_BASE_URL


class DashboardPage(BasePage):
    def __init__(self, driver):
        self.locator = DashboardPageLocators
        super(DashboardPage, self).__init__(driver, EC2_BASE_URL)

    def access_ec2_page(self):
        ec2_page = self.click_button_and_return_page(self.locator.EC2_BTN, EC2Page(self.driver))
        return ec2_page
