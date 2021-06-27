from Pages.base_page import BasePage
from Configs import S3_BASE_URL
from Locators.s3 import S3Locators

class S3HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, base_url=S3_BASE_URL)
        self.driver.get(S3_BASE_URL)
        self.authenticate()

    def click_create_bucket(self):
        self.driver.find_element(*S3Locators.CREATE_BUCKET_HOME_BUTTON).click()
