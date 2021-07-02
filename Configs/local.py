import os
import urllib.parse
import posixpath

DF_USER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MGRlNzVhZGM3Y2M1ZTAwMThmNGZkYmUiLCJuYW1lIjoiaGFuZ2x0dDMiLCJpYXQiOjE2MjUxOTE4NTMsImV4cCI6MTYyNTI3ODI1M30.Xy9l6ORBErsaK7YX_SE_Y6quI6Tnys0KLgJabhUB1Ps"
CE_USER_TOKEN = ""
S3_USER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MGRiZGNkZmM1ZTQ3NzAwMTE0NWRkODYiLCJuYW1lIjoicXVhbmxoMiIsImlhdCI6MTYyNTIxOTE5NywiZXhwIjoxNjI1MzA1NTk3fQ.owueftaI-nLge6Zfv518foM_g_xQ6G7P2ZPnBD8Qlxs"

CE_BASE_URL = "https://staging-ce.engineering.vng.vn/ce/"
CE_VOLUME_URL = posixpath.join(CE_BASE_URL, "elastic-block-store/volumes")
CE_CREATE_VOLUME_URL = posixpath.join(CE_VOLUME_URL, "create-volume")
CE_INSTANCE_URL = posixpath.join(CE_BASE_URL, "instances")
CE_INSTANCE_CREATE_WIZARD_URL = posixpath.join(CE_BASE_URL, "launch-instance-wizard")

CE_API_URL = "https://staging-ce.engineering.vng.vn/api/client/"
CE_INSTANCE_API_CLIENT_URL = urllib.parse.urljoin(CE_API_URL, "instances/")
CE_KEYPAIR_API_CLIENT_URL = urllib.parse.urljoin(CE_API_URL, "keypairs/")
CE_VOLUME_API_CLIENT_URL = urllib.parse.urljoin(CE_API_URL, "volumes/")
CE_SECURITY_GROUP_API_CLIENT_URL = urllib.parse.urljoin(CE_API_URL, "security-groups/")

CE_SG_URL = "https://staging-ce.engineering.vng.vn/ce/network/security-groups/"
CE_SG_CREATE_URL = urllib.parse.urljoin(CE_SG_URL, "create-security-group")
CE_SG_DETAILS_PAGE_URL = urllib.parse.urljoin(CE_SG_URL, "{sg_id}")

CE_SG_API_URL = "https://staging-ce.engineering.vng.vn/api/client/security-groups"

'''
S3
'''
S3_BASE_URL = "https://s3.engineering.vng.vn/s3/"
S3_BUCKET_URL = urllib.parse.urljoin(S3_BASE_URL, "buckets/")
S3_BUCKET_CREATE_URL = urllib.parse.urljoin(S3_BUCKET_URL, "create")
S3_BUCKET_DETAILS_URL = urllib.parse.urljoin(S3_BUCKET_URL, "{bucket_name}")
S3_BUCKET_FILE_UPLOAD_URL = urllib.parse.urljoin(S3_BUCKET_URL, "{bucket_name}/upload",)

S3_API_BASE_URL = "https://s3.engineering.vng.vn/api/client/"
S3_BUCKET_API_CLIENT_URL = urllib.parse.urljoin(S3_API_BASE_URL, "buckets")
S3_FILES_API_CLIENT_URL = urllib.parse.urljoin(S3_API_BASE_URL, "files")

FILE_PATH_UPLOAD_SAMPLE = os.path.join(os.getcwd(), "Configs/TestData/sample_files/first.txt")

CHROME_DRIVER_PATH = os.path.join(os.getcwd(), "Drivers/chromedriver")
LOG_FILE_PATH = os.path.join(os.getcwd(), "Reports/logs")

DF_BASE_URL = "https://staging-mobilefarm.engineering.vng.vn/devicefarm/mobile-device"