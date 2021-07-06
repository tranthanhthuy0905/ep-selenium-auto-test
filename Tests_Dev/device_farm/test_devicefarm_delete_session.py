import os
import unittest
import time 

import HtmlTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tests.device_farm.devicefarm_base_test import DEVICE_FARM_BaseTest
from Pages.device_farm.devicefarm_homepage import DEVICE_FARM_HomePage
from Pages.device_farm.devicefarm_delete_session_page import DEVICE_FARM_DeleteSessionPage

from Locators.device_farm import DEVICE_FARM_ProjectLocators

class Test_DEVICEFARM_Delete_Session(DEVICE_FARM_BaseTest):
    def test_delete_session_successful(self):
        """
            TEST CASE: DF Session should be deleted successfully
        """
        self.df_homepage = DEVICE_FARM_HomePage(self.driver)
        self.df_session = DEVICE_FARM_DeleteSessionPage(self.driver)
        self.df_session.click_delete_session_submit_button()
        self.assertIn("Delete session is successful!", self.driver.page_source, msg='FAIL SM')

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )