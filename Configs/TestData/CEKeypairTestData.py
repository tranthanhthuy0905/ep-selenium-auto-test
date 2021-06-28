from Configs.TestData.BaseTestData import BaseTestData
import random

class CEKeypairTestData(BaseTestData):
    KEYPAIR_NAME = "nhantnc-ce-autotest-keypair" + str(random.randint(100000,999999))
    PUBLIC_KEY = "nhantnc-ce-autotest-keypair" + str(random.randint(100000,999999))

