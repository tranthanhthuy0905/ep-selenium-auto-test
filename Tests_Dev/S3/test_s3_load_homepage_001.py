import os
import time
import unittest

import HtmlTestRunner

from Tests_Dev.S3.s3_base_test import S3BaseTest
from Pages.S3.s3_homepage import S3HomePage
from Configs.TestData.S3TestData import S3TestData


class Test_S3_Home_Page(S3BaseTest):

    def test_load_homepage(self):
        """
            S3 Homepage must be loaded successfully
        """
        self.s3_homepage = S3HomePage(self.driver)

        # Page title must be correct
        self.assertIn(S3TestData.CE_PAGE_TITLE, self.driver.title)
        self.driver.implicitly_wait(10)

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
