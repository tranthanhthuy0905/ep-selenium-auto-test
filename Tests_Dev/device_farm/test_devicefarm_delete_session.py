import os
import unittest
import time 

import HtmlTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tests_Dev.device_farm.devicefarm_base_test import DEVICE_FARM_BaseTest
from Pages.device_farm.devicefarm_homepage import DEVICE_FARM_HomePage
from Pages.device_farm.devicefarm_delete_session_page import DEVICE_FARM_DeleteSessionPage

from Locators.device_farm import DEVICE_FARM_ProjectLocators
from Configs.TestData.DeviceFarmTestData import DEVICE_FARM_TestData

class Test_DEVICEFARM_Delete_Session(DEVICE_FARM_BaseTest):
    def test_delete_session_successful(self):
        """
            TEST CASE: DF Session should be deleted successfully
        """
        """
            Step 1: Create a new project.
        """
        self.project_text = DEVICE_FARM_TestData()
        self._call_api_create_project(self.project_text.PROJECT_NAME)
        """
            Step 2: Get info above project to get project's _id.
        """
        project_info = self._call_api_get_info_project()
        """
            Step 3: Create a new LG session
        """
        self._call_api_create_session(project_info[0].get('_id'), self.project_text.LG_G5_SE)
        """
            Step 4: Get info session to get session's _id
        """
        session_info = self._call_api_get_info_session(project_info[0].get('_id'))
        """
            Step 5: Stop above session.
        """
        self._call_api_stop_session(self.project_text.LG_G5_SE, session_info[0].get('_id'))
        #  begin TEST-CASE
        """
            Step 6: TEST-CASE Delete session.
        """
        self.df_homepage = DEVICE_FARM_HomePage(self.driver)
        self.df_session = DEVICE_FARM_DeleteSessionPage(self.driver)
        self.df_session.click_delete_session_submit_button()
        self.assertIn("Delete session is successful!", self.driver.page_source, msg='DELETE SESSION IS NOT SUCCESSFULLY')
        # end TEST-CASE
        """
            Step 7: Delete above project for cleaning.
        """ 
        self._call_api_delete_project()

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )