from Configs.local import EC2_VOLUME_URL
from Pages.CE.ec2_volume_page import EC2VolumePage
from Locators.CE import EC2CreateVolumnePageLocators, EC2VolumnePageLocators
from Pages.base_page import BasePage
from Configs import EC2_BASE_URL


class EC2VolumePage(BasePage):
    def __init__(self, driver):
        self.locator = EC2VolumnePageLocators
        super(EC2VolumePage, self).__init__(driver, EC2_VOLUME_URL)