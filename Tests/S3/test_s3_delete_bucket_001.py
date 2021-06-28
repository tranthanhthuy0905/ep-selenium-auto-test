import os
import unittest

import HtmlTestRunner

from Tests.S3.s3_base_test import S3BaseTest
from Pages.S3.s3_homepage import S3HomePage

class Test_S3_Delete_Bucket(S3BaseTest):

    def test_upload_file_to_bucket_successful(self):
        '''
            Created empty bucket should be deleted successfully
        '''
        bucket_name = self.create_s3_bucket()
        self.s3_homepage = S3HomePage(self.driver)
        self.s3_homepage.select_s3_bucket(bucket_name)

    def test_upload_non_empty_bucket_non_successful(self):
        '''
            Non-empty bucket must not be deleted
        '''
        pass



if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
