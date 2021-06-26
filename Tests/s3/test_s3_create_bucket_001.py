import os
import unittest
import time

import HtmlTestRunner

from Tests.base_test import BaseTest
from Pages.s3.s3_homepage import S3HomePage, S3CreateBucketPage, S3BucketDetailsPage
from Locators.s3 import S3Locators


class Test_S3_Create_Bucket(BaseTest):

    def test_create_bucket_successful(self):
        """
            S3 Bucket should be created successfully
        """
        self.s3_homepage = S3HomePage(self.driver)
        self.s3_homepage.click_create_bucket()

        self.s3_create_bucket_page = S3CreateBucketPage(self.driver)
        self.assertEqual(self.driver.current_url, self.s3_create_bucket_page.base_url)
        self.assertTrue(
            self.s3_create_bucket_page.check_element_existence(S3Locators.BUCKET_CREATE_TITLE)
        )

        bucket_name = self.s3_create_bucket_page.fill_bucket_create_information()
        self.s3_create_bucket_page.click_create_bucket_submit_button()

        self.driver.implicitly_wait(10)
        self.bucket_details_page = S3BucketDetailsPage(self.driver, bucket_name)
        self.driver.implicitly_wait(10)
        self.assertEqual(
            self.driver.current_url, self.bucket_details_page.base_url
        )
        time.sleep(10)




if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
