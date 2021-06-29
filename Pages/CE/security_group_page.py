
from selenium.webdriver.common.keys import Keys

from Pages.base_page import BasePage
from Configs import CE_SG_URL
from Configs import CE_USER_TOKEN
from Configs.TestData.CESecurityGroupTestData import CESecurityGroupTestData

from Locators.CE import CESecurityGroupLocators


class SGHomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, CE_SG_URL)
        self.authenticate(CE_USER_TOKEN)

    def click_create_button(self):
        self.driver.find_element(*CESecurityGroupLocators.CREATE_BUTTON).click()

    def fill_sg_information(self):
        sec_group_name = CESecurityGroupTestData.SECURITY_GROUP_NAME
        name_text_box = self.driver.find_element(*CESecurityGroupLocators.CREATE_SEC_GROUP_TEXTBOX_NAME_CSS)
        name_text_box.send_keys(Keys.COMMAND + "a" + Keys.DELETE)
        name_text_box.send_keys(sec_group_name)
        return sec_group_name

    def click_create_submit_button(self):
        self.driver.find_element(*CESecurityGroupLocators.SUBMIT_CREATE_BUTTON_X_PATH).click()

    def fill_in_ingress_rule_info(self):
        start_port_text_box = self.find_element(*CESecurityGroupLocators.INGRESS_START_PORT_TEXTBOX)
        end_port_text_box = self.find_element(*CESecurityGroupLocators.INGRESS_END_PORT_TEXTBOX)

    def fill_in_egress_rule_info(self):
        start_port_text_box = self.find_element(*CESecurityGroupLocators.EGRESS_START_PORT_TEXTBOX)
        end_port_text_box = self.find_element(*CESecurityGroupLocators.EGRESS_END_PORT_TEXTBOX)

    def click_add_ingress(self):
        self.find_element(*CESecurityGroupLocators.ADD_INGRESS_BUTTON)

    def click_add_egress(self):
        self.find_element(*CESecurityGroupLocators.ADD_EGRESS_BUTTON)

    def add_ingress_rule(self):
        self.fill_in_ingress_rule_info()
        self.click_add_ingress()

    def add_egress_rull(self):
        self.fill_in_egress_rule_info()
        self.click_add_egress()




