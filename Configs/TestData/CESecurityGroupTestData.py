from Configs.TestData.BaseTestData import BaseTestData
import random

class CESecurityGroupTestData(BaseTestData):
    SECURITY_GROUP_NAME = "quanlh2-ce-autotest-sg" + str(random.randint(100000,999999))
    DESCRIPTION = "quanlh2-ce-autotest-sg" + str(random.randint(100000,999999))
    VALID_PORTS_1 = (1, 8000)
    VALID_CIDR_1 = "0.0.0.0/0"
    INVALID_CIDR_1 = "0.0.0.0"

    SG_ID_REGEX = "[A-z0-9]*?-[A-z0-9]*?-[A-z0-9]*?-[A-z0-9]*?"