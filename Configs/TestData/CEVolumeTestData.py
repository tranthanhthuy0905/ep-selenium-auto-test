from Configs.TestData.BaseTestData import BaseTestData
import random

class CEVolumeTestData(BaseTestData):
    VOLUME_NAME = "nhantnc-ce-autotest-volume" + str(random.randint(100000,999999))
    SIZE = str(random.randint(1,200))

    SIZE1 = str(random.randint(1, 99))

    SIZE2 = str(random.randint(101, 500))
