"""
    Command run test:
        python3 -m unittest Tests_Dev.EFS.test_delete_filesystem -v

    Test big flow of Delete a filesystem in EFS service
"""

import os
import unittest

import HtmlTestRunner

from Tests_Dev.EFS.efs_base_test import EFSBaseTest


class Test_delete_filesystem(EFSBaseTest):

    def test_delete_filesystem_no_ip(self):
        """
            TEST CASE: Delete a filesystem NOT giving access to any ip
        """
        self.delete_filesystem_cases(False, False)
        self.tearDown()

    def test_delete_filesystem_read_only_ip(self):
        """
            TEST CASE: Delete a filesystem setting Read-only access for an ip
        """
        self.delete_filesystem_cases(True, True)
        self.tearDown()

    def test_delete_filesystem_full_access_ip(self):
        """
            TEST CASE: Delete a filesystem setting Full access for an ip
        """
        self.delete_filesystem_cases(True, False)
        self.tearDown()


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
