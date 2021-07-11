from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage
from Locators.CD import CustomDomainPageLocators
import time
from Configs import *

class CustomDomainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, CUSTOM_DOMAIN_BASE_URL)
        self.locator = CustomDomainPageLocators
        self.driver.get(CUSTOM_DOMAIN_BASE_URL)
        self.authenticate(CUSTOM_DOMAIN_USER_TOKEN)


    def click_create_domain_btn(self):
        self.click_button(self.locator.CREATE_DOMAIN_BTN)
        

    def fill_domain_name(self, domain_name):
        self.fill_form(domain_name, self.locator.DOMAIN_TEXTBOX)
        

    def fill_port(self, port):
        self.fill_form(port, self.locator.PORT_TEXTBOX)
        

    def click_test_connection(self):
        self.click_button(self.locator.TEST_CONNECTION_BTN)
        

    def click_create_btn(self):
        self.click_button(self.locator.CREATE_BTN)
        



    def choose_protocol(self, protocol):
        self\
            .wait_and_click_button(self.locator.PROTOCOL_SELECTOR)\
            .click_button(protocol)
        

    def choose_instance(self, instance_info):
        self\
            .wait_and_click_button(self.locator.INSTANCE_SELECTOR)\
            .click_button(self.locator.INSTANCE_INFO(instance_info))
        

    def check_connection_is_success(self):
        self.check_element_existence(self.locator.CHECK_CIRCLE_ICON)
    
    def check_connection_is_fail(self):
        self.check_element_existence(self.locator.CHECK_CLOSE_ICON)
        

    def check_action_successfully(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.locator.SUCCESS_NOTIFICATION))
            self.click_button(self.locator.CLOSE_NOTIFICATION_BTN)
        except:
            return False

    def check_action_fail(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.locator.FAILED_NOTIFICATION))
            return True
        except:
            return False
        

    def check_if_created_domain_successfully(self, domain_name):
        try:
            self.check_action_successfully()
            self.check_domain_existence(domain_name)    
            return True
        except:
            return False

    def check_if_deleted_domain_successfully(self, domain_id):
        try:
            WebDriverWait(self.driver, 30).until(EC.invisibility_of_element_located(self.locator.DOMAIN_RADIO(domain_id)))
            return True
        except:
            return False        


    def check_domain_existence(self, domain_name):
        self.check_element_existence(self.locator.ROW_BY_INSTANCE_NAME(domain_name))

    def get_domain_id(self, domain_name):
        row = self.find_element(*self.locator.ROW_BY_INSTANCE_NAME(domain_name))
        return row.get_attribute("data-row-key")

    def create_custom_domain(self, protocol_locator, domain_name, port, instance_info):
        # Click on "Create domain" button on the top right corner
        self.click_create_domain_btn()
        # Select Http:// protocol
        self.choose_protocol(protocol_locator)
        # Fill in Domain name textbox
        self.fill_domain_name(domain_name)
        # Fill in port textbox
        self.fill_port(port)
        # Select Instance in IPAddress list
        self.choose_instance(instance_info)

    def select_domain(self, domain_id):
        self.click_button(self.locator.DOMAIN_RADIO(domain_id))

    def delete_domain(self, domain_id):
        self.select_domain(domain_id)
        self.click_button(self.locator.ACTION_BTN)
        self.click_button(self.locator.DELETE_BTN)
        self.wait_and_click_button(self.locator.CONFIRM_DELETE_BTN)


        
        
        

    