
from Pages.base_page import BasePage
from Configs import S3_BUCKET_DETAILS_URL

class S3BucketDetailsPage(BasePage):
    def __init__(self, driver, bucket_name):
        super().__init__(driver=driver, base_url=S3_BUCKET_DETAILS_URL.format(bucket_name=bucket_name))