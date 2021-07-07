'''
Scenario 7: Create Security Group without entering Start Port or End Port
	Given user just finished creating a security group
	When user fill in any information except Start Port or and Port
	And user clicks "Add"
	Then user receives a textbox warning
	And the new rule is not added

Scenario 8: Create Security Group with Start Port is greater than End Port (failing)
	Given user just finished creating a security group
	When user fill in Start port is 5555 and Endport is 4444
	And user clicks "Add"
	Then user receives a textbox warning
	And the new rule is not added
'''

import os
import time
import unittest

import HtmlTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Locators.CE import CESecurityGroupLocators
from Pages.CE.security_group_page import SGDetailsPage
from Tests.CE.CE_Security_Group.sg_base_test import SGBaseTest
from Configs.TestData.CESecurityGroupTestData import CESecurityGroupTestData


class TestCreateSGInvalidPort(SGBaseTest):
    def test_create_sg_without_entering_ports(self):
        '''
            User should not be able to create a security group without entering port
        '''
        '''Given user just finished creating a security group'''
        sg_id, sg_name = self.create_security_group()
        self.sg_id = sg_id
        self.sg_details_page = SGDetailsPage(self.driver, sg_id)
        self.sg_details_page.access_page()

        '''
            When user fill in any information except Start Port or and Port
            And user clicks "Add"
        '''
        self.sg_details_page.select_ingress_protocol(CESecurityGroupTestData.ICMP_SELECTION_INDEX)
        self.sg_details_page.click_add_ingress()

        '''
            Then user receives a textbox warning
	        And the new rule is not added
        '''
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(CESecurityGroupLocators.IMCP_TYPE_REQUIRED_ALERT)
        )
        self.assertTrue(
            self.sg_details_page.check_element_existence(CESecurityGroupLocators.IMCP_TYPE_REQUIRED_ALERT)
        )
        self.assertTrue(
            self.sg_details_page.check_element_existence(CESecurityGroupLocators.IMCP_CODE_REQUIRED_ALERT)
        )

    def _test_create_sg_entering_endport_greater_than_startport(self):
        '''
            User should not be able to create a security group entering endport port greater than startport
        '''
        '''Given user just finished creating a security group'''
        sg_id, sg_name = self.create_security_group()
        self.sg_id = sg_id
        self.sg_details_page = SGDetailsPage(self.driver, sg_id)
        self.sg_details_page.access_page()

        '''
            When user select Protocol to UDP in Ingress Rule, and fill in Start Port and End Port information, and click Add
        '''
        self.sg_details_page.fill_in_ingress_rule_info(CESecurityGroupTestData.INVALID_PORTS_1[0],
                                                       CESecurityGroupTestData.INVALID_PORTS_1[1])
        self.sg_details_page.click_add_ingress()

        '''
            Then user receives a textbox warning
            And the new rule is not added
        '''

        # UI NOT COMPLETED

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(CESecurityGroupLocators.INVALID_START_PORT_ALERT)
        )
        self.assertTrue(
            self.sg_details_page.check_element_existence(CESecurityGroupLocators.INVALID_START_PORT_ALERT)
        )
        self.assertTrue(
            self.sg_details_page.check_element_existence(CESecurityGroupLocators.INVALID_END_PORT_ALERT)
        )

        self.assertFalse(self.sg_details_page.check_element_existence(CESecurityGroupLocators.INGRESS_RULE_ROW(
            protocol=CESecurityGroupTestData.TCP_VALUE_IN_TABLE,
            start_port=CESecurityGroupTestData.INVALID_PORTS_1[0],
            end_port=CESecurityGroupTestData.INVALID_PORTS_1[1],
            cidr=CESecurityGroupTestData.DEFAULT_CIDR
        )))


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
