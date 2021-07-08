from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from Locators.CE import CESnapshotLocators
from Pages.CE.create_snapshot_page import CECreateSnapshotPage
from Pages.CE.snapshot_page import CESnapshotPage
from Tests_Dev.CE_Volume.volume_base_test import VolumeBaseTest


class SnapshotBaseTest(VolumeBaseTest):

    def create_snapshot(self, volume_name, stop_vm, attach_vm):
        self.ce_homepage.access_snapshot_page()
        self.snapshot_page = CESnapshotPage(self.driver)
        self.assertEqual(
            self.driver.current_url, self.snapshot_page.base_url
        )
        self.snapshot_page.click_create_snapshot_btn()
        self.create_snapshot_page = CECreateSnapshotPage(self.driver)
        self.assertEqual(
            self.driver.current_url, self.create_snapshot_page.base_url
        )

        self.create_snapshot_page \
            .input_snapshot_name() \
            .click_button(CESnapshotLocators.SELECT_VOLUME)

        if attach_vm:
            # self.create_snapshot_page.input_volume_choice(volume_name)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable
                                                 ((By.XPATH, "//div[text()='" + volume_name + "']")),
                                                 "Cannot choose the volume")

            self.create_snapshot_page \
                .click_button((By.XPATH, "//div[text()='" + volume_name + "']")) \
                .click_button(CESnapshotLocators.CREATE_SNAPSHOT_CONFIRM)

            self.snapshot_name = self.create_snapshot_page.snapshot_name
            time.sleep(3)
            if stop_vm:
                self.assertTrue(
                    self.snapshot_page.check_element_existence(
                        (By.XPATH, "//td[contains(.,'" + self.snapshot_name + "')]")),
                    "Should SUCCEED to create a snapshot from a volume attached with a Stopped instance by updating "
                    "that snapshot in the list "
                )
                self.snapshot_id = self.driver.find_element_by_xpath(
                    "//td[contains(.,'" + self.snapshot_name + "')]/parent::*").get_attribute("data-row-key")

                time.sleep(5)
                self.snapshot_page.click_button(
                    (By.XPATH,
                     '//span[././input/@type="radio" and ancestor::tr/@data-row-key="' + self.snapshot_id + '"]'))
            else:
                self.assertEqual(
                    self.driver.current_url, self.create_snapshot_page.base_url,
                    "Should FAIL to create a snapshot from a volume attached with a Running instance"
                )
        else:
            # TODO: Check that user should not be able to find the volume not attached with any instance
            # The chosen volume not attached with any instance should not be suggested in the volume list of Creating Snapshot
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH,
                                                                                     '//div[text()="' + volume_name + '"]')),
                                                 "Should FAIL to create a snapshot from a volume not attached with any instance")

    def delete_snapshot(self, snapshot_name):
        # Click on "Actions" button
        # Choose Delete snapshot option
        # Click Delete button to confirm the deletion
        time.sleep(2)
        self.snapshot_page \
            .click_button(CESnapshotLocators.ACTIONS_BTN) \
            .click_button(CESnapshotLocators.DELETE_SNAPSHOT)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(CESnapshotLocators.DELETE_CONFIRM))
        self.snapshot_page.click_button(CESnapshotLocators.DELETE_CONFIRM)
        time.sleep(2)
        # TODO: Check if the snapshot is eliminated from the list
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH,
                                    "//td[contains(.,'" + snapshot_name + "')]/parent::*")),
                        "Should SUCCEED to delete the volume snapshot")

    def revert_to_snapshot(self):
        self.snapshot_page \
            .click_button(CESnapshotLocators.ACTIONS_BTN) \
            .click_button(CESnapshotLocators.REVERT_TO_SNAPSHOT) \
            .click_button(CESnapshotLocators.REVERT_CONFIRM)
        # TODO: Check the condition of reverting successfully
