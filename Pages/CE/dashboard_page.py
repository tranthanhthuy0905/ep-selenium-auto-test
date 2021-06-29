from Locators.CE import DashboardPageLocators
from Pages.base_page import BasePage
from Pages.CE.homepage import CEHomePage
from Configs import CE_BASE_URL


class DashboardPage(BasePage):
    def __init__(self, driver):
        self.locator = DashboardPageLocators
        super(DashboardPage, self).__init__(driver, CE_BASE_URL)

    def access_CE_page(self):
        CE_page = self.click_button_and_return_page(self.locator.CE_BTN, CEHomePage(self.driver))
        return CE_page
