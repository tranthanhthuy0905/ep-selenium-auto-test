"""
    Command run test:
        python3 -m unittest Tests_Dev.RDS.test_create_cluster -v

    Test big flow of Create Cluster in RDS service
"""

import os
import unittest

import HtmlTestRunner

from Configs.TestData.RDSTestData import RDSTestData
from Tests_Dev.RDS.rds_base_test import RDSBaseTest


class TestCreateCluster(RDSBaseTest):
    def test_create_cluster_template_configs_correct_pw(self):
        """
            TEST CASE: Create a cluster choosing Dev/Test config, entering valid passwords
        """
        self.create_db_cases("Abc123456", "Abc123456", "Dev/Test", 1)

    def test_create_cluster_custom_configs_correct_pw(self):
        """
            TEST CASE: Create a cluster choosing Custom config, entering valid passwords
        """
        self.create_db_cases("Abc123456", "Abc123456", "Custom", RDSTestData.NO_OF_REPLICA1)

    def test_create_cluster_template_configs_unmatched_pw(self):
        """
            TEST CASE: Create a cluster choosing Dev/Test config, entering invalid passwords
        """
        self.create_db_cases("Abc123456", "Abcd123456", "Dev/Test", 1)

    def test_create_cluster_template_configs_missing_pw(self):
        """
            TEST CASE: Create a cluster choosing Dev/Test config, NOT entering passwords
        """
        self.create_db_cases("", "", "Dev/Test", 1)

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
