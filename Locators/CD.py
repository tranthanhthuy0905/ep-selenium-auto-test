from selenium.webdriver.common.by import By

class CustomDomainPageLocators(object):
    CREATE_DOMAIN_BTN = (By.XPATH, "//button[contains(.,'Create domain')]")
    ACTION_BTN = (By.XPATH, "//button[contains(.,'Actions ')]")
    DELETE_BTN = (By.XPATH, "//li[@role='menuitem']/span[text()='Delete']")
    CONFIRM_DELETE_BTN = (By.XPATH, "//button[@class='ant-btn ant-btn-dangerous']/span")
    DOMAIN_TEXTBOX = (By.XPATH, "//*[@id='create-custom-domain']/div[1]/div[2]/div/div/span/span/span/input")
    PORT_TEXTBOX = (By.ID, "create-custom-domain_port")
    TEST_CONNECTION_BTN = (By.XPATH, "//button[contains(.,'Test Connection  ')]")
    CREATE_BTN = (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[3]/button[2]")
    HTTP_PROTOCOL = (By.XPATH, "//div[@title='http://']/div[text()='http://']")
    HTTPS_PROTOCOL = (By.XPATH, "//div[@title='https://']/div[text()='https://']")
    PROTOCOL_SELECTOR = (By.XPATH, "//*[@id='create-custom-domain']/div[1]/div[2]/div/div/span/span/span/span[1]")
    INSTANCE_SELECTOR = (By.XPATH, "//*[@id='create-custom-domain']/div[2]/div[2]/div/div/div[1]/div/div/div/div/div")
    INSTANCE_INFO = lambda _info : (By.XPATH, f"//strong[contains(.,'{_info}')]")
    CHECK_CIRCLE_ICON = (By.XPATH, "//*[@id='create-custom-domain']/button/span[@aria-label='check-circle']")
    CHECK_CLOSE_ICON = (By.XPATH, "//*[@id='create-custom-domain']/button/span[@aria-label='close-circle']")
    ROW_BY_INSTANCE_NAME = lambda _domain_name: (By.XPATH, f"//td[contains(.,'{_domain_name}')]/parent::*")
    SUCCESS_NOTIFICATION = (By.XPATH, "//div[text()='Successful!']")
    FAILED_NOTIFICATION = (By.XPATH, "//span[text()='Failed']")
    CLOSE_NOTIFICATION_BTN = (By.CLASS_NAME, "ant-notification-close-x")
    DOMAIN_RADIO = lambda _domain_id: (By.XPATH, f"//tr[@data-row-key='{_domain_id}']/td[1]/label/span")


