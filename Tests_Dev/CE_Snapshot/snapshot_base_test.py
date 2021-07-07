import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Locators.CE import CESnapshotLocators
from Pages.CE.snapshot_page import CESnapshotPage
from Tests_Dev.CE_Volume.volume_base_test import VolumeBaseTest


class SnapshotBaseTest(VolumeBaseTest):

    def create_snapshot(self, snapshot_name, volume_name, attach_VM):
        self.ce_homepage.access_snapshot_page()
        self.snapshot_page = CESnapshotPage(self.driver)
        self.snapshot_page.click_create_snapshot_btn()
        # Input the instance name
        self.snapshot_page.fill_form(snapshot_name, CESnapshotLocators.SNAPSHOT_NAME_FORM)
        time.sleep(5)
        if (attach_VM):
            # Select a volume attached with an instance
            self.snapshot_page.find_element(*CESnapshotLocators.SELECT_VOLUME) \
                .send_keys(volume_name)
            self.snapshot_page.find_element(*CESnapshotLocators.SELECT_VOLUME) \
                .send_keys(Keys.ENTER)
            # Click on Create Snapshot button to confirm the creation
            self.snapshot_page.click_button(CESnapshotLocators.CREATE_SNAPSHOT_CONFIRM)
            if (self.instance_state == "Running"):
                # If user wants to create snapshot from a volume attached with a Running instance,
                # it should FAIL
                self.assertFalse(
                    self.driver.find_element_by_xpath("//td[contains(.,'" + snapshot_name + "')]/parent::*"),
                    "Should fail to create volume snapshot from a volume attached with a Running instance"
                )
            else:
                # If user wants to create snapshot from a volume attached with a Stopped instance,
                # it should SUCCEED
                self.assertTrue(
                    self.driver.find_element_by_xpath("//td[contains(.,'" + snapshot_name + "')]/parent::*"),
                    "Should succeed to create volume snapshot from a volume attached with a Stopped instance"
                )
        else:
            # The chosen volume not attached with any instance should not be suggested in the volume list of Creating Snapshot
            self.snapshot_page.click_button(CESnapshotLocators.SELECT_VOLUME)
            self.assertFalse(
                self.snapshot_page.find_element((By.XPATH, '//div[text()="' + volume_name + '"]'),
                                                "Should fail to snapshot a volume not attached with any instance")
            )

    def delete_snapshot(self, snapshot_name):
        # Click on "Actions" button
        # Choose Delete snapshot option
        # Click Delete button to confirm the deletion
        self.click_button(CESnapshotLocators.ACTIONS_BTN)\
            .click_button(CESnapshotLocators.DELETE_SNAPSHOT)\
            .click_button(CESnapshotLocators.DELETE_CONFIRM)
        time.sleep(2)
        # Check if the snapshot name is eliminated from the snapshot list successfully or not
        self.assertFalse(
            self.driver.find_element_by_xpath("//td[contains(.,'" + snapshot_name + "')]/parent::*"),
            "Should succeed to create volume snapshot from a volume attached with a Stopped instance"
        )

    def auto_delete_snapshot(self, snapshot_name):
        snapshot_row = self.driver.find_element(
            *CESnapshotLocators.PARRENT_BY_SNAPSHOT_NAME(_snapshot_name=snapshot_name))
        self.snapshot_id = snapshot_row.get_attribute("data-row-key")
        self.delete_CE_volume_by_id(self.snapshot_id)
