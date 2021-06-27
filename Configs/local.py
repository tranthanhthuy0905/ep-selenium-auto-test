import os
import urllib.parse

USER_TOKEN = ""
COOKIE = { "name": "user-token", "value": USER_TOKEN}

EC2_BASE_URL = "http://staging-ce.engineering.vng.vn/"

S3_BASE_URL = "https://staging-s3.engineering.vng.vn/s3/"
S3_BUCKET_URL = urllib.parse.urljoin(S3_BASE_URL, "buckets/")
S3_BUCKET_CREATE_URL = urllib.parse.urljoin(S3_BUCKET_URL, "create")
S3_BUCKET_DETAILS_URL = urllib.parse.urljoin(S3_BUCKET_URL, "{bucket_name}")

S3_BUCKET_API_CLIENT_URL = "https://staging-s3.engineering.vng.vn/api/client/buckets"


CHROME_DRIVER_PATH = os.path.join(os.getcwd(), "Drivers/chromedriver")
CHROME_CONFIGS = []