from Configs.TestData.BaseTestData import BaseTestData
import time
import random

class CEInstanceTestData(BaseTestData):
    INSTANCE_NAME = "autotest-instance-" + str(time.time()).replace('.', '')
    DEFAULT_PASSWORD = "autotest" + str(random.randint(100000,999999))
    STOP_STATUS = "stop"
    RUNNING_STATUS = "start"

    MACHINE_IMAGE = "Ubuntu20_Stable"

    def gen_instance_name():
        return "autotest-instance-" + str(time.time()).replace('.', '')

