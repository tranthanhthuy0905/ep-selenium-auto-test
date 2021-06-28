import os
import urllib.parse

S3_USER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MGQ0MjA2ODViZjgwNjAwMTgwNmUwMTQiLCJuYW1lIjoicXVhbmxoMiIsImlhdCI6MTYyNDg0NDE0MSwiZXhwIjoxNjI0OTMwNTQxfQ.MVLUQvzsWjxu8L1dBWDkUUR8l1Av-15RLnhgyaQXZZQ"

EC2_BASE_URL = "http://staging-ce.engineering.vng.vn/"


'''
S3
'''
S3_BASE_URL = "https://staging-s3.engineering.vng.vn/s3/"
S3_BUCKET_URL = urllib.parse.urljoin(S3_BASE_URL, "buckets/")
S3_BUCKET_CREATE_URL = urllib.parse.urljoin(S3_BUCKET_URL, "create")
S3_BUCKET_DETAILS_URL = urllib.parse.urljoin(S3_BUCKET_URL, "{bucket_name}")
S3_BUCKET_FILE_UPLOAD_URL = urllib.parse.urljoin(S3_BUCKET_URL, "{bucket_name}/upload",)

S3_API_BASE_URL = "https://staging-s3.engineering.vng.vn/api/client/"
S3_BUCKET_API_CLIENT_URL = urllib.parse.urljoin(S3_API_BASE_URL, "buckets")
S3_FILES_API_CLIENT_URL = urllib.parse.urljoin(S3_API_BASE_URL, "files")

FILE_PATH_UPLOAD_SAMPLE = os.path.join(os.getcwd(), "Configs/TestData/sample_files/first.txt")

CHROME_DRIVER_PATH = os.path.join(os.getcwd(), "Drivers/chromedriver")
LOG_FILE_PATH = os.path.join(os.getcwd(), "Reports/logs")
CHROME_CONFIGS = []