from Configs.TestData.BaseTestData import BaseTestData
import random

class EFSTestData(BaseTestData):
    FILESYSTEM_NAME = "autotest-efs-" + str(random.randint(100000,999999))
