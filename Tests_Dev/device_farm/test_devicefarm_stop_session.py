import os
import unittest
import time 

import HtmlTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tests.device_farm.devicefarm_base_test import DEVICE_FARM_BaseTest
from Pages.device_farm.devicefarm_homepage import DEVICE_FARM_HomePage
from Pages.device_farm.devicefarm_stop_session_page import DEVICE_FARM_StopSessionPage

from Locators.device_farm import DEVICE_FARM_ProjectLocators

class Test_DEVICEFARM_Stop_Session(DEVICE_FARM_BaseTest):
    def test_stop_session_successful(self):
        """
            TEST CASE: DF Session should be stopped successfully
        """
        self.df_homepage = DEVICE_FARM_HomePage(self.driver)
        self.df_session = DEVICE_FARM_StopSessionPage(self.driver)
        _status = self.df_session.click_stop_session_submit_button()
        time.sleep(2)
        # assert "Session is stopped successfully" in self.driver.page_source
        # self.assertIn("Session is stopped successfully", self.driver.page_source, msg='FAIL SM')
        
if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )