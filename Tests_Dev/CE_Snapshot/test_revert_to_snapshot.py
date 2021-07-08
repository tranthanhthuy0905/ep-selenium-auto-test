"""
    Command run test:
        python3 -m unittest Tests_Dev.CE_Snapshot.test_revert_to_snapshot -v

    Test big flow Delete Snapshot
"""
from Configs.TestData.CEVolumeTestData import CEVolumeTestData
from Locators.CE import CECreateVolumePageLocators
from Tests_Dev.CE_Snapshot.snapshot_base_test import SnapshotBaseTest


class Test_revert_to_snapshot(SnapshotBaseTest):

    def test_revert_to_snapshot(self):
        """
            TEST CASE: Revert to snapshot (created from a volume attached with a Stopped instance)
        """
        # *** Choose one volume attached with a Stopped instance ***
        # Flow of work:
        # - Create an instance + Stop instance
        # - Create a volume
        # - Attach volume to above instance
        self.choose_volume(CECreateVolumePageLocators.CUSTOM_DISK,
                           True, CEVolumeTestData.SIZE2, True)
        # *** Create the volume snapshot ***
        # Flow of work:
        # - Click on Create Snapshot button
        # - Input snapshot name + Select Stopped instance
        # - Should SUCCEED to find the name of volume attached with a Stopped instance
        self.create_snapshot(self.volume_name, True, True)
        # *** Revert to the snapshot ***
        # Flow of work:
        # - Click on "Actions" button + Choose "Revert to snapshot" option
        # - Click on "Revert" button to confirm
        # - Should SUCCEED to revert to the snapshot
        self.revert_to_snapshot()
        self.tearDown()
