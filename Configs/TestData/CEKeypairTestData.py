from Configs.TestData.BaseTestData import BaseTestData
import random

class CEKeypairTestData(BaseTestData):
    KEYPAIR_NAME = "autotest-keypair-" + str(random.randint(100000,999999))
    PUBLIC_KEY = "autotest-keypair-" + str(random.randint(100000,999999))

