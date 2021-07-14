"""
    Command run test:
        python3 -m unittest Tests_Dev.RDS.test_change_no_of_replica -v

    Test big flow of Change the number of Replica in RDS service
"""

import os
import unittest

import HtmlTestRunner

from Configs.TestData.RDSTestData import RDSTestData
from Tests_Dev.RDS.rds_base_test import RDSBaseTest


class TestChangeNoReplica(RDSBaseTest):

    def test_scale_up_cluster_template_config(self):
        """
            TEST CASE: Scale UP the number of replica of a cluster choosing Dev/Test config
        """
        self.change_no_of_replica_cases("Dev/Test", RDSTestData.NO_OF_REPLICA1, RDSTestData.NO_OF_REPLICA2)

    def test_scale_down_cluster_template_config(self):
        """
            TEST CASE: Scale DOWN the number of replica of a cluster choosing Dev/Test config
        """
        self.change_no_of_replica_cases("Dev/Test", RDSTestData.NO_OF_REPLICA2, RDSTestData.NO_OF_REPLICA1)

    def test_scale_up_cluster_custom_config(self):
        """
            TEST CASE: Scale UP the number of replica of a cluster choosing Custom config
        """
        self.change_no_of_replica_cases("Custom", RDSTestData.NO_OF_REPLICA1, RDSTestData.NO_OF_REPLICA2)

    def test_scale_down_cluster_custom_config(self):
        """
            TEST CASE: Scale DOWN the number of replica of a cluster choosing Custom config
        """
        self.change_no_of_replica_cases("Custom", RDSTestData.NO_OF_REPLICA2, RDSTestData.NO_OF_REPLICA1)

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
