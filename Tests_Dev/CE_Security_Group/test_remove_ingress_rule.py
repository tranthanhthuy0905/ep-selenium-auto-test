'''
Given user just finished adding an Egress rule and the rule is displayed in the Egress Rule table
When user clicks x button at the last column of the rule information
Then there is a popup wich confirm that the user wants to delete the rule
When user clicks Delete button
Then the rule is successfully deleted
And there  is a popup notifying user the action is succeed
'''

from Pages.CE.security_group_page import SGDetailsPage
from Tests.CE.CE_Security_Group import SGBaseTest
from Locators.CE import CESecurityGroupLocators
from Configs.TestData.CESecurityGroupTestData import CESecurityGroupTestData


class TestRemoveIngressRule(SGBaseTest):
    def test_removing_ingress_rule(self):
        sg_id, sg_name = self.create_security_group()
        self.sg_id = sg_id
        '''
            Given user just finished adding an Egress rule and the rule is displayed in the Egress Rule table
            When user clicks x button at the last column of the rule information
            Then there is a popup wich confirm that the user wants to delete the rule
        '''
        self.sg_details_page = SGDetailsPage(self.driver, sg_id)
        self.sg_details_page.add_ingress_rule(CESecurityGroupTestData.VALID_PORTS_1[0], CESecurityGroupTestData.VALID_PORTS_1[1])
        self.sg_details_page.click_first_remove_button()
        '''
            When user clicks Delete button
            Then the rule is successfully deleted
            And there  is a popup notifying user the action is succeed
        '''
        self.assertTrue(
            self.sg_details_page.check_element_existence(CESecurityGroupLocators.CONFIRM_DELETE_RULE_BUTTON),
            "CONFIRM DELETE BUTTON NOT EXISTS"
            )
        self.sg_details_page.click_confirm_remove_button()