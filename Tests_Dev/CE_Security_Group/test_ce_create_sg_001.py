import os
import unittest

import HtmlTestRunner

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
Scenario 1: Create Security Group With Simple Flow
Given a certain user
When the user click the "Create Security Group" button
Then the user will be redirected to a new page
And the user can see a form that allows to enter "Security group name" and "Description"
When the user enters information in the "Security group name" box
Then the user can see a preview of the name of the Security Group
When the user clicks the "Create Security Group" button
Then the user will be redirected to a new page
And user can see details "Security Group", "Ingress Rule", "Egress Rule"
When user wants to set ingress rule
Then the user will have to select Protocol, enter the start port, end port, CIDR
When the user clicks the add button
Then the user can see a message appear with the content "Added Ingress rule successfully."
And the user can see the list of ingress rules
When user wants to set egress rule
Then the user will have to select Protocol, enter the start port, end port, CIDR
When the user clicks the add button
Then the user can see a message appear with the content "Added Egress rule successfully."
And the user can see the list of egress rules
'''

from Pages.CE.security_group_page import SGHomePage, SGCreatePage, SGDetailsPage
from Tests_Dev.CE import SGBaseTest
from Configs.TestData.CESecurityGroupTestData import CESecurityGroupTestData
from Configs import CE_SG_DETAILS_PAGE_URL


class TestCreateSecurityGroup(SGBaseTest):

    def test_create_security_group(self):

        self.sg_home_page = SGHomePage(self.driver)


        '''
        When the user click the "Create Security Group" button
        Then the user will be redirected to a new page
        '''
        self.sg_home_page.click_create_button()
        self.sg_create_page = SGCreatePage(self.driver)

        self.assertEqual(self.driver.current_url, self.sg_create_page.base_url)


        '''
        And the user can see a form that allows to enter "Security group name" and "Description"
        When the user enters information in the "Security group name" box
        Then the user can see a preview of the name of the Security Group
        When the user clicks the "Create Security Group" button
        Then the user will be redirected to a new page
        '''
        self.sg_create_page.fill_sg_information()
        self.sg_create_page.click_create_submit_button()

        '''
        When user wants to set ingress rule
        Then the user will have to select Protocol, enter the start port, end port, CIDR
        When the user clicks the add button
        Then the user can see a message appear with the content "Added Ingress rule successfully."
        And the user can see the list of ingress rules
        When user wants to set egress rule
        Then the user will have to select Protocol, enter the start port, end port, CIDR
        When the user clicks the add button
        Then the user can see a message appear with the content "Added Egress rule successfully."
        And the user can see the list of egress rules
        '''

        WebDriverWait(self.driver, 10).until(
            EC.url_matches(CE_SG_DETAILS_PAGE_URL.format(sg_id=CESecurityGroupTestData.SG_ID_REGEX)),
            f"Current URL does not match SG details URL pattern"
        )
        self.sg_id = self.driver.current_url.split("/")[-1]
        self.sg_details_page = SGDetailsPage(self.driver, self.sg_id)
        self.sg_details_page.add_ingress_rule(CESecurityGroupTestData.VALID_PORTS_1[0], CESecurityGroupTestData.VALID_PORTS_1[1])
  

if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
