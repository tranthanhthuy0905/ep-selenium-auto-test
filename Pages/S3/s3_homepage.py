from Pages.base_page import BasePage
from Pages.S3.s3_create_bucket_page import S3CreateBucketPage
from Configs import S3_BASE_URL, S3_USER_TOKEN
from Locators.S3 import S3Locators

class S3HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, base_url=S3_BASE_URL)
        self.driver.get(S3_BASE_URL)
        self.authenticate(S3_USER_TOKEN)

    def click_create_bucket(self):
        self.driver.find_element(*S3Locators.CREATE_BUCKET_HOME_BUTTON).click()

    def select_s3_bucket(self, bucket_name):
        pass
        # buttonnnnn = S3Locators.BUCKET_RADIO_BUTTON(bucket_name)
        # print(buttonnnnn)
        # self.driver.find_element(*buttonnnnn)