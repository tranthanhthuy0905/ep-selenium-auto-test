from Configs.TestData import CEInstanceTestData
from Locators.CE import CELaunchInstancesWizardPageLocators
from Pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Configs import CE_INSTANCE_CREATE_WIZARD_URL
from selenium.webdriver.common.by import By
import time


class CELaunchInstancesWizardPage(BasePage):
    def __init__(self, driver):
        self.locator = CELaunchInstancesWizardPageLocators
        super().__init__(driver, CE_INSTANCE_CREATE_WIZARD_URL)

    def choose_volume_type(self, locator):
        try:
            self.find_element(*locator)
            self.click_button(self.locator.CUSTOM_DISK)
            return self
        except TimeoutException:
            self.driver.get_screenshot_as_file(
                'error_snapshot/{filename}.png'.format(filename='choose_volume_type'))
            self.driver.quit()

    def choose_instance_details(self):
        self.instance_name = CEInstanceTestData.INSTANCE_NAME
        self\
            .click_button(self.locator.MI_SELECT_BTN)\
            .click_button(self.locator.TYPE_2G_RADIO)\
            .click_button(self.locator.NEXT_BTN)\
            .fill_form(self.instance_name, self.locator.INSTANCE_NAME_FORM)
        return self

    def click_next_btn(self):
        self\
            .click_button(self.locator.NEXT_BTN)
        return self

    def click_review_and_launch_btn(self):
        self\
            .click_button(self.locator.REVIEW_N_LAUNCH_BTN)
        return self

    def review_and_launch_instance(self):
        self\
            .click_button(self.locator.REVIEW_N_LAUNCH_BTN)\
            .click_button(self.locator.LAUNCH_BTN)
        return self

    """
        Define two options: Apply the default password and Edit own password
    """
    def apply_default_password(self):
        self\
            .click_button(self.locator.APPLY_THIS_PASSWORD) \
            .click_button(self.locator.LAUNCH_BTN)

    def edit_password(self):
        self\
            .click_button(self.locator.EDIT_PASSWORD)

    def input_password(self, value1, value2):
        self \
            .fill_form(value1, self.locator.DEFAULT_PASSWORD_TEXTBOX) \
            .fill_form(value2, self.locator.DEFAULT_PASSWORD_CONFIRM_TEXTBOX)


class MachineImageWizardPage(CELaunchInstancesWizardPage):
    def __init__(self, driver):
        self.locator = CELaunchInstancesWizardPageLocators
        super().__init__(driver)

    def choose_machine_image(self):
        self\
            .click_button(self.locator.MI_SELECT_BTN)
        return self

class InstanceTypeWizardPage(CELaunchInstancesWizardPage):
    def __init__(self, driver):
        self.locator = CELaunchInstancesWizardPageLocators
        super().__init__(driver)

    def choose_instance_type(self):
        self\
            .click_button(self.locator.TYPE_2G_RADIO)
        return self

class ConfigureInstanceWizardPage(CELaunchInstancesWizardPage):
    def __init__(self, driver):
        self.locator = CELaunchInstancesWizardPageLocators
        super().__init__(driver)

    def fill_instance_name(self, instance_name):
        self.fill_form(instance_name, self.locator.INSTANCE_NAME_TEXTBOX)
        return self

    def choose_keypair(self):
        self\
            .click_button(self.locator.KEYPAIR_LIST)\
            .choose_keypair_in_selector(self.locator.KEYPAIR_LIST)
        return self

    def fill_keypair_info(self, name, publicKey):
        self\
            .fill_form(name, self.locator.KEYPAIR_NAME_TEXTBOX)\
            .fill_form(publicKey, self.locator.PUBLIC_KEY_TEXTBOX)
        return self

    # TODO
    def choose_keypair_in_selector(self, locator):
        try:
            self.find_element(*locator)
            self.click_button((By.XPATH,"//div[text()='bc:89:6b:6d:32:fd:7c:24:dd:e0:7a:da:6d:3a:f3:62']"))
            return self
        except TimeoutException:
            self.driver.get_screenshot_as_file(
                'error_snapshot/{filename}.png'.format(filename='choose_volume_type'))
            self.driver.quit()

    def fill_default_password(self, password, confirm_password):
        self\
            .fill_form(password, self.locator.DEFAULT_PASSWORD_TEXTBOX)\
            .fill_form(confirm_password, self.locator.DEFAULT_PASSWORD_CONFIRM_TEXTBOX)
        return self

    def create_new_keypair(self, keypair_name, description):
        # Click on "Create new Keypair"
        self.click_button(self.locator.CREATE_NEW_KEYPAIR_BTN)
        # Fill in the form for creating keypair then click ok
        self.fill_keypair_info(keypair_name, description)
        self.click_button(self.locator.CREATE_NEW_KEYPAIR_OK_BTN)
        # Check the new keypair is created successfully
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.locator.CREATE_NEW_KEYPAIR_SUCCESS_MESSAGE))
        # Click on "Close"
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.locator.CREATE_NEW_KEYPAIR_CLOSE_BTN))
        self.click_button(self.locator.CREATE_NEW_KEYPAIR_CLOSE_BTN)
        # Close popup message
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.locator.CLOSE_MESSAGE_BTN))
        self.click_button(self.locator.CLOSE_MESSAGE_BTN)




class AddStorageWizardPage(CELaunchInstancesWizardPage):
    def __init__(self, driver):
        self.locator = CELaunchInstancesWizardPageLocators
        super().__init__(driver)

    def fill_volume_info(self, volume_name, volume_size):
        self\
            .fill_form(volume_name, self.locator.VOlUME_NAME_TEXTBOX) \
            .click_button(self.locator.VOLUME_TYPE_LIST) \
            .choose_volume_type(self.locator.VOLUME_TYPE_LIST) \
            .fill_form(volume_size, self.locator.VOLUME_SIZE_TEXTBOX)
        return self

    def select_volume(self, volume_id):
        self.click_button(CELaunchInstancesWizardPageLocators.RADIO_BY_NAME(volume_id))
        return self

    def add_new_volume(self, volume_name, volume_size):
        # Click "Add new Volume" button
        self.click_button(self.locator.ADD_NEW_VOLUME_BTN)
        # Fill the form and select type of volume
        self.fill_volume_info(volume_name, volume_size)
        # Click on "Create" button on modal
        self.click_button(self.locator.CREATE_VOLUME_BTN)
        # Then the new volume is created
        self.check_element_existence(self.locator.CREATE_VOLUME_SUCCESS_MESSAGE)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.locator.CLOSE_MESSAGE_BTN))
        # Close popup message
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.locator.CLOSE_MESSAGE_BTN))
        self.click_button(self.locator.CLOSE_MESSAGE_BTN)


class SecurityGroupWizardPage(CELaunchInstancesWizardPage):
    def __init__(self, driver):
        self.locator = CELaunchInstancesWizardPageLocators
        super().__init__(driver)

    def fill_security_group_info(self, sg_name, sg_description):
        self\
            .fill_form(sg_name, self.locator.SG_NAME_TEXTBOX)\
            .fill_form(sg_description, self.locator.SG_DESCRIPTION_TEXTBOX)
        return self

    def create_new_security_group(self, sg_name, sg_description):
        # Click on "Create new SG radio"
        self.click_button(self.locator.CREATE_NEW_SG_RADIO)
        # Fill SG name and description
        self.fill_security_group_info(sg_name, sg_description)
        # Click on add SG button
        self.click_button(self.locator.ADD_SG_BTN)
        # Check if SG created successfully
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.locator.CREATE_SG_SUCCESS_MESSAGE))
        # Close popup message
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.locator.CLOSE_MESSAGE_BTN))
        self.click_button(self.locator.CLOSE_MESSAGE_BTN)

    def apply_sg_for_instance(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.locator.SG_APPLY_CHECKBOX))
        self.\
            click_button(self.locator.SG_APPLY_CHECKBOX)
        return self




class ReviewLaunchWizardPage(CELaunchInstancesWizardPage):
    def __init__(self, driver):
        self.locator = CELaunchInstancesWizardPageLocators
        super().__init__(driver)

    def show_password(self):
        self\
            .click_button(self.locator.SHOW_PASSWORD_BTN)
        return self

    def random_password(self):
        self\
            .click_button(self.locator.RANDOM_PASSWORD_BTN)
        return self

    def apply_password(self):
        self\
            .click_button(self.locator.APPLY_PASSWORD_BTN)
        return self

    def copy_password(self):
        self\
            .click_button(self.locator.COPY_PASSWORD_BTN)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.locator.CLOSE_MESSAGE_BTN))
        self.click_button(self.locator.CLOSE_MESSAGE_BTN)
        return self

    def check_instance_state(self, instance_id, state):
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(CELaunchInstancesWizardPageLocators.INSTANCE_STATE_BY_ID(instance_id), state))

    def launch_instance(self):
        self\
            .click_button(self.locator.LAUNCH_BTN)
        return self



