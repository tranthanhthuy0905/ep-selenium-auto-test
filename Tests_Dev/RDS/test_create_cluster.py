import os
import unittest

import HtmlTestRunner

from Configs.TestData.RDSTestData import RDSTestData
from Tests_Dev.RDS.rds_base_test import RDSBaseTest


class TestCreateCluster(RDSBaseTest):
    def create_cluster_template_configs_correct_pw(self):
        self.create_db_cases("Abc123456", "Abc123456", "Dev/Test", RDSTestData.NO_OF_REPLICA1)

    def create_cluster_custom_configs_correct_pw(self):
        self.create_db_cases("Abc123456", "Abc123456", "Custom", RDSTestData.NO_OF_REPLICA1)

    def create_cluster_template_configs_unmatched_pw(self):
        self.create_db_cases("Abc123456", "Abcd123456", "Dev/Test", RDSTestData.NO_OF_REPLICA1)

    def create_cluster_template_configs_missing_pw(self):
        self.create_db_cases("", "", "Dev/Test", RDSTestData.NO_OF_REPLICA1)

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
