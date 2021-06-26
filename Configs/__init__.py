import os
import urllib.parse

USER_TOKEN = ""
COOKIE = { "name": "user-token", "value": USER_TOKEN}

S3_BASE_URL="https://staging-s3.engineering.vng.vn/s3/"
S3_BUCKET_CREATE_URL = urllib.parse.urljoin(S3_BASE_URL, "buckets/create")
S3_BUCKET_DETAILS_URL = urllib.parse.urljoin(S3_BASE_URL, "buckets/{bucket_name}")


CHROME_DRIVER_PATH = os.path.join(os.getcwd(), "Drivers/chromedriver")
CHROME_CONFIGS = []