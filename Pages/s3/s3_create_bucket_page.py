from selenium.webdriver.common.keys import Keys

from Pages.base_page import BasePage
from Configs import S3_BUCKET_CREATE_URL
from Configs.TestData.S3TestData import S3TestData
from Locators.s3 import S3Locators

class S3CreateBucketPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, base_url=S3_BUCKET_CREATE_URL)

    def fill_bucket_create_information(self):
        _bucket_name = S3TestData.BUCKET_NAME
        self.find_element(*S3Locators.BUCKET_NAME_TEXTBOX)\
            .send_keys(_bucket_name)
        self.find_element(*S3Locators.BUCKET_REGION_DROPDOWN)\
            .send_keys(S3TestData.BUCKET_REGION)
        self.find_element(*S3Locators.BUCKET_REGION_DROPDOWN)\
            .send_keys(Keys.ENTER)
        return _bucket_name

    def click_create_bucket_submit_button(self):
        self.driver.implicitly_wait(10)
        self.find_element(*S3Locators.BUCKET_CREATE_SUBMIT_BUTTON)\
            .click()