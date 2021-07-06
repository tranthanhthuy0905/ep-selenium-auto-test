from Configs.TestData.BaseTestData import BaseTestData
import random

class CEVolumeTestData(BaseTestData):
    VOLUME_NAME = "autotest-volume-" + str(random.randint(100000,999999))
    SIZE = str(random.randint(1,200))
    ALLOCATED = "Allocated"
