import os
import unittest
import time 

import HtmlTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tests.device_farm.devicefarm_base_test import DEVICE_FARM_BaseTest
from Pages.device_farm.devicefarm_homepage import DEVICE_FARM_HomePage
from Pages.device_farm.devicefarm_create_session_page import DEVICE_FARM_CreateSessionPage
from Configs.TestData.DeviceFarmTestData import DEVICE_FARM_TestData

from Locators.device_farm import DEVICE_FARM_ProjectLocators

class Test_DEVICEFARM_Create_Session_Galaxy(DEVICE_FARM_BaseTest):
    def test_create_session_galaxy_successful(self):
        """
            TEST CASE: DF Session should be created successfully
        """
        """
            Step 1: Create a new project
        """
        self.project_text = DEVICE_FARM_TestData()
        self._call_api_create_project(self.project_text.PROJECT_NAME)
        """
            Step 2: Get info a project to get project's _id
        """
        project_info = self._call_api_get_info_project()
        # begin TEST-CASE
        """
            Step 3: TEST-CASE: Create a new session in above project.
        """
        self.df_homepage = DEVICE_FARM_HomePage(self.driver)
        self.df_session = DEVICE_FARM_CreateSessionPage(self.driver)
        self.df_session.click_create_session_submit_button()
        _session_name = self.df_session.click_create_session_galaxy()
        self.assertTrue(
            self.df_session.check_element_existence(
                DEVICE_FARM_ProjectLocators.SESSION_STOP_NOTIC
            )
        )
        self.assertTrue(
            self.driver.find_element_by_link_text(_session_name)
        )
        time.sleep(2)
        self.assertIn("Created session successfully", self.driver.page_source, msg="CREATE SESSION IS NOT SUCCESSFULLY")
        # end TEST-CASE
        """
            Step 4: Get info above session.
        """
        session_info = self._call_api_get_info_session(project_info[0].get('_id'))
        """
            Step 5: Stop above session
        """
        self._call_api_stop_session(self.project_text.GALAXY_TAB_E_SERIAL, session_info[0].get('_id'))
        """
            Step 6: Get info session to get session's _id
        """
        session_info = self._call_api_get_info_session(project_info[0].get('_id'))
        """
            Step 7: Delete above session for cleaning.
        """
        self._call_api_delete_session(session_info[0].get('_id'))
        """
            Step 8: Delete above project for cleaning.
        """
        self._call_api_delete_project()
        
        
if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )