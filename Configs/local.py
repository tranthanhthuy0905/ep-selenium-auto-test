import os
import urllib.parse
import posixpath

CE_USER_TOKEN = ""
S3_USER_TOKEN = ""

CE_BASE_URL = "https://staging-ce.engineering.vng.vn/ce/"
CE_VOLUME_URL = posixpath.join(CE_BASE_URL, "elastic-block-store/volumes")
CE_CREATE_VOLUME_URL = posixpath.join(CE_VOLUME_URL, "create-volume")
CE_INSTANCE_URL = posixpath.join(CE_BASE_URL, "instances")
CE_INSTANCE_CREATE_WIZARD_URL = posixpath.join(CE_BASE_URL, "launch-instance-wizard")

CE_API_URL = "https://staging-ce.engineering.vng.vn/api/client/"
CE_INSTANCE_API_CLIENT_URL = urllib.parse.urljoin(CE_API_URL, "instances/")
CE_KEYPAIR_API_CLIENT_URL = urllib.parse.urljoin(CE_API_URL, "keypairs/")
CE_VOLUME_API_CLIENT_URL = urllib.parse.urljoin(CE_API_URL, "volumes/")

CE_SG_URL = "https://console.engineering.vng.vn/ec2/network/security-groups"
CE_SG_CREATE_URL = "https://console.engineering.vng.vn/ec2/network/security-groups/create-security-group"


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
