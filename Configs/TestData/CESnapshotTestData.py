from Configs.TestData.BaseTestData import BaseTestData
import random

class CESnapshotTestData(BaseTestData):
    SNAPSHOT_NAME = "thuytt7-snapshot-" + str(random.randint(100000,999999))
