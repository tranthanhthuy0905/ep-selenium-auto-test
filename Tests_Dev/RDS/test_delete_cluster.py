"""
    Command run test:
        python3 -m unittest Tests_Dev.RDS.test_delete_cluster -v

    Test big flow of Delete Cluster in RDS service
"""

import os
import unittest

import HtmlTestRunner

from Configs.TestData.RDSTestData import RDSTestData
from Tests_Dev.RDS.rds_base_test import RDSBaseTest


class TestDeleteCluster(RDSBaseTest):

    def test_delete_cluster_template_config(self):
        """
            TEST CASE: Delete a cluster choosing Dev/Test config
        """
        self.delete_cluster_cases("Dev/Test", RDSTestData.NO_OF_REPLICA1)

    def test_delete_cluster_custom_config(self):
        """
            TEST CASE: Delete a cluster choosing Custom config
        """
        self.delete_cluster_cases("Custom", RDSTestData.NO_OF_REPLICA1)

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
