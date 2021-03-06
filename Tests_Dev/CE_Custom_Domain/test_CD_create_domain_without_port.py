'''
Scenario 4. Create a custom domain without filling port	
	When user want to create a domain without filling port
	Then user access Custom-Domain page
	When user clicks on "Create domain" button on the top right corner 
	Then user can see a pop-up "Create New Custom Domain" box
	When user selects Https:// protocol
	And fills in Domain name textbox
	And selects Instance in IPAddress list
	Add deletes port textbox value
	And clicks on Test Connection
	Then the connection result is displayed as FAILED icon
	When user clicks on "Create" button on the bottom right
	User can see the "Failed" notification
'''


import os
import unittest

import HtmlTestRunner
from Configs.TestData.CustomDomainTestData import CustomDomainTestData
from Tests_Dev.CE_Custom_Domain.cd_base_test import CDBaseTest
from Pages.CD.custom_domain_page import CustomDomainPage
from Locators.CD import CustomDomainPageLocators
import time


class TestCustomDomain04(CDBaseTest):
    def test_create_doamin_without_port(self):
        """
            TEST CASE: Custom Domain should be created successfully without filling port	
        """
        # Access Custom-Domain page
        self.custom_domain_page = CustomDomainPage(self.driver)

        # Click on "Create domain" button on the top right corner
        domain_name = CustomDomainTestData.gen_domain_name()
        self.custom_domain_page.create_custom_domain(
            protocol_locator=CustomDomainPageLocators.HTTPS_PROTOCOL,
            domain_name=domain_name,
            port=" ",
            instance_info=CustomDomainTestData.INSTANCE_INFO
        )
        self.custom_domain_page.click_test_connection()
        # The connection result is displayed as OK icon
        self.custom_domain_page.check_connection_is_fail()
        # Click on "Create" button on the bottom right
        self.custom_domain_page.click_create_btn()
        # Failed to create domain
        if (not self.custom_domain_page.check_action_fail()):
            self.domain_id = self.custom_domain_page.get_domain_id(domain_name)
    

    

# python3 -m unittest Tests_Dev.CD.test_CD_create_domain_without_port -v


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )