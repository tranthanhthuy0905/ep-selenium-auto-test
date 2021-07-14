from Configs.TestData.BaseTestData import BaseTestData
import random

class RDSTestData(BaseTestData):
    CLUSTER_NAME = "autotest-postgres-" + str(random.randint(100000, 999999))
    NO_OF_REPLICA1 = random.randint(0,1)
    NO_OF_REPLICA2 = random.randint(2,3)
