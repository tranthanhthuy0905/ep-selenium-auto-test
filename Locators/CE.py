from selenium.webdriver.common.by import By


class DashboardPageLocators(object):
    CE_BTN = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/a/div')


class CEPageLocators(object):
    INSTANCES_SUBMENU_BTN = (By.LINK_TEXT, 'Instances')
    INSTANCE_TYPES_SUBMENU_BTN = (By.XPATH, '/html/body/div[1]/section/div[2]/aside/div/div[2]/div[1]/ul/li[5]/ul/li[2]/a')
    INSTANCES_MENU_BTN = (By.LINK_TEXT, 'Instances')
    ELASTIC_BLOCK_STORE_MENU_BTN = (By.XPATH, '/html/body/div/section/div[2]/aside/div/div[2]/div[1]/ul/li[6]/div[1]')
    VOLUMES_SUBMENU_BTN = (By.LINK_TEXT, 'Volumes')
    SNAPSHOTS_SUBMENU_BTN = (By.LINK_TEXT, 'Snapshots')
    KEYPAIR_SUBMENU_BTN = (By.LINK_TEXT, 'Key Pairs')




class CEInstancePageLocators(object):
    LAUNCH_INSTANCES_BTN = (By.LINK_TEXT, 'Launch Instance')
    ANNOUNCEMENT = (By.CSS_SELECTOR, 'div > div > div > div.ant-notification-notice-message')
    RADIO_BTN = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div[3]/div/div/div/div/div/div/div[2]/table/tbody/tr[3]/td[1]/label/span/input')
    INSTANCE_STATE_BTN = (By.XPATH, "//button[contains(.,'Instance state ')]")
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

    INSTANCE_STATE = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div/div/div[3]/div[2]/div/div[2]/div/div[4]/div/div/div[2]')
    INSTANCE_STATE_BY_ID = lambda _id: (By.XPATH, f"//tr[@data-row-key='{_id}']/td[4]/div/span")
    INSTANCE_RADIO_BY_ID = lambda _id: (By.XPATH, f"//tr[@data-row-key='{_id}']/td/label/span")
    STOP_STATUS = "Stopped"
    RUNNING_STATUS = "Running"

class CEInstanceTypesPageLocators(object):
    INSTANCE_TYPE_4G_RADIO = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/table/tbody/tr[3]/td[1]/label/span/input')
    INSTANCE_TYPE_32G_RADIO = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/div/div[2]/table/tbody/tr[7]/td[1]/label/span/input')
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
    KEYPAIR_LIST = (By.XPATH, "//*[@id='root']/section/section/main/div/div/div/div/div/div[2]/div[1]/div[3]/div[5]/div[2]/div")
    KEYPAIR_NAME_TEXTBOX = (By.ID, "create-ssh-key-form_name")
    PUBLIC_KEY_TEXTBOX = (By.ID, "create-ssh-key-form_publicKey")
    DEFAULT_PASSWORD_TEXTBOX = (By.ID, "password")
    DEFAULT_PASSWORD_CONFIRM_TEXTBOX = (By.ID, "password_confirm")
    CREATE_KEYPAIR_SUCCESS_MESSAGE = (By.XPATH, "//div[text()='Created keypair successfully.']")
    INSTANCE_NAME_TEXTBOX = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div[2]/div[1]/div[3]/div[1]/div[2]/input')
    LAUNCH_BTN = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div[2]/div[3]/button[3]')
    REVIEW_N_LAUNCH_BTN = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div[2]/div[3]/button[3]')
    ADD_NEW_VOLUME_BTN = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div[2]/div[1]/button/span')
    VOlUME_NAME_TEXTBOX = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[2]/div[1]/input[@class='ant-input']")
    VOLUME_TYPE_LIST = (By.XPATH, '/html/body/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/div/div/span[2]')
    VOLUME_SIZE_TEXTBOX = (By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[2]/div[3]/div/div/div/input")
    PARRENT_BY_VOLUME_NAME = lambda _volume_name: (By.XPATH, f"//td[contains(.,'{_volume_name}')]/parent::*")
    CUSTOM_DISK = (By.XPATH, "//div[text()='Custom Disk']")
    CREATE_VOLUME_BTN = (By.XPATH, "//span[text()='Create']")
    CREATE_VOLUME_SUCCESS_MESSAGE = (By.XPATH, "//div[text()='Created volume successfully.']")
    CLOSE_MESSAGE_BTN = (By.CLASS_NAME, "ant-notification-close-x")
    RADIO_BY_NAME = lambda _radio_name: (By.NAME, f'{_radio_name}')
    CREATE_NEW_SG_RADIO = (By.XPATH, "//*[@id='root']/section/section/main/div/div/div/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[1]/label/span[1]/input")
    SELECT_EXISTING_SG_RADIO = (By.XPATH, "//*[@id='root']/section/section/main/div/div/div/div/div/div[2]/div[1]/div[1]/div[2]/div[2]/div/div[2]/label/span[1]/input")
    SG_NAME_TEXTBOX = (By.XPATH, "//*[@id='root']/section/section/main/div/div/div/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/span/span/input")
    SG_DESCRIPTION_TEXTBOX = (By.XPATH, "//*[@id='root']/section/section/main/div/div/div/div/div/div[2]/div[1]/div[2]/div[3]/div[2]/input")
    ADD_SG_BTN = (By.XPATH, "//button[contains(.,'Add Security Group')]")
    SG_DETAILS_ID = (By.XPATH, "//*[@id='root']/section/section/main/div/div/div/div/div/div[2]/div[1]/div[4]/div/div/div/div/div/div[1]/div[2]/div/div[1]/div[2]/div")
    SG_APPLY_CHECKBOX = (By.XPATH, "/html/body/div[1]/section/section/main/div/div/div/div/div/div[2]/div[1]/div[2]/div/div[2]/label/span[1]")
    CREATE_SG_SUCCESS_MESSAGE = (By.XPATH, "//div[contains(.,'Created security group successfully')]")
    PARRENT_BY_INSTANCE_NAME = lambda _instance_name: (By.XPATH, f"//td[contains(.,'{_instance_name}')]/parent::*")
    STATE_BY_ID = lambda _id: (By.XPATH, f"//tr[@data-row-key='{_id}']/td[@class='ant-table-cell'][2]/div/span/span[@class='ant-badge-status-text']")
    RANDOM_PASSWORD_BTN = (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div[2]/button/span")
    COPY_PASSWORD_BTN = (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div[3]/button/span")
    SHOW_PASSWORD_BTN = (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/span/span")
    APPLY_PASSWORD_BTN = (By.XPATH, "//button[contains(.,'Apply this password')]")
    FAILED_TO_LAUNCH_NOTI = (By.XPATH, "//div[contains(.,'Failed to launch instance.')]")
    EXISTING_SG_RADIO = lambda _sg_id: (By.NAME, f'{_sg_id}')
    LIST_SG_PAGE = (By.XPATH, "//div[@class='ant-select-selector']/span[@class='ant-select-selection-item']")





    # test_launch_instance_01's elements
    REVIEW_INSTANCE_LAUNCH = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div[2]/div[1]/div[1]/div/h2')
    CONFIGURE_INSTANCE_DETAILS = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div[2]/div[1]/div[1]/div/h2')
    APPLY_THIS_PASSWORD = (By.XPATH, "//button[contains(.,'Apply this password')]")
    EDIT_PASSWORD = (By.XPATH, "//button[contains(.,'<< Edit password')]")
    TWO_PASSWORD_NOT_MATCH = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div[2]/div[1]/div[3]/form/div[2]/div[2]/div/div/div[2]/div')

class CEVolumePageLocators(object):
    CHOOSE_VOLUME_RADIO = (By.XPATH, '/html/body/div[1]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div[3]/div/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[1]/label/span/input')
    VOLUME_ACTIONS_BTN = (By.XPATH, '//button[contains(.,"Actions ")]')
    EXPUNGE_VOLUME_BTN = (By.CSS_SELECTOR, 'li.ant-dropdown-menu-item.ant-dropdown-menu-item-only-child:nth-child(4)')
    EXPUNGE_VOLUME_CONFIRM_BTN = (By.XPATH, "//span[text()='Expunge']")
    CREATE_VOLUME_SUCCESS_MESSAGE = (By.XPATH, "//div[text()='Expunge volume is successful!']")
    VOLUME_NAME_IN_LIST = (By.XPATH, "//*[@id='root']/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div[3]/div/div/div/div/div/div/div[2]/table/tbody/tr[2]/td[2]")
    CREATE_VOLUME_BTN = (By.XPATH, "//button[contains(.,' Create Volume')]")
    #VOLUME_LIST = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div[3]/div/div/div/div/div/div/div[2]')

    # Resize Volume Elements
    RESIZE_VOLUME_BTN = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/button[2]')
    SIZE_GB = (By.XPATH, "//div[preceding-sibling::div/div/text()='Size']")
    RESIZE_VOLUME_BOX = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]')
    # OK_BTN = (By.XPATH, "//button/span[text()='OK']")
    OK_BTN = (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[2]")
    SHRINK_OK_BTN = (By.ID, "form_resize_volume_shrink")
    DISK_OFFERING = (By.XPATH, '//*[@id="form_resize_volume"]/div[1]/div[2]/div/div/div')
    SIZE_FORM = (By.XPATH, "//*[@id='form_resize_volume_size']")

    # Attach volume
    ATTACH_VOLUME_BTN = (By.XPATH, "//button[following-sibling::button/div/text()='Actions ' and ./div/span/@class='anticon anticon-link']")
    SELECT_AN_INSTANCE = (By.ID, "form_attach_volume_vm_id")
    ATTACH_VOLUME_BOX = (By.XPATH, "//div[@class='ant-modal-content' and contains(.,'Attach Volume')]")
    ATTACH_OK_BUTTON = (By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div[3]/button[2]")
    # Detach volume
    DETACH_VOLUME_BTN = (By.XPATH, "//span[text()='Detach volume']")
    DETACH_CONFIRM_BTN = (By.XPATH, "//button//span[text()='Detach']")
    # Delete volume
    DELETE_VOLUME_BTN = (By.XPATH, "//span[text()='Delete volume']")
    DELETE_CONFIRM_BUTTON = (By.XPATH, "//button//span[text()='Delete']")

    # Volume detail
    VM_NAME = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[4]/div/div/div[2]')
    VM_STATE = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[8]/div/div/div[2]')
    VM_ID = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div')
    VOLUMES_LIST = (By.XPATH, "//*[@id='root']/section/section/main/div/div/div/div/div/div/div/div/div[1]/div/div")
    CLOSE_MESSAGE_BTN = (By.CLASS_NAME, "ant-notification-close-x")
    VOLUME_STATE_BY_ID = lambda _id: (By.XPATH, f"//tr[@data-row-key='{_id}']/td[3]/div/span/span[2]")



class CECreateVolumePageLocators(object):
    CREATE_VOLUME_BTN = (By.XPATH, "//button[contains(.,'Create Volume')]")
    VOLUME_TYPE_LIST = (By.XPATH, "/html[@class=' ']/body/div[@id='root']/section/section/main/div/div/div/div/div/div/div/div/div[2]/div/div/div")
    CUSTOM_DISK = (By.XPATH, "//div[text()='Custom Disk']")
    DEFAULT_100G = (By.XPATH, "//div[text()='Default (100G)']")
    OPTION_200G = (By.XPATH, "//div[text()='200G']")
    OPTION_500G = (By.XPATH, "//div[text()='500G']")
    VOLUME_NAME_FORM = (By.XPATH, "//*[@id='root']/section/section/main/div/div/div/div/div/div[3]/div[2]/div/div[1]/input")
    VOLUME_SIZE_FORM = (By.XPATH, "/html[@class=' ']/body/div[@id='root']/section/section/main/div/div/div/div/div/div/div/div/div[3]/div/div/div/input")
    CREATE_VOLUME_SUCCESS_MESSAGE = (By.XPATH, "//div[text()='Created volume successfully.']")
    PARRENT_BY_VOLUME_NAME = lambda _volume_name: (By.XPATH, f"//td[contains(.,'{_volume_name}')]/parent::*")

class CESecurityGroupLocators:

    CREATE_SEC_GROUP_TEXTBOX_NAME_CSS = (By.CSS_SELECTOR, "input.ant-input")
    PREVIEW_SEC_GROUP_NAME = (By.XPATH, "//*[@id='root']/section/section/main/div/div/div/div/div/div[2]/div[2]/div/div[2]/span")
    SEC_GROUP_ID = (By.XPATH, "/html/body/div[1]/section/section/main/div/div/div/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div")

    CREATE_BUTTON = (By.XPATH, '//span[text()=" Create Security Group"]')
    SUBMIT_CREATE_BUTTON_X_PATH = (By.XPATH, '//span[text()="Create Security Group"]')
    CREATE_SUCCESSFUL_POPUP_XPATH = (By.XPATH, "//class[text()='Created security group successfully']")

    COLLAPSE_TEXT_BOX_CLASS = (By.CLASS_NAME, "ant-collapse-content-box")
    SECURITY_GROUP_ITEM_HOME_XPATH = (By.XPATH, '//tr[@data-row-key="{security_group_id}"]')

    '''
    Weird note: ADD_INGRESS_BUTTON and ADD_EGRESS_BUTTON has different structure: preceding::div/text() vs div/span/text()
    ADD_EGRESS_BUTTON has extra space and the end of text: 'Egress Rule '
    '''
    ADD_INGRESS_BUTTON = (By.XPATH, '//*[@id="addRule"]/div/div[5]/div/div[2]/div/div/button')
    # ADD_INGRESS_BUTTON = (By.XPATH, "//button[ancestor::form[@id='addRule' "
    #                                 "and (ancestor::div/@class='ant-collapse-content ant-collapse-content-active' "
    #                                 "and preceding::div/text()='Ingress Rule')]][1]")
    ADD_EGRESS_BUTTON = (By.XPATH, "//button[ancestor::form[@id='addRule' "
                                   "and (ancestor::div/@class='ant-collapse-content ant-collapse-content-active' "
                                   "and preceding::div/span/text()='Egress Rule ')]]")

    INGRESS_START_PORT_TEXTBOX = (By.XPATH, "//input[@id='addRule_startport']")
    INGRESS_END_PORT_TEXTBOX = (By.XPATH, "//input[@id='addRule_endport']")
    INGRESS_IMCP_TYPE_TEXTBOX = (By.XPATH, "//input[@id='addRule_icmptype']")
    INGRESS_IMCP_CODE_TEXTBOX = (By.XPATH, "//input[@id='addRule_icmpcode']")
    INGRESS_CIDR_TEXTBOX = (By.XPATH, "//input[@id='addRule_cidrlist']")
    INGRESS_PROTOCOL_SELECTOR = (By.XPATH, '//*[@id="addRule"]/div/div[1]/div/div[2]/div/div/div/div/span[2]')
    INGRESS_PROTOCOL_SELECTOR_INPUT = (By.XPATH, '//*[@id="addRule_protocol"]')

    EGRESS_START_PORT_TEXTBOX = None
    EGRESS_END_PORT_TEXTBOX = None
    EGRESS_CIDR_TEXTBOX = None

    INVALID_CIDR_ALERT = (By.XPATH, "//div[@role='alert']")

    REMOVE_FIRST_INGRESS_RULE_BUTTON = (By.XPATH, '//*[@id="root"]/section/section/main/div/div/div/div/div/div[2]/div/div[3]/div[2]/div/div[2]/div/div/div/div/div[2]/table/tbody/tr[2]/td[8]/button')
    CONFIRM_DELETE_RULE_BUTTON = (By.XPATH, "//button[@type='button' and ./span/text()='Delete']")
    CANCEL_DELETE_RULE_BUTTON = (By.XPATH, "//button[@type='button' and ./span/text()='Cancel']")
    INGRESS_RULE_ROW = lambda protocol, start_port, end_port, cidr: (
        By.XPATH,
        f"//td[@class='ant-table-cell' and text()='{protocol}' "
        f"and following-sibling::td[text()='{start_port}' "
        f"and following-sibling::td[text()='{end_port}' "
        f"and following-sibling::td[following-sibling"
        f"::td[following-sibling"
        f"::td[text()='{cidr}']]]]]]"
    )
    INGRESS_RULE_ICMP_ROW = lambda protocol, icmp_type, icmp_code, cidr: (
            By.XPATH,
            f"//td[@class='ant-table-cell' and text()='{protocol}' "
            f"and following-sibling::td[following-sibling::td[following-sibling::td[text()='{icmp_type}' "
            f"and following-sibling::td[text()='{icmp_code}' "
            f"and following-sibling::td[text()='{cidr}']]]]]]"
        )

class CEKeypairLocators:
    KEYPAIR_NAME_TEXTBOX = (By.XPATH, "//*[@id='create-ssh-key-form_name']")
    PUBLIC_KEY_TEXTBOX = (By.XPATH, "//*[@id='create-ssh-key-form_publicKey']")
    CREATE_KEYPAIR_BTN = (By.XPATH, "//button[contains(.,' Create keypair')]")
    OK_BTN = (By.XPATH, "//button[contains(.,'OK')]")
    FINGERPRINT_BY_KEYPAIR_NAME = lambda _name: (By.XPATH, f"//tr[@data-row-key='{_name}']/td[@class='ant-table-cell'][2]")
    SUCCESSFULLY_MESSAGE = (By.XPATH, "//p[contains(.,'Created keypair successfully.')]")
    CLOSE_BTN = (By.XPATH, "//button[contains(.,'Close')]")



class CESnapshotLocators(object):
    # Create Snapshot
    CREATE_SNAPSHOT_BTN = (By.XPATH, "//span[text()=' Create Snapshot']")
    SNAPSHOT_NAME_FORM = (By.XPATH, "//input[preceding-sibling::div/text()='Snapshot name']")
    SELECT_VOLUME = (By.XPATH, "//div[preceding-sibling::div/text()='Volume']")
    CREATE_SNAPSHOT_CONFIRM = (By.XPATH, "//button[contains(.,'Create Snapshot')]")

    # Actions button
    ACTIONS_BTN = (By.XPATH, "//button[contains(.,'Actions ')]")

    # Delete Snapshot
    DELETE_SNAPSHOT = (By.XPATH, "//span[text()='Delete snapshot']")
    DELETE_CONFIRM = (By.XPATH, "//button[contains(.,'Delete')]")
    # Revert to snapshot
    REVERT_TO_SNAPSHOT = (By.XPATH, "//span[text()='Revert to snapshot']")
    REVERT_CONFIRM = (By.XPATH,"//button[contains(.,'Revert')]")
    # Get Snapshot ID
    PARRENT_BY_SNAPSHOT_NAME = lambda _snapshot_name: (By.XPATH, f"//td[contains(.,'{_snapshot_name}')]/parent::*")
