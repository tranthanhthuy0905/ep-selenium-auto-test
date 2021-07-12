import os
import unittest
import time

import HtmlTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tests.device_farm.devicefarm_base_test import DEVICE_FARM_BaseTest

from Pages.device_farm.devicefarm_homepage import DEVICE_FARM_HomePage
from Pages.device_farm.devicefarm_delete_project_page import DEVICE_FARM_DeleteProjectPage

from Locators.device_farm import DEVICE_FARM_ProjectLocators
from Configs.TestData.DeviceFarmTestData import DEVICE_FARM_TestData

class Test_DEVICEFARM_Delete_Running_Project(DEVICE_FARM_BaseTest):
    def test_delete_project_fail(self):
        """
            TEST CASE: DF Project should not be deleted successfully
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
        time.sleep(2)
        self.df_homepage = DEVICE_FARM_HomePage(self.driver)
        self.df_delete_project_page = DEVICE_FARM_DeleteProjectPage(self.driver)
        _project_name = self.df_delete_project_page.click_delete_project_submit_button()
        time.sleep(2)
        print('PROJECT NAME', _project_name)
        self.driver.implicitly_wait(10)
        self.assertIn("Failed", self.driver.page_source, msg='CREATE PROJECT IS NOT SUCCESSFULLY')
        """
            Step 4: Get info above session.
        """
        session_info = self._call_api_get_info_session(project_info[0].get('_id'))
        """
            Step 5: Stop above session
        """
        self._call_api_stop_session(self.project_text.LG_G5_SE, session_info[0].get('_id'))
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
