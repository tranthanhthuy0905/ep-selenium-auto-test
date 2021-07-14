from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Configs import RDS_API_BASE_URL, RDS_USER_TOKEN
from Locators.RDS import RDSHomePageLocators
from Pages.RDS.rds_create_page import RDSCreatePage
from Pages.RDS.rds_homepage import RDSHomePage
from Tests.base_test import BaseTest


class RDSBaseTest(BaseTest):

    def clear_database(self):
        """
        Clear all clusters after testing
        """
        if hasattr(self, 'cluster_id'):
            self.delete_cluster_by_id(self.cluster_id)

    def delete_cluster_by_id(self, cluster_id):
        try:
            url = RDS_API_BASE_URL
            params = {
                "id": cluster_id,
            }
            self._call_request_delete(url, params, RDS_USER_TOKEN)
        except Exception as e:
            print("Can't delete file system ", str(e))

    def create_db_cases(self, master_password, confirm_password, config_option, no_of_replica):
        # Direct to homepage of RDS service
        self.rds_homepage = RDSHomePage(self.driver)
        # Click File Systems button to direct to EFS Filesystem page
        self.rds_homepage.click_create_database_button()
        self.rds_create_page = RDSCreatePage(self.driver)
        # Check whether directing to creating database page is correct or not
        self.assertEqual(self.driver.current_url, self.rds_create_page.base_url,
                         "Fail to reach Create Database Page in RDS service")
        self.no_of_replica = no_of_replica
        self.rds_create_page.create_database(master_password, confirm_password, config_option, self.no_of_replica)
        self.cluster_name = self.rds_create_page.cluster_name
        if master_password == confirm_password:
            if master_password != "":
                # Check whether creating database cluster successfully or not
                self.assertTrue(
                    self.driver.find_element_by_xpath("//td[contains(.,'" + self.cluster_name + "')]/parent::*"),
                    "Should SUCCESSFULLY update newly created database to the list with " + config_option + " config and correct password"
                )
                WebDriverWait(self.driver, 1000).until(
                    EC.visibility_of_element_located(RDSHomePageLocators.PROGRESS_STATUS),
                    "Fail to run the database")

                self.cluster_id = self.driver.find_element_by_xpath(
                    "//td[contains(.,'" + self.cluster_name + "')]/parent::*").get_attribute("data-row-key")
            else:
                # Check whether creating database cluster successfully or not
                error_text = "'pg_password' is required"
                self.assertTrue(
                    self.driver.find_element_by_xpath("//div[text()='" + error_text + "']"),
                    "Should FAIL to create database with " + config_option + " config and missing password"
                )
        else:
            # Check whether FAIL to create database cluster or not
            self.assertTrue(
                self.driver.find_element_by_xpath("//div[text()='The two passwords that you entered do not match!']"),
                "Should FAIL to create database with " + config_option + " config and unmatched password"
            )

    def change_no_of_replica(self):
        pass
