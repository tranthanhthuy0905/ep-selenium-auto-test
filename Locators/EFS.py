from selenium.webdriver.common.by import By


class EFSHomePageLocators(object):
    FILES_SYSTEMS = (By.XPATH, "//a[contains(@href,'/efs/file-systems') and ./@class='ant-btn ant-btn-default']")

class EFSFileSystemLocators(object):

    # Mount Command
    MOUNT_COMMAND = (By.XPATH,"//div[preceding-sibling::div/div/text()='Mount Command']")

    # Create File System
    CREATE_FILE_SYSTEM_BTN = (By.XPATH, "//button[contains(.,'Create file system')]")
    INPUT_FILESYSTEM_NAME = (By.XPATH,"//input[@placeholder='Apply a name to your file system']")
    OK_BTN = (By.XPATH, "//button[contains(.,'OK')]")

    # Allow Access Points
    ALLOW_IP_BTN = (By.XPATH, "//button[contains(.,'Allow IP')]")
    ADD_FIELD_BTN = (By.XPATH, "//button[contains(.,'Add field')]")
    INPUT_IP = (By.XPATH, "//input[@id='form_allow_ip_to_access_point_listIP_0_ip']")
    IP_REMOVE_BTN = (By.XPATH, "//*[local-name()='svg' and @data-icon='minus-circle']")
    "//*[local-name()='svg' and @data-icon='minus-circle' and ancestor::div/div/div/div//input/@value='172.25.148.98']"
    ALLOW_IP_OK = (By.XPATH, "//button[contains(.,'OK') and ancestor::div//div//text()='Allow IP to access point']")
    READ_ONLY_CHECKBOX = (By.XPATH, "//input[@id='form_allow_ip_to_access_point_listIP_0_read_only']")
    CLOSE_BTN = (By.XPATH, "//button[@class='ant-modal-close' and following-sibling::div/div/text()='Allow IP to access point']")

    # Delete EFS
    ACTIONS_BTN = (By.XPATH, "//button[contains(.,'Actions ')]")
    DELETE_OPTION = (By.XPATH, "//span[text()='Delete']")
    DELETE_CONFIRM = (By.XPATH, "//button[contains(.,'Delete')]")

