from Pages.CE.ec2_create_volume_page import EC2CreateVolumePage
from Locators.CE import EC2InstancePageLocators, EC2VolumnePageLocators
from Pages.base_page import BasePage
from Pages.CE.ec2_launch_instances_wizard_page import EC2LaunchInstancesWizardPage
from Configs import EC2_VOLUME_URL


class EC2VolumePage(BasePage):
    def __init__(self, driver):
        self.locator = EC2VolumnePageLocators
        super(EC2VolumePage, self).__init__(driver, EC2_VOLUME_URL)


    def access_create_volume_page(self):
        ec2_create_volume_page = self.click_button_and_return_page(self.locator.CREATE_VOLUME_BTN, EC2CreateVolumePage(self.driver))
        return ec2_create_volume_page


    def change_instance_states(self, state_button, confirm_button, message):
        self.click_button(self.locator.RADIO_BTN)\
            .click_button(self.locator.INSTANCE_STATE_BTN)\
            .click_button(state_button)\
            .wait_and_click_button(confirm_button)
        if message:
            self.check_element_existence(message)
        return self


