from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tests.base_test import BaseTest
from Configs import S3_BUCKET_API_CLIENT_URL, S3_FILES_API_CLIENT_URL
from Configs import S3_BUCKET_DETAILS_URL
from Configs import S3_USER_TOKEN
from Pages.s3.s3_homepage import S3HomePage
from Pages.s3.s3_create_bucket_page import S3CreateBucketPage
from Pages.s3.s3_bucket_details_page import S3BucketDetailsPage



class S3BaseTest(BaseTest):
    def _call_api_delete_s3_bucket(self, bucket_name):
        try:
            url = S3_BUCKET_API_CLIENT_URL
            params = {
                "bucket_name": bucket_name
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

    def delete_s3_buckets(self):
        bucket_name = self.service_slug
        self.delete_bucket_files(bucket_name)
    
    def delete_bucket_files(self,bucket_name):
        #TODO: Refactor
        files_info = self._call_api_get_bucket_files(bucket_name)
        list_filenames = []
        try:
            if files_info and files_info["count"] > 0:
                print("FILES INFO:", files_info)
                for item in files_info["results"]["contents"]:
                    list_filenames.append(item["key"])
        except Exception as e:
            print("Can't get filenames to delete;", str(e))
        
        print(f"List files to delete in bucket {bucket_name}:", list_filenames)
        if list_filenames:
            for filename in list_filenames:
                self._call_api_delete_bucket_files(bucket_name, filename)
        
        self._call_api_delete_s3_bucket(bucket_name)


    def _call_api_delete_bucket_files(self, bucket_name, filename):
        url = S3_FILES_API_CLIENT_URL
        try:
            params = {
                "bucket_name": bucket_name,
                "object_key": filename
            }
            self._call_request_delete(url, params, S3_USER_TOKEN)
        except Exception as e:
            print("Can't delete S3 files;", str(e))

    def _call_api_get_bucket_files(self, bucket_name):
        url = S3_FILES_API_CLIENT_URL
        try:
            params = {
                "bucket_name": bucket_name,
            }
            self._call_request_get(url, params, S3_USER_TOKEN)
        except Exception as e:
            print("Can't delete S3 files;", str(e))

    def _call_api_get_bucket_files(self, bucket_name):
        url = S3_FILES_API_CLIENT_URL
        try:
            params = {
                "bucket_name": bucket_name
            }
            return self._call_request_get(url, params, S3_USER_TOKEN)
        except Exception as e:
            print("Can't list S3 files;", str(e))
        


