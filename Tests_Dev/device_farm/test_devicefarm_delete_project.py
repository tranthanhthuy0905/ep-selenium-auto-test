import os
import unittest
import time

import HtmlTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tests_Dev.device_farm.devicefarm_base_test import DEVICE_FARM_BaseTest

from Pages.device_farm.devicefarm_homepage import DEVICE_FARM_HomePage
from Pages.device_farm.devicefarm_delete_project_page import DEVICE_FARM_DeleteProjectPage

from Locators.device_farm import DEVICE_FARM_ProjectLocators
from Configs.TestData.DeviceFarmTestData import DEVICE_FARM_TestData

class Test_DEVICEFARM_Delete_Project(DEVICE_FARM_BaseTest):
    def test_delete_project_successful(self):
        """
            TEST CASE: DF Project should be deleted successfully
        """
        self.project_text = DEVICE_FARM_TestData()
        self._call_api_create_project(self.project_text.PROJECT_NAME)
        self.df_homepage = DEVICE_FARM_HomePage(self.driver)
        self.df_delete_project_page = DEVICE_FARM_DeleteProjectPage(self.driver)
        _project_name = self.df_delete_project_page.click_delete_project_submit_button()
        print('PROJECT NAME', _project_name)
        self.driver.implicitly_wait(10)
        self.assertTrue(
            self.driver.find_element_by_link_text(_project_name)
        )

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )

