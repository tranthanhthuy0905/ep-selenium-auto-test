from selenium.webdriver.common.by import By

class RDSHomePageLocators(object):
    CREATE_DB_BTN = (By.LINK_TEXT, "Create database")
    ACTIONS_BTN = (By.XPATH, "//button[contains(.,'Actions ')]")
    START_BTN = (By.XPATH, "//span[text()='Start']")
    START_CONFIRM_BTN = (By.XPATH, "//button[contains(.,'Start')]")
    RESTART_BTN = (By.XPATH, "//span[text()='Restart']")
    RESTART_CONFIRM_BTN = (By.XPATH, "//button[contains(.,'Restart')]")
    STOP_BTN = (By.XPATH, "//span[text()='Stop']")
    STOP_CONFIRM_BTN = (By.XPATH, "//button[contains(.,'Stop')]")
    DELETE_BTN = (By.XPATH, "//span[text()='Delete']")
    DELETE_CONFIRM_BTN = (By.XPATH, "//button[contains(.,'Delete')]")
    CREATE_READ_REPLICA = (By.XPATH, "//*[local-name()='svg' and @data-icon='plus-circle']")
    NO_OF_SERVERS = (By.ID, "form_create_read_replica_n_servers")
    OK_BTN = (By.XPATH, "//button[contains(.,'OK')]")
    PROGRESS_STATUS = (By.XPATH, "//*[local-name()='svg' and @class='ant-progress-circle' and following-sibling::span/span/@class='anticon anticon-check']")
    REFRESH_BTN = (By.XPATH, "//*[local-name()='svg' and @data-icon='reload']/*[local-name()='path']")

class RDSCreatePageLocators(object):
    CUSTOM_CONFIGS = (By.XPATH, "//div[contains(.,'Custom') and @class='ant-col ant-col-6 gutter-row']")
    DB_INSTANCE_CLASS = (By.ID, "form_create_database_service_offering")
    FIRST_CPU_OPTION = (By.XPATH, "//div[@cpunumber='1']")
    NO_OF_REPLICA = (By.ID, "form_create_database_n_servers")
    DB_INSTANCE_IDENTIFIER = (By.ID, "form_create_database_name")
    MASTER_PASSWORD = (By.ID, "form_create_database_pg_password")
    CONFIRM_PASSWORD = (By.ID, "form_create_database_pg_password_confirm")

    DEV_TEST_CONFIGS = (By.XPATH, "//div[contains(.,'Dev/Test') and @class='ant-col ant-col-6 gutter-row']")

    PRODUCTION_CONFIGS = (By.XPATH, "//div[contains(.,'Production') and @class='ant-col ant-col-6 gutter-row']")

    CREATE_DB_SUBMIT = (By.XPATH, "//button[contains(.,'Create database')]")
    RESET_BTN = (By.XPATH, "//button[contains(.,'Reset')]")
