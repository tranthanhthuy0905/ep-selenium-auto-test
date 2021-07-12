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
from Configs.TestData.DeviceFarmTestData import DEVICE_FARM_TestData
class Test_DEVICEFARM_Stop_Session(DEVICE_FARM_BaseTest):
    def test_stop_session_successful(self):
        """
            TEST CASE: DF Session should be stopped successfully
        """
        """
            Step 1: Create a new project.
        """
        self.project_text = DEVICE_FARM_TestData()
        self._call_api_create_project(self.project_text.PROJECT_NAME)
        """
            Step 2: Get info above project.
        """
        project_info = self._call_api_get_info_project()
        """
            Step 3: Create a new session.
        """
        self._call_api_create_session(project_info[0].get('_id'), self.project_text.LG_G5_SE)
        # begin TEST_CASE
        """
            Step 4: TEST_CASE Stop above session
        """
        self.df_homepage = DEVICE_FARM_HomePage(self.driver)
        self.df_session = DEVICE_FARM_StopSessionPage(self.driver)
        self.df_session.click_stop_session_submit_button()
        time.sleep(2)
        self.assertIn("Session is stopped successfully", self.driver.page_source, msg='STOP SESSION IS NOT SUCCESSFULLY')
        # end TEST-CASE
        """
            Step 5: Get info session to get session's _id.
        """
        session_info = self._call_api_get_info_session(project_info[0].get('_id'))
        """
            Step 6: Delete above session for cleaning.
        """
        self._call_api_delete_session(session_info[0].get('_id'))
        """
            Step 7: Delete above project for cleaning.
        """
        self._call_api_delete_project()
        
if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )