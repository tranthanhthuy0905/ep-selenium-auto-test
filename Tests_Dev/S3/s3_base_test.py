import logging

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tests_Dev.base_test import BaseTest
from Configs import S3_BUCKET_API_CLIENT_URL, S3_FILES_API_CLIENT_URL
from Configs import S3_BUCKET_DETAILS_URL
from Configs import S3_USER_TOKEN
from Pages.S3.s3_homepage import S3HomePage
from Pages.S3.s3_create_bucket_page import S3CreateBucketPage
from Pages.S3.s3_bucket_details_page import S3BucketDetailsPage, S3BucketFilesAndFoldersPage

class S3BaseTest(BaseTest):

    def setup_test_instances(self):
        self.bucket_name = None
        self.buckets_list = []

    def clear_test_instances(self):
        self.delete_s3_bucket()
        self.delete_s3_buckets()

    def delete_s3_bucket(self):
        try:
            bucket_name = self.bucket_name
            assert bucket_name
        except:
            return None
        self._exec_delete_bucket(bucket_name)

    def delete_s3_buckets(self):
        try:
            buckets_list = self.buckets_list
            assert buckets_list
        except:
            return None
        for bucket_name in buckets_list:
            self._exec_delete_bucket(bucket_name)

    def _exec_delete_bucket(self, bucket_name):
        self.delete_bucket_files(bucket_name)
        self._call_api_delete_s3_bucket(bucket_name)


    def _call_api_delete_s3_bucket(self, bucket_name):
        try:
            url = S3_BUCKET_API_CLIENT_URL
            params = {
                "bucket_name": bucket_name
            }
            self._call_request_delete(url, params, S3_USER_TOKEN)
        except Exception as e:
            logging.error("Can't delete S3 bucket;", str(e))

    def create_s3_bucket(self, upload_file=False):
        self.s3_homepage = S3HomePage(self.driver, authenticate=False)
        self.s3_homepage.click_create_bucket()
        self.s3_create_bucket_page = S3CreateBucketPage(self.driver)
        bucket_name = self.s3_create_bucket_page.fill_bucket_create_information()
        self.service_slug = bucket_name
        self.s3_create_bucket_page.click_create_bucket_submit_button()
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, 10).until(EC.url_to_be(S3_BUCKET_DETAILS_URL.format(bucket_name=bucket_name)))
        if upload_file:
            # TODO: Can check selenium timeout here by removing if
            self.upload_files_to_bucket(bucket_name)

        return bucket_name

    def upload_files_to_bucket(self, bucket_name):
        self.s3_bucket_details_page = S3BucketDetailsPage(self.driver, bucket_name)
        self.s3_bucket_details_page.access_page()
        self.s3_bucket_details_page.click_upload_file()

        self.s3_files_and_folders_page = S3BucketFilesAndFoldersPage(self.driver, bucket_name)
        self.s3_files_and_folders_page.upload_file_from_browser()

    def delete_bucket_files(self,bucket_name):
        #TODO: Refactor
        files_info = self._call_api_get_bucket_files(bucket_name)
        list_filenames = []
        try:
            if files_info and files_info["count"] > 0:
                for item in files_info["results"]["contents"]:
                    list_filenames.append(item["key"])
        except Exception as e:
            logging.error("Can't get filenames to delete;", str(e))

        logging.info(f"List files to delete in bucket {bucket_name}: {list_filenames}")
        if list_filenames:
            for filename in list_filenames:
                self._call_api_delete_bucket_files(bucket_name, filename)

    def _call_api_delete_bucket_files(self, bucket_name, filename):
        url = S3_FILES_API_CLIENT_URL
        try:
            params = {
                "bucket_name": bucket_name,
                "object_key": filename
            }
            self._call_request_delete(url, params, S3_USER_TOKEN)
        except Exception as e:
            logging.error("Can't delete S3 files;", str(e))

    def _call_api_get_bucket_files(self, bucket_name):
        url = S3_FILES_API_CLIENT_URL
        try:
            params = {
                "bucket_name": bucket_name
            }
            return self._call_request_get(url, params, S3_USER_TOKEN)
        except Exception as e:
            logging.error("Can't list S3 files;", str(e))



