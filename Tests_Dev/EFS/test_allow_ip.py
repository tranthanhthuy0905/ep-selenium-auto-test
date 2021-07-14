"""
    Command run test:
        python3 -m unittest Tests_Dev.EFS.test_allow_ip -v

    Test big flow of Allow IP (setting access point to an instance) in EFS service
"""

import os
import unittest

import HtmlTestRunner

from Tests_Dev.EFS.efs_base_test import EFSBaseTest


class Test_allow_ip(EFSBaseTest):

    def test_allow_ip_full_access(self):
        """
            TEST CASE: Allow an ip to access the filesystem (full access)
        """
        self.allow_ip_cases(False)

    def test_allow_ip_read_only(self):
        """
            TEST CASE: Allow an ip to access the filesystem (Read-only)
        """
        self.allow_ip_cases(True)


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
