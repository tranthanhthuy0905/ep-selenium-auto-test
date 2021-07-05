from Configs.TestData.BaseTestData import BaseTestData
import random

class S3TestData(BaseTestData):
    BUCKET_NAME = "quanlh2-test-hehe-" + str(random.randint(100000,999999))
    BUCKET_REGION = "VNG Campus"