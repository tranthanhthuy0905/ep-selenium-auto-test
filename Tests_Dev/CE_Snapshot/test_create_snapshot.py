"""
    Command run test:
        python3 -m unittest Tests_Dev.CE_Snapshot.test_create_snapshot -v

    Test big flow Create Snapshot
"""

from Configs.TestData.CESnapshotTestData import CESnapshotTestData
from Configs.TestData.CEVolumeTestData import CEVolumeTestData
from Locators.CE import CECreateVolumePageLocators
from Tests_Dev.CE_Snapshot.snapshot_base_test import SnapshotBaseTest


class Test_create_snapshot(SnapshotBaseTest):

    def test_create_snapshot_volume_noVM(self):
        '''
            TEST CASE: Create a snapshot from a volume not attached with any instance
        '''
        # *** Choose one volume not attached with any instance ***
        self.choose_volume(CECreateVolumePageLocators.CUSTOM_DISK,
                           False, CEVolumeTestData.SIZE2, False)
        # *** Create the volume snapshot ***
        # Flow of work:
        # - Click on Create Snapshot button
        # - Input snapshot name
        # - Should FAIL to find the name of volume not attached with any instance
        self.create_snapshot(CESnapshotTestData.SNAPSHOT_NAME, self.volume_name, False)

    def test_create_snapshot_volume_Running_VM(self):
        '''
            TEST CASE: Create a snapshot from a volume attached with a Running instance
        '''
        # *** Choose one volume attached with a Running instance ***
        # Flow of work:
        # - Create an instance
        # - Create a volume
        # - Attach volume to above instance
        self.choose_volume(CECreateVolumePageLocators.CUSTOM_DISK,
                           False, CEVolumeTestData.SIZE2, True)

        # *** Create the volume snapshot ***
        # Flow of work:
        # - Click on Create Snapshot button
        # - Input snapshot name + Select Running instance
        # - Should FAIL to find the name of volume attached with a Running instance
        self.create_snapshot(CESnapshotTestData.SNAPSHOT_NAME, self.volume_name, False)

    def test_create_snapshot_volume_Stopped_VM(self):
        '''
            TEST CASE: Create a snapshot from a volume attached with a Stopped instance
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
