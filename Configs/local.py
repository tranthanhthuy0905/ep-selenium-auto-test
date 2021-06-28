import os
import urllib.parse

DASHBOARD_USER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MGQzZmRmY2U0M2Q3NjAwMTk5YmZhNzIiLCJuYW1lIjoidGh1eXR0NyIsImlhdCI6MTYyNDg4MjIzOCwiZXhwIjoxNjI0OTY4NjM4fQ.-7vmUrypJ3AtJwu9XTD2rxMNYIfWUAbw95zJ_VetLh0"
DASHBOARD_BASE_URL = "https://staging-console.engineering.vng.vn/dashboard"

EC2_USER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MGQ5OTIwODhlNDM1MjAwMTg5ZTNmNzMiLCJuYW1lIjoidGh1eXR0NyIsImlhdCI6MTYyNDg3MTQ1MSwiZXhwIjoxNjI0OTU3ODUxfQ.jbFSM7yW4J10Qdha_IG43MiHSJzouAuub9m3imZ_cwc"
EC2_BASE_URL = "https://staging-ce.engineering.vng.vn/ce/"
EC2_INSTANCE_URL = urllib.parse.urljoin(EC2_BASE_URL, "instances")
EC2_INSTANCE_CREATE_WIZARD_URL = urllib.parse.urljoin(EC2_BASE_URL, "launch-instance-wizard")

S3_USER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MGQ0MjA2ODViZjgwNjAwMTgwNmUwMTQiLCJuYW1lIjoicXVhbmxoMiIsImlhdCI6MTYyNDg0NDE0MSwiZXhwIjoxNjI0OTMwNTQxfQ.MVLUQvzsWjxu8L1dBWDkUUR8l1Av-15RLnhgyaQXZZQ"
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
CHROME_CONFIGS = []
