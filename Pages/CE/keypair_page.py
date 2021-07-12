import logging

from Locators.CE import CEKeypairLocators
from Pages.base_page import BasePage
from Pages.CE.launch_instances_wizard_page import CELaunchInstancesWizardPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Configs import CE_KEYPAIR_URL
from Configs import CE_USER_TOKEN

class CEKeypairPage(BasePage):
    def __init__(self, driver, authenticate=True):
        super().__init__(driver, CE_KEYPAIR_URL)
        self.locator = CEKeypairLocators
        if authenticate:
            self.driver.get(self.base_url)
            self.authenticate(CE_USER_TOKEN)
            self.driver.get(self.base_url)

    def create_new_keypair(self, keypair_name, public_key):
        self.click_create_keypair()
        self.fill_keypair_info(keypair_name, public_key)
        self.click_create_keypair_submit_button()
        return keypair_name

    def select_keypair_by_name(self, keypair_name):
        self.click_button(self.locator.SELECT_KEYPAIR_RADIO(keypair_name))
        return self

    def click_action(self):
        self.click_button(CEKeypairLocators.ACTION_BTN)
        return self

    def click_delete(self):
        self.click_button(CEKeypairLocators.DELETE_BTN)
        return self

    def click_confirm_delete(self):
        self.click_button(CEKeypairLocators.CONFIRM_DELETE_BTN)
        return self
    
    def click_create_keypair_btn(self):
        self.click_button(CEKeypairLocators.CREATE_KEYPAIR_BTN)
        return self

    def click_ok_btn(self):
        self.click_button(CEKeypairLocators.OK_BTN)
        return self

    def click_close_btn(self):
        self.click_button(CEKeypairLocators.CLOSE_BTN)
        return self

    def fill_keypair_info(self, keypair_name, public_key):
        self \
            .fill_form(keypair_name, self.locator.KEYPAIR_NAME_TEXTBOX) \
            .fill_form(public_key, self.locator.PUBLIC_KEY_TEXTBOX)
        return self
    
    def check_if_keypair_created_successfully(self):
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(CEKeypairLocators.SUCCESSFULLY_MESSAGE, "Created keypair successfully."))
        self.click_button(CEKeypairLocators.CLOSE_BTN)
    
    # get fingerprint of keypair in list keypair
    def get_fingerprint(self, keypair_name):
        return self.find_element(*CEKeypairLocators.FINGERPRINT_BY_KEYPAIR_NAME(keypair_name)).text

    def create_keypair_simple_flow(self, keypair_name, public_key):
        self.click_button(CEKeypairLocators.CREATE_KEYPAIR_BTN)
        self.fill_keypair_info(keypair_name, "")
        self.click_button(CEKeypairLocators.OK_BTN)
        self.check_if_keypair_created_successfully()

        # return fingerpring for selecting step in instance wizard
        return self.get_fingerprint(keypair_name)
        logging.info(f"Filled in keypair information. Name: {keypair_name}, public_key: {public_key[:-10]+ '...' if public_key else '<empty>'}")

    def click_create_keypair(self):
        self.click_button(CEKeypairLocators.CREATE_KEYPAIR_BTN)
        logging.info("Clicked create keypair button")
    
    def click_create_keypair_submit_button(self):
        self.click_button(CEKeypairLocators.OK_BTN)
        logging.info("Clicked submit create keypair button")

    def check_keypair_existence_in_table(self, kp_name):
        return self.check_element_existence(
            CEKeypairLocators.KEYPAIR_ROW(kp_name)
        )

    def check_alert_invalid_key_existence(self):
        return self.check_element_existence(
            CEKeypairLocators.INVALID_KEY_ALERT_DIALOG
        )

    def check_download_keypair_dialog_existence(self):
        return self.check_element_existence(
            CEKeypairLocators.DOWNLOAD_KEYPAIR_DIALOG
        )

    def check_alert_public_key_existence(self):
        return self.check_element_existence(
            CEKeypairLocators.DUPLICATED_PUBLIC_KEY_DIALOG
        )
