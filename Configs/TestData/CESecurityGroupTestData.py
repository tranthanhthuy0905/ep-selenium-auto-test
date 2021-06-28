from Configs.TestData.BaseTestData import BaseTestData
import random

class CESecurityGroupTestData(BaseTestData):
    SECURITY_GROUP_NAME = "nhantnc-ce-autotest-sg" + str(random.randint(100000,999999))
    DESCRIPTION = "nhantnc-ce-autotest-sg" + str(random.randint(100000,999999))
