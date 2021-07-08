'''
Scenario 6: Create Security Group with Protocal All
Given user just finished creating a security group
When user select Protocol to "all" in Ingress Rule, and fill in Start Port and End Port information, and click Add
Then a new "all" rule is added
And user should see a new rule is added to the Ingress Rule table, with field Protocal is "All"
'''

import os
import time
import unittest

import HtmlTestRunner

from Locators.CE import CESecurityGroupLocators
from Pages.CE.security_group_page import SGDetailsPage
from Tests.CE.CE_Security_Group.sg_base_test import SGBaseTest
from Configs.TestData.CESecurityGroupTestData import CESecurityGroupTestData


class TestCreateSgAllProtocol(SGBaseTest):
    def test_create_sg_all_protocol(self):
        '''
            User should be able to create a security group with ICMP rule
        '''
        '''Given user just finished creating a security group'''
        sg_id, sg_name = self.create_security_group()
        self.sg_id = sg_id
        self.sg_details_page = SGDetailsPage(self.driver, sg_id)

        '''
            When user select Protocol to "all" in Ingress Rule, and fill in Start Port and End Port information, and click Add
        '''
        self.sg_details_page.select_ingress_protocol(CESecurityGroupTestData.ALL_SELECTION_INDEX)
        self.sg_details_page.click_add_ingress()

        '''
            Then a new icmp rule is added
            And user should see a new rule is added to the Ingress Rule table, with field Protocol is All
        '''
        self.sg_details_page.check_element_existence(CESecurityGroupLocators.INGRESS_RULE_ROW(
            protocol=CESecurityGroupTestData.ALL_VALUE_IN_TABLE,
            start_port=CESecurityGroupTestData.VALID_PORTS_1[0],
            end_port=CESecurityGroupTestData.VALID_PORTS_1[1],
            cidr=CESecurityGroupTestData.DEFAULT_CIDR
        ))

        time.sleep(5)



if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
