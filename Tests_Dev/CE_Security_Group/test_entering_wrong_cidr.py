'''
Given user just finished creating a security group
When user enter any start port, end port, and CIDR is 0.0.0.0
Then there will be warning at the textbox
And user cannot add Ingress Rule
'''

from Pages.CE.security_group_page import SGDetailsPage
from Tests.CE.CE_Security_Group.sg_base_test import SGBaseTest
from Locators.CE import CESecurityGroupLocators
from Configs.TestData.CESecurityGroupTestData import CESecurityGroupTestData


class TestEnteringWrongCidr(SGBaseTest):
    def test_entering_wrong_format_cidr_001(self):
        sg_id, sg_name = self.create_security_group()
        self.sg_id = sg_id
        self.sg_details_page = SGDetailsPage(self.driver, sg_id)
        self.sg_details_page.access_page()

        """
            Given user just finished creating a security group
            When user enter any start port, end port, and CIDR is 0.0.0.0
        """
        self.sg_details_page.fill_in_ingress_rule_info(*CESecurityGroupTestData.VALID_PORTS_1)
        self.sg_details_page.add_ingress_cidr(CESecurityGroupTestData.INVALID_CIDR_1)

        # TODO: UI NOT IMPLEMENTED - PENDING
        '''
            Then there will be warning at the textbox
            And user cannot add Ingress Rule
        '''
        self.assertTrue(
            self.sg_details_page.check_element_existence(CESecurityGroupLocators.INVALID_CIDR_ALERT), 
            "INVALID CIDR ALERT NOT FOUND"
            )