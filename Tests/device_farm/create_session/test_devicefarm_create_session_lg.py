import os
import unittest
import time 

import HtmlTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tests.device_farm.devicefarm_base_test import DEVICE_FARM_BaseTest
from Pages.device_farm.devicefarm_homepage import DEVICE_FARM_HomePage
from Pages.device_farm.devicefarm_create_session_page import DEVICE_FARM_CreateSessionPage

from Locators.device_farm import DEVICE_FARM_ProjectLocators

class Test_DEVICEFARM_Create_Session_LG(DEVICE_FARM_BaseTest):
    def test_create_session_lg_successful(self):
        """
            TEST CASE: DF Session should be created successfully
        """
        self.df_homepage = DEVICE_FARM_HomePage(self.driver)
        self.df_session = DEVICE_FARM_CreateSessionPage(self.driver)
        self.df_session.click_create_session_submit_button()
        _session_name = self.df_session.click_create_session_lg()
        self.assertTrue(
            self.df_session.check_element_existence(
                DEVICE_FARM_ProjectLocators.SESSION_STOP_NOTIC
            )
        )
        self.assertTrue(
            self.driver.find_element_by_link_text(_session_name)
        )
        self.assertIn("Created session successfully", self.driver.page_source, msg="CREATE SESSION IS NOT SUCCESSFULLY")
        
        
if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )