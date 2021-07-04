import time
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Configs.TestData.CEVolumeTestData import CEVolumeTestData

from Locators.CE import CEInstancePageLocators, CEVolumePageLocators, CECreateVolumePageLocators
from Pages.CE.create_volume_page import CECreateVolumePage
from Pages.base_page import BasePage
from Pages.CE.launch_instances_wizard_page import CELaunchInstancesWizardPage
from Configs import CE_VOLUME_URL
from selenium.common.exceptions import TimeoutException


class CEVolumePage(BasePage):
    def __init__(self, driver):
        self.locator = CEVolumePageLocators
        super().__init__(driver, CE_VOLUME_URL)


    def click_create_volume_btn(self):
        self.driver.find_element(*self.locator.CREATE_VOLUME_BTN).click()

    def create_new_volume(self, volume_size, disk_option):
        # *** Create a volume ***
        # When user clicks on "Create Volume" button on the top right
        self.click_create_volume_btn()
        self.create_volume_page = CECreateVolumePage(self.driver)

        # When user clicks on "Create" button
        self.volume_name = CEVolumeTestData.VOLUME_NAME
        time.sleep(2)
        self.create_volume_page.create_volume(volume_name=self.volume_name, volume_size=volume_size, disk_option=disk_option)

    # def attach_volume_to_instance(self, instance_name):
    #     self\
    #         .click_button(CEVolumePageLocators.SELECT_AN_INSTANCE)\
    #         .click_button(By.XPATH, '//div[text()="'+ instance_name +'"]')\
    #         .click_button(CEVolumePageLocators.OK_BTN)
    #     self

    def attach_volume_to_instance(self, instance_name, instance_state):
        # *** Attach the volume with the running VM ***
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(CEVolumePageLocators.ATTACH_VOLUME_BTN))
        self.click_button(CEVolumePageLocators.ATTACH_VOLUME_BTN)
        #     .click_button(CEVolumePageLocators.SELECT_AN_INSTANCE)\
        #     .click_button(By.XPATH, '//div[text()="'+ instance_name +'"]')\
        #     .click_button(CEVolumePageLocators.OK_BTN)
        self.find_element(*CEVolumePageLocators.SELECT_AN_INSTANCE) \
            .send_keys(instance_name)
        self.find_element(*CEVolumePageLocators.SELECT_AN_INSTANCE) \
            .send_keys(Keys.ENTER)
        time.sleep(2)
        self.click_button(CEVolumePageLocators.OK_BTN)
        # *** Check if the volume is attached with VM successfully or not ***
        self.assertTrue(
            self.volume_page.check_element_existence(
                (By.XPATH,
                 '//td[text()="' + self.instance_name + '" and ancestor::tr/@data-row-key="' + self.volume_name + '"]')),
            "Should successfully attach the volume with a "+ instance_state + " VM"
        )

    def detach_volume_from_vm(self):
        self\
            .click_button(self.locator.VOLUME_ACTIONS_BTN)
        self.ass
    def choose_disk_offering_option(self, locator, option):
        try:
            self.find_element(*locator)
            self.click_button(option)
            return self
        except TimeoutException:
            self.driver.get_screenshot_as_file(
                'error_snapshot/{filename}.png'.format(filename='choose_disk_offering_option'))
            self.driver.quit()


    def choose_Shrink_OK(self):
        self\
            .click_button(self.locator.SHRINK_OK_BTN)
        self
    #
    def check_size_gb(self):
        size_gb = self.driver.find_element(*self.locator.SIZE_GB).text
        return size_gb

    # def change_instance_states(self, state_button, confirm_button, message):
    #     self.click_button(self.locator.RADIO_BTN)\
    #         .click_button(self.locator.INSTANCE_STATE_BTN)\
    #         .click_button(state_button)\
    #         .wait_and_click_button(confirm_button)
    #     if message:
    #         self.check_element_existence(message)
    #     return self


