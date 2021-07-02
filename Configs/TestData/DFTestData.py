from Configs.TestData.BaseTestData import BaseTestData
import random

class DFTestData(BaseTestData):
    PROJECT_NAME = "selenium-test-" + str(random.randint(100000,999999))
    PROJECT_REGION = "VNG Campus (Staging)"