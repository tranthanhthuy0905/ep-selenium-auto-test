from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tests.base_test import BaseTest
from Configs import S3_BUCKET_API_CLIENT_URL
from Configs import S3_BUCKET_DETAILS_URL
from Configs import S3_USER_TOKEN
from Pages.s3.s3_homepage import S3HomePage
from Pages.s3.s3_create_bucket_page import S3CreateBucketPage
from Pages.s3.s3_bucket_details_page import S3BucketDetailsPage



class S3BaseTest(BaseTest):
    def _call_api_delete_s3_bucket(self):
        try:
            url = S3_BUCKET_API_CLIENT_URL
            params = {
                "bucket_name": self.service_slug
            }
            self._call_request_delete(url, params, S3_USER_TOKEN)
        except Exception as e:
            print("Can't delete S3 bucket;", str(e))

    def create_s3_bucket(self):
        self.s3_homepage = S3HomePage(self.driver)
        self.s3_homepage.click_create_bucket()
        self.s3_create_bucket_page = S3CreateBucketPage(self.driver)
        bucket_name = self.s3_create_bucket_page.fill_bucket_create_information()
        self.service_slug = bucket_name
        self.s3_create_bucket_page.click_create_bucket_submit_button()
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, 10).until(EC.url_to_be(S3_BUCKET_DETAILS_URL.format(bucket_name=bucket_name)))
        return bucket_name

