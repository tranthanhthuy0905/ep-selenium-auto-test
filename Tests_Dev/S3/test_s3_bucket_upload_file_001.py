import os
import unittest

import HtmlTestRunner

from Tests_Dev.S3.s3_base_test import S3BaseTest
from Pages.S3.s3_bucket_details_page import S3BucketDetailsPage, S3BucketFilesAndFoldersPage
from Pages.S3.s3_homepage import S3HomePage

class Test_S3_Upload_File(S3BaseTest):

    def test_upload_file_to_bucket_successful(self):
        '''
        File should be successfully uploaded to a S3 bucket
        '''

        self.s3_homepage = S3HomePage(self.driver, authenticate=True)
        self.bucket_name = self.create_s3_bucket()
        self.s3_bucket_details_page = S3BucketDetailsPage(self.driver, self.bucket_name)
        self.s3_bucket_details_page.access_page()
        self.s3_bucket_details_page.click_upload_file()

        self.s3_files_and_folders_page = S3BucketFilesAndFoldersPage(self.driver, self.bucket_name)
        self.assertEqual(self.driver.current_url, self.s3_files_and_folders_page.base_url)

        # self.s3_files_and_folders_page.click_add_file_button()
        self.s3_files_and_folders_page.upload_file_from_browser()

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
