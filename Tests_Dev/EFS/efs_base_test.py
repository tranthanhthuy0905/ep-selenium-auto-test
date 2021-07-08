import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Configs.TestData.EFSTestData import EFSTestData
from Locators.EFS import EFSFileSystemLocators
from Pages.EFS.efs_filesystem_page import EFSFileSystemPage
from Pages.EFS.efs_homepage import EFSHomePage
from Tests_Dev.CE_Volume.volume_base_test import VolumeBaseTest


class EFSBaseTest(VolumeBaseTest):
    def create_filesystem_cases(self):
        self.efs_homepage = EFSHomePage(self.driver)
        self.efs_homepage.click_file_systems_button()
        self.efs_filesystem_page = EFSFileSystemPage(self.driver)
        # Check whether directing to file system page is correct or not
        self.assertEqual(self.driver.current_url, self.efs_filesystem_page.base_url)
        self.assertTrue(
            self.efs_filesystem_page.check_element_existence(EFSFileSystemLocators.CREATE_FILE_SYSTEM_BTN)
        )
        self.file_name = EFSTestData.FILESYSTEM_NAME
        self.efs_filesystem_page.create_file_system(self.file_name)
        # Check whether creating successfully or not
        self.assertTrue(
            self.driver.find_element_by_xpath("//td[contains(.,'" + self.file_name + "')]/parent::*"),
            "Should successfully update newly created file system to the list"
        )
        self.file_id = self.driver.find_element_by_xpath(
            "//td[contains(.,'" + self.file_name + "')]/parent::*").get_attribute("data-row-key")
        self.efs_filesystem_page.select_file_system(self.file_id)

    def allow_ip_cases(self, read_only):
        self.launch_instance_01_default_pw()
        self.create_filesystem_cases()
        self.efs_filesystem_page.allow_ip(self.instance_ip, self.file_id, read_only)
        time.sleep(2)
        self.efs_filesystem_page \
            .select_file_system(self.file_id) \
            .click_button(EFSFileSystemLocators.ALLOW_IP_BTN)
        # Check if allowing ip is successful or not
        self.assertTrue(
            self.driver.find_element((By.XPATH, '//input[@value="' + self.instance_ip + '"]'))
        )
        checkbox = self.efs_filesystem_page.find_element(EFSFileSystemLocators.READ_ONLY_CHECKBOX)
        if read_only:
            self.assertTrue(
                checkbox.is_selected() == True,
                "FAIL to set Read-only mode for the allowed ip"
            )
        else:
            self.assertFalse(
                checkbox.is_selected() == True,
                "FAIL to NOT set Read-only mode for the allowed ip"
            )

    def delete_filesystem_cases(self, allow_ip, read_only):
        self.create_filesystem_cases()
        if allow_ip:
            self.allow_ip_cases(read_only)
            self.efs_filesystem_page.delete_filesystem(self.file_id)
            # Check whether delete successfully or not
            if read_only:
                WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH,
                                                                                     "//td[contains(.,'" + self.file_name + "')]/parent::*")),
                                                 "Should SUCCEED to delete the filesystem attached to a Read-only ip")
            else:
                WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH,
                                                                                         "//td[contains(.,'" + self.file_name + "')]/parent::*")),
                                                     "Should SUCCEED to delete the filesystem attached to a full-access ip")

        else:
            self.efs_filesystem_page.delete_filesystem(self.file_id)
            # Check whether delete successfully or not
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH,
                                                                                     "//td[contains(.,'" + self.file_name + "')]/parent::*")),
                                                 "Should SUCCEED to delete the filesystem  NOT attached to any ip")
