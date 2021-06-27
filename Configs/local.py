import os
import urllib.parse

USER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MGQyZTdiZDBlYjhhNjAwMThmNjdkNjEiLCJuYW1lIjoibmhhbnRuYyIsImlhdCI6MTYyNDc5Mjc4NiwiZXhwIjoxNjI0ODc5MTg2fQ.wyBpG6ItUEht0e09cUXwFm_jqiqIc48khqEpUEFBAUY"
COOKIE = { "name": "user-token", "value": USER_TOKEN}

EC2_BASE_URL = "https://staging-ce.engineering.vng.vn/ce/"
EC2_API_URL = "https://staging-ce.engineering.vng.vn/api/client/"
EC2_VOLUME_URL = urllib.parse.urljoin(EC2_BASE_URL, "elastic-block-store/volumes")
EC2_CREATE_VOLUME_URL = urllib.parse.urljoin(EC2_BASE_URL, "elastic-block-store/volumes/create-volume")
EC2_INSTANCE_URL = urllib.parse.urljoin(EC2_BASE_URL, "instances")
EC2_INSTANCE_CREATE_WIZARD_URL = urllib.parse.urljoin(EC2_BASE_URL, "launch-instance-wizard")
EC2_INSTANCE_API_CLIENT_URL = urllib.parse.urljoin(EC2_API_URL, "instances/")
EC2_KEYPAIR_API_CLIENT_URL = urllib.parse.urljoin(EC2_API_URL, "keypairs/")

S3_BASE_URL = "https://staging-s3.engineering.vng.vn/s3/"
S3_BUCKET_URL = urllib.parse.urljoin(S3_BASE_URL, "buckets/")
S3_BUCKET_CREATE_URL = urllib.parse.urljoin(S3_BUCKET_URL, "create")
S3_BUCKET_DETAILS_URL = urllib.parse.urljoin(S3_BUCKET_URL, "{bucket_name}")

S3_BUCKET_API_CLIENT_URL = "https://staging-s3.engineering.vng.vn/api/client/buckets"


CHROME_DRIVER_PATH = os.path.join(os.getcwd(), "Drivers/chromedriver")
CHROME_CONFIGS = []