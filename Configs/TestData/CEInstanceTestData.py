from Configs.TestData.BaseTestData import BaseTestData
import random

class CEInstanceTestData(BaseTestData):
    INSTANCE_NAME = "autotest-instance-" + str(random.randint(100000,999999))
    DEFAULT_PASSWORD = "autotest" + str(random.randint(100000,999999))
    STOP_STATUS = "stop"
    RUNNING_STATUS = "start"

