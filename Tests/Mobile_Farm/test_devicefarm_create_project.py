import os
import unittest
import time 

import HtmlTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tests.Mobile_Farm.devicefarm_base_test import DEVICE_FARM_BaseTest
from Pages.device_farm.devicefarm_homepage import DEVICE_FARM_HomePage
from Pages.device_farm.devicefarm_create_project_page import DEVICE_FARM_CreateProjectPage

from Locators.device_farm import DEVICE_FARM_ProjectLocators

class Test_DEVICEFARM_Create_Project(DEVICE_FARM_BaseTest):
    def test_create_project_successful(self):
        """
            TEST CASE: DF Project should be created successfully
        """
        self.df_homepage = DEVICE_FARM_HomePage(self.driver)
        self.df_homepage.click_create_project()

        self.df_create_project_page = DEVICE_FARM_CreateProjectPage(self.driver)
        self.assertTrue(
            self.df_create_project_page.check_element_existence(DEVICE_FARM_ProjectLocators.PROJECT_CREATE_TITLE)
        )
        project_name = self.df_create_project_page.fill_project_create_information()
        self.service_slug = project_name

        self.df_create_project_page.click_create_project_submit_button()
        
        self.driver.implicitly_wait(10)
        self.assertTrue(
            self.driver.find_element_by_link_text(project_name)
        )

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )