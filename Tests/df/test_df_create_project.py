import os
import unittest
import time 

import HtmlTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tests.df.df_base_test import DFBaseTest
from Pages.df.df_homepage import DFHomePage
from Pages.df.df_create_project_page import DFCreateProjectPage

from Locators.df import DFProjectLocators

class Test_DF_Create_Project(DFBaseTest):
    def test_create_project_successful(self):
        """
            TEST CASE: DF Project should be created successfully
        """
        self.df_homepage = DFHomePage(self.driver)
        self.df_homepage.click_create_project()

        self.df_create_project_page = DFCreateProjectPage(self.driver)
        self.assertTrue(
            self.df_create_project_page.check_element_existence(DFProjectLocators.PROJECT_CREATE_TITLE)
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