import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Configs import RDS_API_BASE_URL, RDS_USER_TOKEN
from Locators.RDS import RDSHomePageLocators, RDSCreatePageLocators
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
        # Click Create Database button to direct to RDS Create DB page
        self.rds_homepage.click_create_database_button()
        self.rds_create_page = RDSCreatePage(self.driver)
        # Check whether directing to creating database page is correct or not
        self.assertEqual(self.driver.current_url, self.rds_create_page.base_url,
                         "Fail to reach Create Database Page in RDS service")
        self.no_of_replica = no_of_replica
        # Create database steps
        # Flow of work:
        #   - Select the config type
        #   - If "Custom" option, select Core size and No of replica
        #   - Input DB Instance Identifier, Master Pw and Confirm Pw
        #   - Click on "Create Database" button and click on "Confirm" button to complete the creation process
        self.rds_create_page.create_database(master_password, confirm_password, config_option, self.no_of_replica)
        self.cluster_name = self.rds_create_page.cluster_name

        # TEST CASE: Master pw matches with Confirm pw
        if master_password == confirm_password:
            self.rds_create_page.click_button(RDSCreatePageLocators.CREATE_DB_SUBMIT)
            # TEST CASE: Input Master Pw and matching Confirm pw
            if master_password != "":
                time.sleep(2)
                self.rds_create_page.click_button(RDSCreatePageLocators.CONFIRM_BTN)
                # Check whether creating database cluster successfully or not
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, "//td[contains(.,'" + self.cluster_name + "')]/parent::*")),
                    "Should SUCCESSFULLY update newly created database to the list with " + config_option + " config and correct password")
                self.assertTrue(
                    self.driver.find_element_by_xpath("//td[contains(.,'" + self.cluster_name + "')]/parent::*")
                )

                # Check whether run the cluster successfully or not
                self.cluster_id = self.driver.find_element_by_xpath(
                    "//td[contains(.,'" + self.cluster_name + "')]/parent::*").get_attribute("data-row-key")

                WebDriverWait(self.driver, 1000).until(EC.text_to_be_present_in_element
                                                      (RDSHomePageLocators.STATUS_BY_ID(self.cluster_id),
                                                       "Running"),
                                                      "FAIL to run the newly created cluster")
            # TEST CASE: Miss to input Master Pw and matching Confirm pw
            else:
                # Check whether creating database cluster successfully or not
                error_text = "'pg_password' is required"
                self.assertTrue(
                    self.driver.find_element_by_xpath("//div[text()='" + error_text + "']"),
                    "Should FAIL to create database with " + config_option + " config and missing password"
                )
        # TEST CASE: Master pw unmatches with Confirm pw
        else:
            # Check whether FAIL to create database cluster or not
            self.assertTrue(
                self.driver.find_element_by_xpath("//div[text()='The two passwords that you entered do not match!']"),
                "Should FAIL to create database with " + config_option + " config and unmatched password"
            )

    def change_no_of_replica_cases(self, config_option, no_of_replica, no_of_server):
        # Step 1: Create a Cluster simple flow
        self.create_db_cases("Abc123456", "Abc123456", config_option, no_of_replica)
        # Flow of test:
        #   - Select the newly created cluster and click on "Create read replica" button
        #   - Input the number of replica and click on "OK" button
        self.rds_homepage\
            .select_cluster(self.cluster_id)\
            .click_button(RDSHomePageLocators.CREATE_READ_REPLICA)\
            .fill_form(no_of_server, RDSHomePageLocators.NO_OF_SERVERS)\
            .click_button(RDSHomePageLocators.OK_BTN)

        # Wait for the change in the number of replica being updated
        if no_of_replica <= no_of_server:
            WebDriverWait(self.driver, 500).until(EC.text_to_be_present_in_element
                                                  (RDSHomePageLocators.STATUS_BY_ID(self.cluster_id),
                                                   "Running"),
                                                  "FAIL to scale up the number of replica")
            # Check if the number of replica is upsized or not
            self.assertTrue(
                self.rds_homepage.find_element(*RDSHomePageLocators.NO_OF_CLUSTER).text == no_of_server,
                "FAIL to scale up the number of replica"
            )
        else:
            WebDriverWait(self.driver, 500).until(EC.text_to_be_present_in_element
                                                  (RDSHomePageLocators.STATUS_BY_ID(self.cluster_id),
                                                   "Running"),
                                                  "FAIL to scale down the number of replica")
            # Check if the number of replica is downsized or not
            self.assertTrue(
                self.rds_homepage.find_element(RDSHomePageLocators.NO_OF_CLUSTER).text == no_of_server,
                "FAIL to scale down the number of replica"
            )

    def delete_cluster_cases(self, config_option, no_of_replica):
        # Step 1: Create a Cluster simple flow
        self.create_db_cases("Abc123456", "Abc123456", config_option, no_of_replica)
        # Flow of test:
        #   - Select the newly created cluster
        #   - Click on "Actions" button, select the delete option and click on "Delete" button to confirm
        self.rds_homepage\
            .select_cluster(self.cluster_id)\
            .delete_cluster()
        # Check if the cluster is successfully eliminated from the list or not
        WebDriverWait(self.driver, 500).until(EC.invisibility_of_element_located
                                              ((By.XPATH, "//td[contains(.,'" + self.cluster_name + "')]/parent::*")),
                                              "FAIL to delete the cluster")
