from selenium.webdriver.common.by import By


class DashboardPageLocators(object):
    CE_BTN = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/a/div')


class CEPageLocators(object):
    INSTANCES_SUBMENU_BTN = (By.LINK_TEXT, 'Instances')
    INSTANCE_TYPES_SUBMENU_BTN = (By.XPATH, '/html/body/div[1]/section/div[2]/aside/div/div[2]/div[1]/ul/li[5]/ul/li[2]/a')
    INSTANCES_MENU_BTN = (By.LINK_TEXT, 'Instances')
    ELASTIC_BLOCK_STORE_MENU_BTN = (By.XPATH, '/html/body/div/section/div[2]/aside/div/div[2]/div[1]/ul/li[6]/div[1]')
    VOLUMES_SUBMENU_BTN = (By.LINK_TEXT, 'Volumes')


class CEInstancePageLocators(object):
    LAUNCH_INSTANCES_BTN = (By.LINK_TEXT, 'Launch Instance')
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


class CEInstanceTypesPageLocators(object):
    INTANCE_TYPE_4G_RADIO = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/table/tbody/tr[3]/td[1]/label/span/input')
    INTANCE_TYPE_32G_RADIO = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/table/tbody/tr[7]/td[1]/label/span/input')
    MEMORY_SORTER = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[1]/table/thead/tr/th[5]/div/div')
    COPY = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div/div[3]/div[2]/div/div[2]/div/div[1]/div/div/div[2]/div/span/span')
    COPY_CLIPBOARD_SUCCESS_MESSAGE = (By.XPATH, '//div[text()="Copy to clipboard is successful"]')
    REFRESH_BTN = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/button')


class CELaunchInstancesWizardPageLocators(object):
    MI_SELECT_BTN = (By.XPATH, "//button[contains(.,'Select')]")
    TYPE_2G_RADIO = (By.NAME, '872c5a42-fbb1-4d94-9482-6def419ec553')
    NEXT_BTN = (By.XPATH, "//button[contains(.,'Next')]")
    CREATE_NEW_KEYPAIR_BTN = (By.XPATH, "//button[contains(.,'Create new Keypair')]")
    CREATE_NEW_KEYPAIR_OK_BTN = (By.XPATH, "//button[contains(.,'OK')]")
    CREATE_NEW_KEYPAIR_CLOSE_BTN = (By.XPATH, "//button[contains(.,'Close')]")
    CREATE_NEW_KEYPAIR_SUCCESS_MESSAGE = (By.XPATH, "//div[contains(.,'Created keypair successfully.')]")
    KEYPAIR_LIST = (By.XPATH, "/html[@class=' ']/body/div[@id='root']/section/section/main/div/div/div/div/div/div/div/div/div[2]/div/div/div")
    KEYPAIR_NAME = (By.ID, "create-ssh-key-form_name")
    PUBLIC_KEY = (By.ID, "create-ssh-key-form_publicKey")
    DEFAULT_PASSWORD = (By.ID, "password")
    DEFAULT_PASSWORD_CONFIRM = (By.ID, "password_confirm")
    CREATE_KEYPAIR_SUCCESS_MESSAGE = (By.XPATH, "//div[text()='Created keypair successfully.']")
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

    # test_launch_instance_01's elements
    APPLY_THIS_PASSWORD = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]/span")
    EDIT_PASSWORD = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[1]/span")
    DEFAULT_PASSWORD = (By.ID, "password")
    DEFAULT_PASSWORD_CONFIRM = (By.ID, "password_confirm")
    TWO_PASSWORD_NOT_MATCH = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div[2]/div[1]/div[3]/form/div[2]/div[2]/div/div/div[2]/div')

class CEVolumnePageLocators(object):
    CHOOSE_VOLUMNE_RADIO = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div[3]/div/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[1]/label/span/input')
    VOLUME_ACTIONS_BTN = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/button[4]')
    EXPUNGE_VOLUME_BTN = (By.CSS_SELECTOR, 'li.ant-dropdown-menu-item.ant-dropdown-menu-item-only-child:nth-child(4)')
    EXPUNGE_VOLUME_CONFIRM_BTN = (By.XPATH, "//span[text()='Expunge']")
    CREATE_VOLUMNE_SUCCESS_MESSAGE = (By.XPATH, "//div[text()='Expunge volume is successful!']")
    VOLUME_NAME_IN_LIST = (By.XPATH, "//*[@id='root']/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div[3]/div/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[2]")
    CREATE_VOLUME_BTN = (By.XPATH, "//button[contains(.,' Create Volume')]")



class CECreateVolumnePageLocators(object):
    CREATE_VOlUMNE_BTN = (By.XPATH, "//button[contains(.,'Create Volume')]")
    VOLUME_TYPE_LIST = (By.XPATH, "/html[@class=' ']/body/div[@id='root']/section/section/main/div/div/div/div/div/div/div/div/div[2]/div/div/div")
    CUSTOM_DISK = (By.XPATH, "//div[text()='Custom Disk']")
    VOLUME_NAME_FORM = (By.XPATH, "//*[@id='root']/section/section/main/div/div/div/div/div/div[3]/div[2]/div/div[1]/input")
    VOLUME_SIZE_FORM = (By.XPATH, "/html[@class=' ']/body/div[@id='root']/section/section/main/div/div/div/div/div/div/div/div/div[3]/div/div/div/input")
    CREATE_VOLUMNE_SUCCESS_MESSAGE = (By.XPATH, "//div[text()='Created volume successfully.']")

class CESecurityGroupLocators:

    CREATE_SEC_GROUP_TEXTBOX_NAME_CSS = (By.CSS_SELECTOR, "input.ant-input")

    CREATE_BUTTON = (By.XPATH, '//span[text()=" Create Security Group"]')
    SUBMIT_CREATE_BUTTON_X_PATH = (By.XPATH, '//span[text()="Create Security Group"]')
    CREATE_SUCCESSFUL_POPUP_XPATH = (By.XPATH, "//class[text()='Created security group successfully']")

    COLLAPSE_TEXT_BOX_CLASS = (By.CLASS_NAME, "ant-collapse-content-box")
    SECURITY_GROUP_ITEM_HOME_XPATH = (By.XPATH, '//tr[@data-row-key="{security_group_id}"]')

    ADD_INGRESS_BUTTON = None
    ADD_EGRESS_BUTTON = None

    INGRESS_START_PORT_TEXTBOX = None
    INGRESS_END_PORT_TEXTBOX = None

    EGRESS_START_PORT_TEXTBOX = None
    EGRESS_END_PORT_TEXTBOX = None