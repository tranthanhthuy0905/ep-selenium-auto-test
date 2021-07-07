import os
import unittest
import time 

import HtmlTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tests_Dev.device_farm.devicefarm_base_test import DEVICE_FARM_BaseTest
from Pages.device_farm.devicefarm_homepage import DEVICE_FARM_HomePage
from Pages.device_farm.devicefarm_stop_session_page import DEVICE_FARM_StopSessionPage

from Locators.device_farm import DEVICE_FARM_ProjectLocators
from Configs.TestData.DeviceFarmTestData import DEVICE_FARM_TestData
class Test_DEVICEFARM_Stop_Session(DEVICE_FARM_BaseTest):
    def test_stop_session_successful(self):
        """
            TEST CASE: DF Session should be stopped successfully
        """
        print("---create project-------")
        self.project_text = DEVICE_FARM_TestData()
        self._call_api_create_project(self.project_text.PROJECT_NAME)
        print("------get info project--------")
        project_info = self._call_api_get_info_project()
        print("-------create session---------")
        self._call_api_create_session(project_info[0].get('_id'), self.project_text.LG_G5_SE)
        print("-----begin stop session----------")
        self.df_homepage = DEVICE_FARM_HomePage(self.driver)
        self.df_session = DEVICE_FARM_StopSessionPage(self.driver)
        self.df_session.click_stop_session_submit_button()
        time.sleep(2)
        self.assertIn("Session is stopped successfully", self.driver.page_source, msg='STOP SESSION IS NOT SUCCESSFULLY')
        
if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )