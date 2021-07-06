from Locators.CE import CEKeypairLocators
from Pages.base_page import BasePage
from Pages.CE.launch_instances_wizard_page import CELaunchInstancesWizardPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Configs import CE_KEYPAIR_URL

class CEKeypairPage(BasePage):
    def __init__(self, driver):
        self.locator = CEKeypairLocators
        super().__init__(driver, CE_KEYPAIR_URL)

    def fill_keypair_info(self, keypair_name, public_key):
        self \
            .fill_form(keypair_name, self.locator.KEYPAIR_NAME_TEXTBOX) \
            .fill_form(public_key, self.locator.PUBLIC_KEY_TEXTBOX)
        