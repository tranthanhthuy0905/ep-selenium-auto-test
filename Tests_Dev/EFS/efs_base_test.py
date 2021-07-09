import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Configs import EFS_FILESYSTEM_API_CLIENT_URL, EFS_USER_TOKEN
from Configs.TestData.EFSTestData import EFSTestData
from Locators.EFS import EFSFileSystemLocators
from Pages.EFS.efs_filesystem_page import EFSFileSystemPage
from Pages.EFS.efs_homepage import EFSHomePage
from Tests_Dev.CE_Volume.volume_base_test import VolumeBaseTest


class EFSBaseTest(VolumeBaseTest):

    def clear_filesystem(self):
        """
        Clear all file systems after testing
        """
        if hasattr(self, 'file_id'):
            self.delete_filesystem_by_id(self.file_id)

    def delete_filesystem_by_id(self, file_id):
        try:
            url = EFS_FILESYSTEM_API_CLIENT_URL
            params = {
                "id": file_id,
            }
            self._call_request_delete(url, params, EFS_USER_TOKEN)
        except Exception as e:
            print("Can't delete file system ", str(e))

    def create_filesystem_cases(self):
        """
        General method to create a file system simple flow
        """
        # Direct to homepage of EFS service
        self.efs_homepage = EFSHomePage(self.driver)
        # Click File Systems button to direct to EFS Filesystem page
        self.efs_homepage.click_file_systems_button()
        self.efs_filesystem_page = EFSFileSystemPage(self.driver)
        # Check whether directing to file system page is correct or not
        self.assertEqual(self.driver.current_url, 'https://efs.engineering.vng.vn/' + self.efs_filesystem_page.base_url)
        self.assertTrue(
            self.efs_filesystem_page.check_element_existence(EFSFileSystemLocators.CREATE_FILE_SYSTEM_BTN)
        )
        self.file_name = EFSTestData.FILESYSTEM_NAME
        # Create a file system simple flow
        #   Flow of work:
        #       - Click on "Create file system" button
        #       - Enter volume name and click on "OK" button
        self.efs_filesystem_page.create_file_system(self.file_name)
        # Check whether creating file system successfully or not
        self.assertTrue(
            self.driver.find_element_by_xpath("//td[contains(.,'" + self.file_name + "')]/parent::*"),
            "Should successfully update newly created file system to the list"
        )
        self.file_id = self.driver.find_element_by_xpath(
            "//td[contains(.,'" + self.file_name + "')]/parent::*").get_attribute("data-row-key")
        self.efs_filesystem_page.select_file_system(self.file_id)

    def allow_ip_cases(self, read_only):
        # Create a Running instance simple flow
        self.launch_instance_01_default_pw()
        # Create a volume from EFS service
        self.create_filesystem_cases()
        # Set access for the instance above
        #   Flow of work:
        #       - Click on "Allow ip" button
        #       - Click on "Add field" button and enter the ip of above instance
        #       - If wanting to set Read-only access, check the Read-only Checkbox
        self.efs_filesystem_page.allow_ip(self.instance_ip, self.file_id, read_only)

        # Test Checking: Due to only being able to check UI, flow of check is:
        #   - Click on "Actions" button again and check whether the ip is included
        #   in the pop-up "Allow IP to access point" box
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(EFSFileSystemLocators.ALLOW_IP_BTN))
        self.efs_filesystem_page.click_button(EFSFileSystemLocators.ALLOW_IP_BTN)
        checkbox = self.efs_filesystem_page.find_element(*EFSFileSystemLocators.READ_ONLY_CHECKBOX)
        # Scenario 3: Set Read-only access
        if read_only:
            # Check if allowing ip is successful or not
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, '//input[@value="' + self.instance_ip + '"]')),
                                                 "Fail to allow ip with Read-only access")
            # Check if the Read-only Checkbox is checked
            self.assertTrue(
                checkbox.is_selected() == True,
                "FAIL to set Read-only mode for the allowed ip"
            )
        # Scenario 2: Set Full access
        else:
            # Check if allowing ip is successful or not
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, '//input[@value="' + self.instance_ip + '"]')),
                "Fail to allow ip with full access")
            # Check if the Read-only Checkbox is NOT checked
            self.assertFalse(
                checkbox.is_selected() == True,
                "FAIL to NOT set Read-only mode for the allowed ip"
            )
        # Close the pop-up "Allow IP to access point" box
        self.efs_filesystem_page.click_button(EFSFileSystemLocators.CLOSE_BTN)

    def delete_filesystem_cases(self, allow_ip, read_only):
        # Scenario 5 + 6: Delete a volume allowing ip to access
        if allow_ip:
            # Create volume and allow ip to access
            self.allow_ip_cases(read_only)
            time.sleep(3)
            # Delete the volume
            #   Flow of work:
            #       - Click on "Actions" button
            #       - Select "Delete" option and Click on "Delete" button to confirm
            self.efs_filesystem_page.delete_filesystem()
            # Check whether deleting successfully or not

            # Scenario 5: Delete a volume storage with Read-only ip
            if read_only:
                WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH,
                                                                                         "//td[contains(.,'" + self.file_name + "')]/parent::*")),
                                                     "Should SUCCEED to delete the filesystem attached to a Read-only ip")
            # Scenario 6: Delete a volume storage with full-access ip
            else:
                WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH,
                                                                                         "//td[contains(.,'" + self.file_name + "')]/parent::*")),
                                                     "Should SUCCEED to delete the filesystem attached to a full-access ip")

        # Scenario 4: Delete a volume storage no ip
        else:
            # Create a volume simple flow
            self.create_filesystem_cases()
            time.sleep(3)
            # Delete the volume
            #   Flow of work:
            #       - Click on "Actions" button
            #       - Select "Delete" option and Click on "Delete" button to confirm
            self.efs_filesystem_page.delete_filesystem()
            # Check whether delete successfully or not
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.XPATH,
                                                                                     "//td[contains(.,'" + self.file_name + "')]/parent::*")),
                                                 "Should SUCCEED to delete the filesystem  NOT attached to any ip")
