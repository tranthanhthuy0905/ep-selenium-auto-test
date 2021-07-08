import os
import urllib.parse
import posixpath

from dotenv import load_dotenv

load_dotenv()

# AUTHENTICATION
# Note: Configure in .env file, .env file should not be pushed to git.
DEVICE_FARM_USER_TOKEN = os.getenv("DEVICE_FARM_USER_TOKEN", "")
CE_USER_TOKEN = os.getenv("CE_USER_TOKEN", "")
S3_USER_TOKEN = os.getenv("S3_USER_TOKEN", "")

# Common
FILE_PATH_UPLOAD_SAMPLE = os.path.abspath("Configs/TestData/sample_files/first.txt")
CHROME_DRIVER_PATH = os.path.abspath("Drivers/chromedriver")
LOG_FILE_PATH = os.path.abspath("Reports/logs")

# CE
CE_BASE_URL = os.path.join(os.getenv("CE_BASE_URL"), "ce/")
CE_API_URL = urllib.parse.urljoin(os.getenv("CE_BASE_URL"), "api/client/")

CE_VOLUME_URL = posixpath.join(CE_BASE_URL, "elastic-block-store/volumes")
CE_SNAPSHOT_URL = posixpath.join(CE_BASE_URL, "elastic-block-store/snapshots")
CE_CREATE_VOLUME_URL = posixpath.join(CE_VOLUME_URL, "create-volume")
CE_INSTANCE_URL = posixpath.join(CE_BASE_URL, "instances")
CE_KEYPAIR_URL = posixpath.join(CE_BASE_URL, "keypair")

CE_INSTANCE_API_CLIENT_URL = urllib.parse.urljoin(CE_API_URL, "instances/")
CE_KEYPAIR_API_CLIENT_URL = urllib.parse.urljoin(CE_API_URL, "keypairs/")
CE_VOLUME_API_CLIENT_URL = urllib.parse.urljoin(CE_API_URL, "volumes/")
CE_SNAPSHOT_API_CLIENT_URL = urllib.parse.urljoin(CE_API_URL, "snapshot-volume/")
CE_SG_API_CLIENT_URL = urllib.parse.urljoin(CE_API_URL, "security-groups/")

CE_SG_URL = urllib.parse.urljoin(CE_BASE_URL, "network/security-groups/")
CE_SG_CREATE_URL = urllib.parse.urljoin(CE_SG_URL, "create-security-group")
CE_SG_DETAILS_PAGE_URL = urllib.parse.urljoin(CE_SG_URL, "{sg_id}")

CE_SG_KEYPAIR_HOMEPAGE_URL = urllib.parse.urljoin(CE_BASE_URL, "keypair") #Should keypair be plural??

CE_INSTANCE_CREATE_WIZARD_URL = posixpath.join(CE_BASE_URL, "launch-instance-wizard")
CE_SG_API_URL = urllib.parse.urljoin(CE_API_URL, "security-groups")
CE_KEYPAIR_API_URL = urllib.parse.urljoin(CE_API_URL, "keypairs/{keypair_name}")

# S3
S3_BASE_URL = urllib.parse.urljoin(os.getenv("S3_BASE_URL"), "s3/")
S3_API_BASE_URL = urllib.parse.urljoin(os.getenv("S3_BASE_URL"), "api/client")

S3_BUCKET_URL = urllib.parse.urljoin(S3_BASE_URL, "buckets/")
S3_BUCKET_CREATE_URL = urllib.parse.urljoin(S3_BUCKET_URL, "create")
S3_BUCKET_DETAILS_URL = urllib.parse.urljoin(S3_BUCKET_URL, "{bucket_name}")
S3_BUCKET_FILE_UPLOAD_URL = urllib.parse.urljoin(S3_BUCKET_URL, "{bucket_name}/upload",)

S3_BUCKET_API_CLIENT_URL = urllib.parse.urljoin(S3_API_BASE_URL, "buckets")
S3_FILES_API_CLIENT_URL = urllib.parse.urljoin(S3_API_BASE_URL, "files")

# Device Farm
DEVICE_FARM_BASE_URL = urllib.parse.urljoin(os.getenv("DEVICE_FARM_BASE_URL"), "devicefarm/mobile-device")
