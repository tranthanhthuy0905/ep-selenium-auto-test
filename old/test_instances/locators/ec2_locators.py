from selenium.webdriver.common.by import By


class DashboardPageLocators(object):
    EC2_BTN = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/a/div')


class EC2PageLocators(object):
    INSTANCES_SUBMENU_BTN = (By.XPATH, '/html/body/div[1]/section/div[2]/aside/div/div[2]/div[1]/ul/li[5]/ul/li[1]/a')
    INSTANCE_TYPES_SUBMENU_BTN = (By.XPATH, '/html/body/div[1]/section/div[2]/aside/div/div[2]/div[1]/ul/li[5]/ul/li[2]/a')
    INSTANCES_MENU_BTN = (By.XPATH, '/html/body/div[1]/section/div[2]/aside/div/div[2]/div[1]/ul/li[5]/div')
    ELASTIC_BLOCK_STORE_MENU_BTN = (By.XPATH, '/html/body/div/section/div[2]/aside/div/div[2]/div[1]/ul/li[6]/div[1]')
    VOLUMES_SUBMENU_BTN = (By.XPATH, '/html/body/div[1]/section/div[2]/aside/div/div[2]/div[1]/ul/li[6]/ul/li[1]/a')


class EC2InstancePageLocators(object):
    LAUNCH_INSTANCES_BTN = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/button[3]/a')
    ANNOUNCEMENT = (By.CSS_SELECTOR, 'div > div > div > div.ant-notification-notice-message')
    RADIO_BTN = (By.CSS_SELECTOR, '#root > section > section > main > div > div > div > div > div > div > div > div:nth-child(1) > div > div > div.ant-card-body > div.ant-spin-nested-loading > div > div > div > div > div > div > div.ant-table-body > table > tbody > tr.ant-table-row.ant-table-row-level-0 > td.ant-table-cell.ant-table-selection-column > label > span > input')
    INSTANCE_STATE_BTN = (By.CSS_SELECTOR, '#root > section > section > main > div > div > div > div > div > div > div > div:nth-child(1) > div > div > div.ant-card-head > div > div.ant-card-extra > div > button:nth-child(3) > div')
    STOP_INSTANCE_BTN = (By.CSS_SELECTOR, 'li.ant-dropdown-menu-item.ant-dropdown-menu-item-only-child:nth-child(1)')
    START_INSTANCE_BTN = (By.CSS_SELECTOR, 'li.ant-dropdown-menu-item.ant-dropdown-menu-item-only-child:nth-child(2)')
    REBOOT_INSTANCE_BTN = (By.CSS_SELECTOR, 'li.ant-dropdown-menu-item.ant-dropdown-menu-item-only-child:nth-child(3)')
    TERMINATE_INSTANCE_BTN = (By.CSS_SELECTOR, 'li.ant-dropdown-menu-item.ant-dropdown-menu-item-only-child:nth-child(4)')
    STOP_CONFIRM_BTN = (By.XPATH, "//span[text()='Stop']")
    START_CONFIRM_BTN = (By.XPATH, "//span[text()='Start']")
    REBOOT_CONFIRM_BTN = (By.XPATH, "//span[text()='Reboot']")
    TERMINATE_CONFIRM_BTN = (By.XPATH, "//span[text()='Terminate']")
    LAUNCH_VM_SUCCESS_MESSAGE = (By.XPATH, '//div[text()="Launched an instance successfully."]')
    STOP_VM_SUCCESS_MESSAGE = (By.XPATH, '//div[text()="Stop instance is successful!"]')
    REBOOT_VM_SUCCESS_MESSAGE = (By.XPATH, '//div[text()="Start instance is successful!"]')
    START_VM_SUCCESS_MESSAGE = (By.XPATH, '//div[text()="Start instance is successful!"]')
    # TERMINATE_VM_SUCCESS_MESSAGE = (By.XPATH, '//div[text()=""]')
    LAUNCH_VM_ERROR_MESSAGE = (By.XPATH, '//div[text()="Failed to launch instance."]')
    COPY_CLIPBOARD_SUCCESS_MESSAGE = (By.XPATH, '//div[text()="Copy to clipboard is successful"]')
    CONNECT_BTN = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/button[2]')
    INSTANCE_DETAILS_TAB = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div[3]/div[2]/div/div[1]/div[2]/div[1]/div[1]/div/div[1]/div')
    INSTANCE_VOLUME_TAB = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div[3]/div[2]/div/div[1]/div[2]/div[1]/div[1]/div/div[2]/div')
    INSTANCE_SECURITY_GROUP_TAB = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div[3]/div[2]/div/div[1]/div[2]/div[1]/div[1]/div/div[3]/div')
    INSTANCE_NETWORKING_TAB = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div[3]/div[2]/div/div[1]/div[2]/div[1]/div[1]/div/div[2]/div')
    DROP_DOWN_LIST_BTN = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div[3]/div[2]/div/div[2]/div/div/div[1]')
    COPY = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div[3]/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/span/span')
    REFRESH_BTN = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/button[1]')


class EC2InstanceTypesPageLocators(object):
    INTANCE_TYPE_4G_RADIO = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/table/tbody/tr[3]/td[1]/label/span/input')
    INTANCE_TYPE_32G_RADIO = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/table/tbody/tr[7]/td[1]/label/span/input')
    MEMORY_SORTER = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/table/thead/tr/th[5]/div/div')
    COPY = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div/div[3]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/span/span')
    COPY_CLIPBOARD_SUCCESS_MESSAGE = (By.XPATH, '//div[text()="Copy to clipboard is successful"]')
    REFRESH_BTN = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/button')


class EC2LaunchInstancesWizardPageLocators(object):
    MI_SELECT_BTN = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div[2]/div[1]/div[3]/div/div/div[2]/div/div/div/div[1]/div/ul/li/ul/li/button')
    TYPE_2G_RADIO = (By.NAME, 'b7b4474b-61d5-49db-adb5-bd0a029a35e3')
    NEXT_BTN = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div[2]/div[3]/button[4]')
    INSTANCE_NAME_FORM = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div[2]/div[1]/div[3]/div[1]/div[2]/input')
    LAUNCH_BTN = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div[2]/div[3]/button[3]')
    REVIEW_N_LAUNCH_BTN = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div[2]/div[3]/button[3]')
    ADD_NEW_VOLUME_BTN = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div[2]/div[1]/button/span')
    VOlUME_NAME_FORM = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[1]/input')
    VOLUME_TYPE_LIST = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div')
    VOLUME_SIZE_FORM = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/input')
    CUSTOM_DISK = (By.XPATH, "//div[text()='Custom Disk']")
    CREATE_VOlUMNE_BTN = (By.XPATH, "//span[text()='Create']")
    CREATE_VOLUMNE_SUCCESS_MESSAGE = (By.XPATH, "//div[text()='Created volume successfully.']")


class EC2ElasticBlockStoreVolumnePageLocators(object):
    CHOOSE_VOLUMNE_RADIO = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div[3]/div/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[1]/label/span/input')
    VOLUME_ACTIONS_BTN = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/button[4]')
    EXPUNGE_VOLUME_BTN = (By.CSS_SELECTOR, 'li.ant-dropdown-menu-item.ant-dropdown-menu-item-only-child:nth-child(4)')
    EXPUNGE_VOLUME_CONFIRM_BTN = (By.XPATH, "//span[text()='Expunge']")
    CREATE_VOLUMNE_SUCCESS_MESSAGE = (By.XPATH, "//div[text()='Expunge volume is successful!']")


