
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.base_page import BasePage
from Configs import CE_SG_URL, CE_SG_CREATE_URL, CE_SG_DETAILS_PAGE_URL
from Configs import CE_USER_TOKEN
from Configs.TestData.CESecurityGroupTestData import CESecurityGroupTestData

from Locators.CE import CESecurityGroupLocators


class SGHomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, CE_SG_URL)
        self.driver.get(CE_SG_URL)
        self.authenticate(CE_USER_TOKEN)
        self.driver.get(CE_SG_URL)

    def click_create_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(CESecurityGroupLocators.CREATE_BUTTON)
        )
        self.driver.find_element(*CESecurityGroupLocators.CREATE_BUTTON).click()


class SGCreatePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, CE_SG_CREATE_URL)
        self.driver.get(CE_SG_CREATE_URL)

    def fill_sg_information(self):
        sec_group_name = CESecurityGroupTestData.SECURITY_GROUP_NAME
        name_text_box = self.driver.find_element(*CESecurityGroupLocators.CREATE_SEC_GROUP_TEXTBOX_NAME_CSS)
        name_text_box.send_keys(Keys.COMMAND + "a" + Keys.DELETE)
        name_text_box.send_keys(sec_group_name)
        return sec_group_name

    def click_create_submit_button(self):
        self.driver.find_element(*CESecurityGroupLocators.SUBMIT_CREATE_BUTTON_X_PATH).click()


class SGDetailsPage(BasePage):
    def __init__(self, driver, sg_id):
        super().__init__(driver, CE_SG_DETAILS_PAGE_URL.format(sg_id=sg_id))

    def fill_in_ingress_rule_info(self, start_port, end_port):
        start_port_text_box = self.find_element(*CESecurityGroupLocators.INGRESS_START_PORT_TEXTBOX)
        end_port_text_box = self.find_element(*CESecurityGroupLocators.INGRESS_END_PORT_TEXTBOX)
        start_port_text_box.send_keys(start_port)
        end_port_text_box.send_keys(end_port)

    def fill_in_egress_rule_info(self):
        start_port_text_box = self.find_element(*CESecurityGroupLocators.EGRESS_START_PORT_TEXTBOX)
        end_port_text_box = self.find_element(*CESecurityGroupLocators.EGRESS_END_PORT_TEXTBOX)

    def click_add_ingress(self):
        self.find_element(*CESecurityGroupLocators.ADD_INGRESS_BUTTON).click()

    def click_add_egress(self):
        self.find_element(*CESecurityGroupLocators.ADD_EGRESS_BUTTON).click()

    def add_ingress_rule(self, start_port, end_port):
        self.fill_in_ingress_rule_info(start_port, end_port)
        self.click_add_ingress()

    def add_egress_rull(self):
        self.fill_in_egress_rule_info()
        self.click_add_egress()

    def add_ingress_cidr(self, cidr):
        ingress_cidr_textbox = self.find_element(*CESecurityGroupLocators.INGRESS_CIDR_TEXTBOX)
        # ingress_cidr_textbox.clear()
        ingress_cidr_textbox.send_keys(cidr)
        self.click_add_ingress()
        time.sleep(10)

