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
        print("---create project-------")
        self.project_text = DEVICE_FARM_TestData()
        self._call_api_create_project(self.project_text.PROJECT_NAME)
        print("------get info project--------")
        project_info = self._call_api_get_info_project()
        print("-------create session---------")
        self._call_api_create_session(project_info[0].get('_id'), self.project_text.GALAXY_TAB_E_SERIAL)
        print("-------get info session---------")
        session_info = self._call_api_get_info_session('60e5af7c7259ac001258aac2')
        print("-------stop session----------")
        self._call_api_stop_session(self.project_text.GALAXY_TAB_E_SERIAL, session_info[0].get('_id'))
        print("-------begin delete session-------")
        self.df_homepage = DEVICE_FARM_HomePage(self.driver)
        self.df_session = DEVICE_FARM_DeleteSessionPage(self.driver)
        self.df_session.click_delete_session_submit_button()
        self.assertIn("Delete session is successful!", self.driver.page_source, msg='DELETE SESSION IS NOT SUCCESSFULLY')

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )