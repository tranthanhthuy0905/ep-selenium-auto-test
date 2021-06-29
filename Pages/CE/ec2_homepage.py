"""
Access CE page
"""

from Pages.base_page import BasePage
#from Pages.s3.s3_create_bucket_page import S3CreateBucketPage
from Configs import EC2_BASE_URL, EC2_USER_TOKEN
from Locators.ec2 import EC2PageLocators
from Pages.ec2.ec2_instances_page import EC2InstancesPage

class EC2HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver=driver, base_url=EC2_BASE_URL)
        self.driver.get(EC2_BASE_URL)
        self.authenticate(EC2_USER_TOKEN)

    # User selects "Instances => Instances" on left side menu
    def access_instance_page(self):
        ec2_instances_page = self \
            .click_button_and_return_page(EC2PageLocators.INSTANCES_SUBMENU_BTN, EC2InstancesPage(self.driver))
        return ec2_instances_page
