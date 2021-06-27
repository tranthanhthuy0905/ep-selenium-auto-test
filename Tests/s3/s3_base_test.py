
from Tests.base_test import BaseTest
from Configs import S3_BUCKET_API_CLIENT_URL

class S3BaseTest(BaseTest):
    def delete_s3_bucket(self):
        try:
            url = S3_BUCKET_API_CLIENT_URL
            params = {
                "bucket_name": self.service_slug
            }
            self._call_request_delete(url, params)
        except Exception as e:
            print("Can't delete S3 bucket;", str(e))