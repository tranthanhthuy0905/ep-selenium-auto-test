import os
import urllib.parse
import posixpath

CE_USER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MGRkZTNkZWY0NDUzMDAwMTkzMGIzMDEiLCJuYW1lIjoicXVhbmxoMiIsInNldHRpbmdzIjp7ImxheW91dFRoZW1lIjoic2xhdGVEYXJrMSIsInRpbWVab25lIjoiQXNpYS9Ib19DaGlfTWluaCJ9LCJ1c2VySW5mbyI6eyJidXNpbmVzc1Bob25lcyI6WyIwOTM3NDkyNDM4Il0sImVtcGxveWVlSWQiOiJWRy0xNDA0NCIsImRpc3BsYXlOYW1lIjoiUXXDom4uIEzDom0gSG_DoG5nICgyKSIsImRlcGFydG1lbnQiOiJEYXRhIFBsYXRmb3JtIiwiam9iVGl0bGUiOiJBc3NvY2lhdGUgRGF0YSBFbmdpbmVlciIsIm1haWwiOiJxdWFubGgyQHZuZy5jb20udm4iLCJtb2JpbGVQaG9uZSI6IigrODQpIDA5Mzc0OTI0MzgifSwicm9sZXMiOlsiVVNFUiJdLCJyaWdodCI6WyJURVNUIl0sIl9pZCI6IjYwZGRlM2RlZjQ0NTMwMDAxOTMwYjMwMSIsInVzZXIiOiJxdWFubGgyIiwic3RhdHVzIjoiQUNUSVZFIiwibGFzdExvZ2luIjoiMjAyMS0wNy0wMVQxNTo0ODo0Ni40MDdaIiwiY3JlYXRlZEF0IjoiMjAyMS0wNy0wMVQxNTo0ODo0Ni40MDlaIiwiaWQiOiI2MGRkZTNkZWY0NDUzMDAwMTkzMGIzMDEiLCJpYXQiOjE2MjUxNTQ1MjYsImV4cCI6MTYyNTI0MDkyNn0.yZypViT6zX63QX64po7Jcs9f9x9U-L__0zIHyc3ovKA"
S3_USER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MGQ0MjA2ODViZjgwNjAwMTgwNmUwMTQiLCJuYW1lIjoicXVhbmxoMiIsInNldHRpbmdzIjp7ImxheW91dFRoZW1lIjoic2xhdGVEYXJrMSIsInRpbWVab25lIjoiQXNpYS9Ib19DaGlfTWluaCJ9LCJ1c2VySW5mbyI6eyJidXNpbmVzc1Bob25lcyI6WyIwOTM3NDkyNDM4Il0sImVtcGxveWVlSWQiOiJWRy0xNDA0NCIsImRpc3BsYXlOYW1lIjoiUXXDom4uIEzDom0gSG_DoG5nICgyKSIsImRlcGFydG1lbnQiOiJEYXRhIFBsYXRmb3JtIiwiam9iVGl0bGUiOiJBc3NvY2lhdGUgRGF0YSBFbmdpbmVlciIsIm1haWwiOiJxdWFubGgyQHZuZy5jb20udm4iLCJtb2JpbGVQaG9uZSI6IigrODQpIDA5Mzc0OTI0MzgifSwic3RhdHVzIjoiQUNUSVZFIiwicm9sZXMiOlsiVVNFUiJdLCJyaWdodCI6WyJURVNUIl0sIl9pZCI6IjYwZDQyMDY4NWJmODA2MDAxODA2ZTAxNCIsInVzZXIiOiJxdWFubGgyIiwibGFzdExvZ2luIjoiMjAyMS0wNy0wMVQxNTo1NDozMi4zMDhaIiwiY3JlYXRlZEF0IjoiMjAyMS0wNi0yNFQwNjowNDoyNC4xMTZaIiwidXBkYXRlZEF0IjoiMjAyMS0wNy0wMVQxNTo1NDozMi4zMTFaIiwidXBkYXRlZEJ5IjoiNjBkNDIwNjg1YmY4MDYwMDE4MDZlMDE0IiwiaWQiOiI2MGQ0MjA2ODViZjgwNjAwMTgwNmUwMTQiLCJpYXQiOjE2MjUxNTQ4NzIsImV4cCI6MTYyNTI0MTI3Mn0.Naa-l7HxsVi2X9dIGMy0BqXd6yc4x733pWOTxozb5Vg"

CE_BASE_URL = "https://staging-ce.engineering.vng.vn/ce/"
CE_VOLUME_URL = posixpath.join(CE_BASE_URL, "elastic-block-store/volumes")
CE_CREATE_VOLUME_URL = posixpath.join(CE_VOLUME_URL, "create-volume")
CE_INSTANCE_URL = posixpath.join(CE_BASE_URL, "instances")
CE_INSTANCE_CREATE_WIZARD_URL = posixpath.join(CE_BASE_URL, "launch-instance-wizard")

CE_API_URL = "https://staging-ce.engineering.vng.vn/api/client/"
CE_INSTANCE_API_CLIENT_URL = urllib.parse.urljoin(CE_API_URL, "instances/")
CE_KEYPAIR_API_CLIENT_URL = urllib.parse.urljoin(CE_API_URL, "keypairs/")
CE_VOLUME_API_CLIENT_URL = urllib.parse.urljoin(CE_API_URL, "volumes/")

CE_SG_URL = "https://staging-ce.engineering.vng.vn/ce/network/security-groups/"
CE_SG_CREATE_URL = urllib.parse.urljoin(CE_SG_URL, "create-security-group")
CE_SG_DETAILS_PAGE_URL = urllib.parse.urljoin(CE_SG_URL, "{sg_id}")

CE_SG_API_URL = "https://staging-ce.engineering.vng.vn/api/client/security-groups"

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
