import os
import unittest
import time 

import HtmlTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tests.df.df_base_test import DFBaseTest
from Pages.df.df_homepage import DFHomePage
from Pages.df.df_delete_project_page import DFDeleteProjectPage

from Locators.df import DFProjectLocators

class Test_DF_Delete_Project(DFBaseTest):
    def test_delete_project_successful(self):
        """
            TEST CASE: DF Project should be deleted successfully
        """
        self.df_homepage = DFHomePage(self.driver)
        self.df_delete_project_page = DFDeleteProjectPage(self.driver)
        _project_name = self.df_delete_project_page.click_delete_project_submit_button()
        self.driver.implicitly_wait(10)
        self.assertTrue(
            self.driver.find_element_by_link_text(_project_name)
        )

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )

