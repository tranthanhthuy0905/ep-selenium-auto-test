'''
Scenario 5: Create Security Group with Protocol ICMP
Given user just finished creating a security group
When user select Protocol to IMCP in Ingress Rule, and fill in IMCP Type = 1 and IMCP Code = 3 information, and click Add
Then a new icmp rule is added
And user should see a new rule is added to the Ingress Rule table, with 
'''

import os
import time
import unittest

import HtmlTestRunner

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Locators.CE import CESecurityGroupLocators
from Pages.CE.security_group_page import SGHomePage, SGCreatePage, SGDetailsPage
from Tests.CE_Security_Group.sg_base_test import SGBaseTest
from Configs.TestData.CESecurityGroupTestData import CESecurityGroupTestData
from Configs import CE_SG_DETAILS_PAGE_URL



class TestCreateSgICMPProtocol(SGBaseTest):
    def test_create_sg_icmp_protocol(self):
        '''
            User should be able to create a security group with ICMP rule
        '''
        '''Given user just finished creating a security group'''
        sg_id, sg_name = self.create_security_group()
        self.sg_id = sg_id
        self.sg_details_page = SGDetailsPage(self.driver, sg_id)

        '''
            When user select Protocol to ICMP in Ingress Rule, and fill in Start Port and End Port information, and click Add
        '''
        self.sg_details_page.select_ingress_protocol(CESecurityGroupTestData.ICMP_SELECTION_INDEX)
        self.sg_details_page.fill_in_icmp_info(CESecurityGroupTestData.VALID_ICMP_1[0], CESecurityGroupTestData.VALID_ICMP_1[1])
        self.sg_details_page.click_add_ingress()

        '''
            Then a new icmp rule is added
            And user should see a new rule is added to the Ingress Rule table, with field Protocal is ICMP
        '''
        self.sg_details_page.check_element_existence(CESecurityGroupLocators.INGRESS_RULE_ICMP_ROW(
            protocol=CESecurityGroupTestData.ICMP_VALUE_IN_TABLE,
            icmp_type=CESecurityGroupTestData.VALID_ICMP_1[0],
            icmp_code=CESecurityGroupTestData.VALID_ICMP_1[1],
            cidr=CESecurityGroupTestData.DEFAULT_CIDR
        ))

        time.sleep(5)



if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
