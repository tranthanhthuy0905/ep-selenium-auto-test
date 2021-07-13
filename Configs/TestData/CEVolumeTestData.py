from Configs.TestData.BaseTestData import BaseTestData
import random
import time

class CEVolumeTestData(BaseTestData):
    VOLUME_NAME = "autotest-volume-" + str(random.randint(100000,999999))
    SIZE = str(random.randint(1,200))

    SIZE1 = str(random.randint(1, 99))

    SIZE2 = str(random.randint(101, 500))

    ALLOCATED = "Allocated"

    def gen_volume_name():
        return "autotest-volume-" + str(time.time()).replace('.', '')

    def gen_volume_size():
        return str(random.randint(1,200))