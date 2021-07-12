import logging

from Pages.base_page import BasePage
from Configs import S3_BASE_URL, S3_USER_TOKEN
from Locators.S3 import S3Locators

class S3HomePage(BasePage):
    def __init__(self, driver, authenticate=False):
        super().__init__(driver=driver, base_url=S3_BASE_URL)
        self.driver.get(S3_BASE_URL)
        if authenticate:
            logging.info(f"Authenticating url: {S3_BASE_URL}, Token: {S3_USER_TOKEN[:10]}....{S3_USER_TOKEN[-10:]}")
            self.authenticate(S3_USER_TOKEN)
            self.driver.get(S3_BASE_URL)

    def click_create_bucket(self):
        self.wait_and_click_button(S3Locators.CREATE_BUCKET_HOME_BUTTON, 2)
        logging.info("'Create bucket' button is clicked.")

    def select_s3_bucket(self, bucket_name):
        self.click_button(
            S3Locators.BUCKET_RADIO_BUTTON(bucket_name)
        )
        logging.info(f"Radio button of bucket {bucket_name} is selected.")

    def click_action_button(self):
        self.click_button(
            S3Locators.ACTION_BUTTON
        )
        logging.info(f"Action button is clicked.")
    
    def click_delete_option(self):
        self.click_button(
            S3Locators.DELETE_BUCKET_OPTION
        )
        logging.info("Delete option in dropdown menu is selected.")

    def click_delete_confirm_button(self):
        self.wait_and_click_button(
            S3Locators.DELETE_CONFIRM_BUTTON, 3
        )
        logging.info("Delete button in confirmation dialog is clicked.")