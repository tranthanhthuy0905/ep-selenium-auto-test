import os
import logging

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#TODO
from Tests.CE.ce_base_test import CEBaseTest
from Pages.CE.security_group_page import SGHomePage, SGCreatePage
from Configs import CE_SG_API_URL, CE_SG_URL
from Configs import CE_USER_TOKEN
from Configs.TestData.CESecurityGroupTestData import CESecurityGroupTestData

class SGBaseTest(CEBaseTest):
    def create_security_group(self):
        self.sg_home_page = SGHomePage(self.driver)
        self.sg_home_page.click_create_button()
        self.sg_create_page = SGCreatePage(self.driver)
        sg_name = self.sg_create_page.fill_sg_information()
        self.sg_create_page.click_create_submit_button()
        self.driver.implicitly_wait(10)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_matches(os.path.join(CE_SG_URL, CESecurityGroupTestData.SG_ID_REGEX)))
        sg_id = self.driver.current_url.split("/")[-1]

        return sg_id, sg_name

    def delete_sg(self):
        url = CE_SG_API_URL
        try:
            params = {
                "id": self.sg_id
            }
        except:
            logging.info("No created-SG to clean.")
            return

        self._call_request_delete(url, params, CE_USER_TOKEN)

    def clear_test_instances(self):
        logging.info("Done testing. Clearing test instances.")
        self.delete_sg()
