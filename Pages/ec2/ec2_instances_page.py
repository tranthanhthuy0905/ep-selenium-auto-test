from Locators.ec2 import EC2InstancePageLocators
from Pages.base_page import BasePage
from Pages.ec2.ec2_launch_instances_wizard_page import EC2LaunchInstancesWizardPage
from Configs import EC2_INSTANCE_URL


class EC2InstancesPage(BasePage):
    def __init__(self, driver):
        self.locator = EC2InstancePageLocators
        super(EC2InstancesPage, self).__init__(driver, EC2_INSTANCE_URL)

    def access_launch_instances_wizard_page(self):
        ec2_launch_instances_wizard_page = self.click_button_and_return_page(self.locator.LAUNCH_INSTANCES_BTN, EC2LaunchInstancesWizardPage(self.driver))
        return ec2_launch_instances_wizard_page

    def change_instance_states(self, state_button, confirm_button, message):
        self.click_button(self.locator.RADIO_BTN)\
            .click_button(self.locator.INSTANCE_STATE_BTN)\
            .click_button(state_button)\
            .wait_and_click_button(confirm_button)
        if message:
            self.check_element_existence(message)
        return self


