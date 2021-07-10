import os
import unittest
import logging

import HtmlTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tests_Dev.S3.s3_base_test import S3BaseTest

from Pages.S3.s3_homepage import S3HomePage
from Pages.S3.s3_create_bucket_page import S3CreateBucketPage
from Pages.S3.s3_bucket_details_page import S3BucketDetailsPage

from Locators.S3 import S3Locators


class Test_S3_Create_Bucket(S3BaseTest):

    def test_create_bucket_successful(self):
        """
            S3 Bucket should be created successfully
        """
        self.s3_homepage = S3HomePage(self.driver, authenticate=True)
        self.s3_homepage.click_create_bucket()

        self.s3_create_bucket_page = S3CreateBucketPage(self.driver)
        self.assertEqual(self.driver.current_url, self.s3_create_bucket_page.base_url)
        self.assertTrue(
            self.s3_create_bucket_page.check_element_existence(S3Locators.BUCKET_CREATE_TITLE)
        )

        bucket_name = self.s3_create_bucket_page.fill_bucket_create_information()
        self.service_slug = bucket_name

        self.s3_create_bucket_page.click_create_bucket_submit_button()

        self.driver.implicitly_wait(10)
        self.bucket_details_page = S3BucketDetailsPage(self.driver, bucket_name)
        self.driver.implicitly_wait(10)

        WebDriverWait(self.driver, 10).until(EC.url_to_be(self.bucket_details_page.base_url))
        self.assertEqual(
            self.driver.current_url, self.bucket_details_page.base_url
        )


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
