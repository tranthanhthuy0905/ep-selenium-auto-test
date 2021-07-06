from Configs.TestData.CESnapshotTestData import CESnapshotTestData
from Configs.TestData.CEVolumeTestData import CEVolumeTestData
from Locators.CE import CECreateVolumePageLocators
from Tests_Dev.CE_Snapshot.snapshot_base_test import SnapshotBaseTest


class Test_delete_snapshot(SnapshotBaseTest):

    def test_delete_snapshot(self):
        '''
            TEST CASE: Delete a snapshot (created from a volume attached with a Stopped instance)
        '''
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
        self.create_snapshot(CESnapshotTestData.SNAPSHOT_NAME, self.volume_name, False)
        # *** Delete the snapshot ***
        # Flow of work:
        # - Click on "Actions" button + Choose "Delete snapshot" option
        # - Click on "Delete" button to confirm the deletion
        # - Should SUCCEED to delete the snapshot
        self.delete_snapshot(CESnapshotTestData.SNAPSHOT_NAME)
