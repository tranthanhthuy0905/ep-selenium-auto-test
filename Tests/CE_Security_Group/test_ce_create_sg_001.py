import os
import time
import unittest

import HtmlTestRunner

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
from Tests.CE.ce_base_test import CEBaseTest


class TestCreateSecurityGroup(CEBaseTest):

    def test_create_security_group(self):
        self.sg_home_page = SGHomePage(self.driver)
        self.sg_home_page.click_create_button()

        self.sg_create_page = SGCreatePage(self.driver)

        self.assertEqual(self.driver.current_url, self.sg_create_page.base_url)

        self.sg_create_page.fill_sg_information()
        self.sg_create_page.click_create_submit_button()

        sg_id = self.driver.current_url.split["/"][-1]
        self.sg_details_page = SGDetailsPage(self.driver, sg_id)
        self.sg_home_page.add_ingress_rule()
        # self.sg_home_page.add_egress_rull()

        #
        # self._created_sec_group_id = self.keep_trying(lambda: collapse_text_box.find_elements_by_tag_name('div')[2].text, unsatisfactory='')
        # self._created_sec_group_name = collapse_text_box.find_elements_by_tag_name('div')[6].text

    # def test_security_group_flow(self):
    #     try:
    #         self.test_create_security_group()
    #     except Exception as e:
    #         raise(e)
    #     finally:
    #         if self._created_sec_group_id:
    #             self.driver.quit()
    #             delete_security_group(self._created_sec_group_id)


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output=os.path.join(os.getcwd(), "Reports"))
    )
