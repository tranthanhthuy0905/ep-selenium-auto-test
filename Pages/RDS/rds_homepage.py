from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Configs import RDS_BASE_URL, RDS_USER_TOKEN
from Configs.TestData.RDSTestData import RDSTestData
from Locators.RDS import RDSHomePageLocators
from Pages.base_page import BasePage


class RDSHomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver=driver, base_url=RDS_BASE_URL)
        self.driver.get(RDS_BASE_URL)
        self.authenticate(RDS_USER_TOKEN)
        self.locator = RDSHomePageLocators

    def click_create_database_button(self):
        self.click_button(self.locator.CREATE_DB_BTN)
        return self

    def select_cluster(self, cluster_id):
        self.click_button(
            (By.XPATH, '//span[././input/@type="radio" and ancestor::tr/@data-row-key="' + cluster_id + '"]'))
        return self

    def start_cluster(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locator.ACTIONS_BTN),
                                             "Cannot click on 'Actions' button")
        self\
            .click_button(self.locator.ACTIONS_BTN)\
            .click_button(self.locator.START_BTN)\
            .click_button(self.locator.START_CONFIRM_BTN)
        return self

    def restart_cluster(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locator.ACTIONS_BTN),
                                             "Cannot click on 'Actions' button")
        self\
            .click_button(self.locator.ACTIONS_BTN)\
            .click_button(self.locator.RESTART_BTN)\
            .click_button(self.locator.RESTART_CONFIRM_BTN)
        return self

    def stop_cluster(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locator.ACTIONS_BTN),
                                              "Cannot click on 'Actions' button")
        self\
            .click_button(self.locator.ACTIONS_BTN)\
            .click_button(self.locator.STOP_BTN)\
            .click_button(self.locator.STOP_CONFIRM_BTN)
        return self

    def delete_cluster(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locator.ACTIONS_BTN),
                                             "Cannot click on 'Actions' button")
        self\
            .click_button(self.locator.ACTIONS_BTN)\
            .click_button(self.locator.DELETE_BTN)\
            .click_button(self.locator.DELETE_CONFIRM_BTN)
        return self

    def create_read_replica(self, no_of_replica):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locator.ACTIONS_BTN),
                                             "Cannot click on 'Actions' button")
        self\
            .click_button(self.locator.CREATE_READ_REPLICA)\
            .fill_form(no_of_replica, self.locator.NO_OF_SERVERS)\
            .click_button(self.locator.OK_BTN)
        return self
