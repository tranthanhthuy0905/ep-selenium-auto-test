'''
Scenario 5. Delete a custom domain	
	Given a custom domain
	When user want to delete that custom domain
	Then user access Custom-Domain page
	When user selects that domain in Domains List
	User should see the infomation of that domain
	When user clicks on Actions button on the top right corner
	Then user should see the Delete button in the drop-down
	When user clicks on Delete button 
	Then user should see the "Delete the domain" confirm modal
	When user clicks on Delete button on the bottom right corner
	Then the domain should be deleted successfully
	And the domain should disappear from Domains List
'''


import os
import unittest

import HtmlTestRunner
from Configs.TestData.CustomDomainTestData import CustomDomainTestData
from Tests_Dev.CE_Custom_Domain.cd_base_test import CDBaseTest
from Pages.CD.custom_domain_page import CustomDomainPage
from Locators.CD import CustomDomainPageLocators
import time


class TestCustomDomain05(CDBaseTest):
    def test_delete_domain(self):
        """
            TEST CASE: Custom Domain should be deleted successfully
        """
        # Access Custom-Domain page
        self.custom_domain_page = CustomDomainPage(self.driver)

        # Click on "Create domain" button on the top right corner
        self.custom_domain_page.click_create_domain_btn()
        # Select Http:// protocol
        self.custom_domain_page.choose_protocol(CustomDomainPageLocators.HTTP_PROTOCOL)
        # Fill in Domain name textbox
        domain_name = CustomDomainTestData.gen_domain_name()
        self.custom_domain_page.fill_domain_name(domain_name)
        # Fill in port textbox
        self.custom_domain_page.fill_port(CustomDomainTestData.HTTP_PORT)
        # Select Instance in IPAddress list
        self.custom_domain_page.choose_instance(CustomDomainTestData.INSTANCE_INFO)
        # Click on Test Connection
        self.custom_domain_page.click_test_connection()
        # The connection result is displayed as OK icon
        self.custom_domain_page.check_connection_is_success()
        # Click on "Create" button on the bottom right
        self.custom_domain_page.click_create_btn()
       
        # Check if the new domain is created successfully
        if (self.custom_domain_page.check_if_created_domain_successfully(domain_name)):
            self.domain_id = self.custom_domain_page.get_domain_id(domain_name)
            # delete domain
            self.custom_domain_page.delete_domain(self.domain_id)
            # if domain deleted successfully, delete the domain for preventing auto clear test data
            if(self.custom_domain_page.check_if_deleted_domain_successfully):
                if (hasattr(self, "domain_id")):
                    delattr(self, "domain_id")




        

    

# python3 -m unittest Tests_Dev.CD.test_CD_delete_domain -v


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )