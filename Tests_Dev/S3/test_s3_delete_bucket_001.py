
'''
Scenario 5: Delete an empty bucket
	Given there is at least 1 bucket created
	When user select radio button next to any row of bucket info that has files in
	Then user should see the radio button is ticked
	And the details of bucket are displayed at the section below
	When user click Action button
	Then user see menu of options dropped down, including Delete
	When user select Delete
	Then there is a confirmation window pop up
	And user sees 2 buttons Delete and Cancel
	When user clicks Delete
	Then user receives a successful notification popup
	And the bucket is sucessufully deleted
'''
import os
import unittest

import HtmlTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Locators.S3 import S3Locators
from Tests_Dev.S3.s3_base_test import S3BaseTest
from Pages.S3.s3_homepage import S3HomePage

class Test_S3_Delete_Bucket(S3BaseTest):

    def test_delete_non_empty_bucket_successful(self):
        '''
            Created empty bucket should be deleted successfully
        '''

        # Given there is at least 1 bucket created
        self.s3_homepage = S3HomePage(self.driver, authenticate=True)
        bucket_name = self.create_s3_bucket(upload_file=False)

        self.s3_homepage.access_page()

        # When user select radio button next to any row of bucket info that has files in
        # Then user should see the radio button is ticked
        self.s3_homepage.select_s3_bucket(bucket_name)

        # And the details of bucket are displayed at the section below #todo
        '''
            Wait for issue https://gitlab-corp.vng.com.vn/tse/engineering-platform/r-n-d/console-storage-s3/-/issues/3
        '''

        # When user click Action button
        # Then user see menu of options dropped down, including Delete
        self.s3_homepage.click_action_button()

        # When user select Delete
        self.s3_homepage.click_delete_option()

        # Then there is a confirmation window pop up
        # And user sees 2 buttons Delete and Cancel
        self.s3_homepage.check_element_existence(
            S3Locators.DELETE_CANCEL_BUTTON
        )
        self.s3_homepage.check_element_existence(
            S3Locators.DELETE_CONFIRM_BUTTON
        )

        # When user clicks Delete
        self.s3_homepage.click_delete_confirm_button()


        # Then user receives a successful notification popup
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(S3Locators.DELETE_BUCKET_SUCCESSFUL_ALERT)),
        self.assertTrue(
            self.s3_homepage.check_element_existence(S3Locators.DELETE_BUCKET_SUCCESSFUL_ALERT)
        )

        # And the bucket is successfully deleted
        ## Wait till the row of the bucket disappear
        self.keep_trying(
            lambda : WebDriverWait(self.driver, 10).until_not(EC.presence_of_element_located(S3Locators.BUCKET_DATA_ROW(bucket_name))),
            attempts=10,
            unsatisfactory=False
        )
        self.assertFalse(
            self.s3_homepage.check_element_existence(
                S3Locators.BUCKET_DATA_ROW(bucket_name)
            ),
            f"ERROR: Bucket {bucket_name} should not exist."
        )

    def _test_upload_non_empty_bucket_non_successful(self):
        '''
            Non-empty bucket must not be deleted
        '''
        pass
        


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
