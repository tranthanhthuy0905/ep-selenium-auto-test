import os
import time

from Pages.base_page import BasePage
from Configs import S3_BUCKET_DETAILS_URL, S3_BUCKET_FILE_UPLOAD_URL
from Configs import FILE_PATH_UPLOAD_SAMPLE
from Locators.s3 import S3Locators

class S3BucketDetailsPage(BasePage):
    def __init__(self, driver, bucket_name):
        super().__init__(driver=driver, base_url=S3_BUCKET_DETAILS_URL.format(bucket_name=bucket_name))

    def access_page(self):
        self.driver.get(self.base_url)

    def click_upload_file(self):
        self.check_element_existence(S3Locators.BUCKET_UPLOAD_FILE_BUTTON)
        self.find_element(*S3Locators.BUCKET_UPLOAD_FILE_BUTTON).click()


class S3BucketFilesAndFoldersPage(BasePage):
    def __init__(self, driver, bucket_name):
        super().__init__(driver=driver, base_url=S3_BUCKET_FILE_UPLOAD_URL.format(bucket_name=bucket_name))

    def click_add_file_button(self):
        self.find_element(*S3Locators.ADD_FILES_BUTTON).click()

    def upload_file_from_browser(self):
        # TODO: CHECK FROM DIALOG POPUP???
        self.driver.implicitly_wait(10)
        file_input = self.driver.find_element(*S3Locators.FILE_INPUT)
        file_input.send_keys(FILE_PATH_UPLOAD_SAMPLE)
        # file_input.send_keys(Keys.ENTER)
        time.sleep(3)
        self.find_element(*S3Locators.UPLOAD_FILE_SUBMIT_BUTTON).click()

