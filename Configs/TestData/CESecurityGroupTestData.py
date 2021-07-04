from Configs.TestData.BaseTestData import BaseTestData
import random

class CESecurityGroupTestData(BaseTestData):
    SECURITY_GROUP_NAME = "autotest-sg-" + str(random.randint(100000,999999))
    DESCRIPTION = "This security group is created by automated testing."
    VALID_PORTS_1 = (1, 8000)
    VALID_PORTS_2 = (5000, 5000)
    INVALID_PORTS_1 = (6666, 5555)
    DEFAULT_CIDR = "0.0.0.0/0"
    VALID_CIDR_1 = "0.0.0.0/0"
    INVALID_CIDR_1 = "0.0.0.0"
    INVALID_CIDR_2 = "abcdef"
    INVALID_CIDR_3 = "0.0.0.0/0.0.0.0"

    SG_ID_REGEX = "[A-z0-9]*?-[A-z0-9]*?-[A-z0-9]*?-[A-z0-9]*?"

    TCP_SELECTION_INDEX = 0
    UDP_SELECTION_INDEX = 1
    ICMP_SELECTION_INDEX = 2
    ALL_SELECTION_INDEX = 3

    UDP_VALUE_IN_TABLE = "udp"