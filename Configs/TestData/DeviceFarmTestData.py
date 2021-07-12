from Configs.TestData.BaseTestData import BaseTestData
import random

class DEVICE_FARM_TestData(BaseTestData):
    PROJECT_NAME = "selenium-test-project-" + str(random.randint(100000,999999))
    PROJECT_REGION = "VNG Campus (Staging)"
    SESSION_NAME = "selenium-test-session-" + str(random.randint(100000, 999999))
    GALAXY_TAB_E_SERIAL = "3801b6264398b200"
    LG_G5_SE = "LGH84598611fed"
    XPERIA_AQA = "YT911BL3PZ"
    PIXEL_3 = "3801b6264398b200"
    LIVE = "AHW00016144"
    PIXEL = "FA72A0304440"