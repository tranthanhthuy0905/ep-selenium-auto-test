'''
Scenario 4: Create Security Group with Protocol UDP
Given user just finished creating a security group
When user select Protocol to UDP in Ingress Rule, and fill in Start Port and End Port information, and click Add
Then a new udp rule is added
And user should see a new rule is added to the Ingress Rule table, with field Protocal is UDP
'''

import os
import time
import unittest

import HtmlTestRunner

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Locators.CE import CESecurityGroupLocators
from Pages.CE.security_group_page import SGHomePage, SGCreatePage, SGDetailsPage
from Tests_Dev.CE_Security_Group.sg_base_test import SGBaseTest
from Configs.TestData.CESecurityGroupTestData import CESecurityGroupTestData
from Configs import CE_SG_DETAILS_PAGE_URL



class TestCreateSgUdpProtocol(SGBaseTest):
    def test_create_sg_udp_protocol(self):
        '''
            User should be able to create a security group with UDP rule
        '''
        '''Given user just finished creating a security group'''
        sg_id, sg_name = self.create_security_group()
        self.sg_id = sg_id
        self.sg_details_page = SGDetailsPage(self.driver, sg_id)

        '''
            When user select Protocol to UDP in Ingress Rule, and fill in Start Port and End Port information, and click Add
        '''
        self.sg_details_page.fill_in_ingress_rule_info(CESecurityGroupTestData.VALID_PORTS_1[0], CESecurityGroupTestData.VALID_PORTS_1[1])
        self.sg_details_page.select_ingress_protocol(CESecurityGroupTestData.UDP_SELECTION_INDEX)
        self.sg_details_page.click_add_ingress()

        '''
            Then a new udp rule is added
            And user should see a new rule is added to the Ingress Rule table, with field Protocal is UDP
        '''
        self.sg_details_page.check_element_existence(CESecurityGroupLocators.INGRESS_RULE_ROW(
            protocol=CESecurityGroupTestData.UDP_VALUE_IN_TABLE,
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
