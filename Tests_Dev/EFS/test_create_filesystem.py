"""
    Command run test:
        python3 -m unittest Tests_Dev.EFS.test_create_filesystem -v

    Test big flow of Create a filesystem in EFS service
"""

import os
import unittest

import HtmlTestRunner

from Tests_Dev.EFS.efs_base_test import EFSBaseTest


class Test_create_filesystem(EFSBaseTest):

    def test_create_filesystem(self):
        """
            TEST CASE: Create a filesystem simple flow
        """
        self.create_filesystem_cases()


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
