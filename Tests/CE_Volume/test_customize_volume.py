"""
    This test is general to all the scenarios from 11 to 13 to CUSTOMIZE volume in CE_EBS
"""

import os
import time
import unittest

import HtmlTestRunner

from Tests.CE_Volume.volume_base_test import VolumeBaseTest


class Test_Customize_Volume(VolumeBaseTest):
    """

    """
    def test_custom_volume(self):

        # Access Volume Page, Choose Volume
        self.access_volume_page()

        # Check information of chosen volume
        self.check_info_volume()

        # Check VM attached: Yes, No

        # Yes: Detach
        if (self.vm_id != "-"):


        # No:
        if (self.vm_id == "-"):
            # Attach

            # Delete


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
