from Configs.TestData.BaseTestData import BaseTestData
import random

class S3TestData(BaseTestData):
    BUCKET_NAME = "thuytt7-test-CE-Instance" + str(random.randint(100000,999999))
    BUCKET_REGION = "VNG Campus (Staging)"
