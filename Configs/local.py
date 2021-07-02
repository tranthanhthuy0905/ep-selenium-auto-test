import os
import urllib.parse
import posixpath

CE_USER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MGRkZjJlMmY0NDUzMDAwMTkzMGIzMDgiLCJuYW1lIjoidGh1eXR0NyIsInNldHRpbmdzIjp7ImxheW91dFRoZW1lIjoic2xhdGVEYXJrMSIsInRpbWVab25lIjoiQXNpYS9Ib19DaGlfTWluaCJ9LCJ1c2VySW5mbyI6eyJidXNpbmVzc1Bob25lcyI6WyIwOTQxMjEwOTAwIl0sImVtcGxveWVlSWQiOiJWRy0xNTQwNyIsImRpc3BsYXlOYW1lIjoiVGjDunkuIFRy4bqnbiBUaGFuaCAoNykiLCJkZXBhcnRtZW50IjoiRGF0YSBQbGF0Zm9ybSIsImpvYlRpdGxlIjoiU29mdHdhcmUgRGV2ZWxvcG1lbnQgSW50ZXJuIiwibWFpbCI6InRodXl0dDdAdm5nLmNvbS52biIsIm1vYmlsZVBob25lIjoiKCs4NCkgMDk0MTIxMDkwMCJ9LCJyb2xlcyI6WyJVU0VSIl0sInJpZ2h0IjpbIlRFU1QiXSwiX2lkIjoiNjBkZGYyZTJmNDQ1MzAwMDE5MzBiMzA4IiwidXNlciI6InRodXl0dDciLCJzdGF0dXMiOiJBQ1RJVkUiLCJsYXN0TG9naW4iOiIyMDIxLTA3LTAxVDE2OjUyOjUwLjk1MFoiLCJjcmVhdGVkQXQiOiIyMDIxLTA3LTAxVDE2OjUyOjUwLjk1M1oiLCJpZCI6IjYwZGRmMmUyZjQ0NTMwMDAxOTMwYjMwOCIsImlhdCI6MTYyNTE1ODM3MCwiZXhwIjoxNjI1MjQ0NzcwfQ.GbBzp3157vOSxHIO8GXGzRJ18kr3M9Zvyh-a_sxGEqQ"
S3_USER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2MGQ5OTIwODhlNDM1MjAwMTg5ZTNmNzMiLCJuYW1lIjoidGh1eXR0NyIsImlhdCI6MTYyNDg5MDY3OSwiZXhwIjoxNjI0OTc3MDc5fQ.eZSGEZPn-xkcOnBizWgceKPCuYXPINqzbl7nrDlnKHQ"

CE_BASE_URL = "https://staging-ce.engineering.vng.vn/ce/"
CE_VOLUME_URL = posixpath.join(CE_BASE_URL, "elastic-block-store/volumes")
CE_CREATE_VOLUME_URL = posixpath.join(CE_VOLUME_URL, "create-volume")
CE_INSTANCE_URL = posixpath.join(CE_BASE_URL, "instances")
CE_INSTANCE_CREATE_WIZARD_URL = posixpath.join(CE_BASE_URL, "launch-instance-wizard")

CE_API_URL = "https://staging-ce.engineering.vng.vn/api/client/"
CE_INSTANCE_API_CLIENT_URL = urllib.parse.urljoin(CE_API_URL, "instances/")
CE_KEYPAIR_API_CLIENT_URL = urllib.parse.urljoin(CE_API_URL, "keypairs/")
CE_VOLUME_API_CLIENT_URL = urllib.parse.urljoin(CE_API_URL, "volumes/")


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
