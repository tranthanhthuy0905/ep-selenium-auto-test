from Locators.CE import CEInstanceTypesPageLocators
from Pages.base_page import BasePage


class CEInstanceTypesPage(BasePage):
    def __init__(self, driver):
        self.locator = CEInstanceTypesPageLocators
        super(CEInstanceTypesPage, self).__init__(driver)

