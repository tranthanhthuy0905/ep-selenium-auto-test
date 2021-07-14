from Configs.TestData.RDSTestData import RDSTestData
from Tests_Dev.RDS.rds_base_test import RDSBaseTest


class TestChangeSizeCluster(RDSBaseTest):

    def test_scale_up_cluster_template_config(self):
        self.create_db_cases("Abc123456", "Abc123456", "Dev/Test", RDSTestData.NO_OF_REPLICA1)

