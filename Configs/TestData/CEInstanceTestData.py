from Configs.TestData.BaseTestData import BaseTestData
import random

class CEInstanceTestData(BaseTestData):
    INSTANCE_NAME = "nhantnc-ce-autotest-instance" + str(random.randint(100000,999999))
    DEFAULT_PASSWORD = "NhanTNC" + str(random.randint(100000,999999))

