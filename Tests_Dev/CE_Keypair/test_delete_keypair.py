'''
Scenario 6: Delete a keypair
	Given a certain user and at least one keypair is created
	When user tick radio button of a keypair in a menu
	The keypair is selected
	And the row of keypair is highlighted
	When user click Actions button
	Then a list of options dropped down, including "Delete Keypair"
	When user clicks "Delete Keypair"
	A confirmation dialog pops up
	When user clicks "Delete"
	Then the keypair is deleted
	And user should see it disappear from the menu table
'''

import time
from Pages.CE.keypair_page import CEKeypairPage
from Tests.CE.CE_Security_Group.sg_base_test import SGBaseTest
from Configs.TestData.CEKeypairTestData import CEKeypairTestData

class TestDeleteKeypair(SGBaseTest):
    def test_delete_keypair(self):

        # Given a certain user
        self.keypair_homepage = CEKeypairPage(self.driver, authenticate=True)
        keypair_name = CEKeypairTestData.KEYPAIR_NAME
        self.keypair_name = keypair_name
        public_key = CEKeypairTestData.VALID_PUBLIC_KEY_1 + str(time.time)[-5:]
        self.keypair_homepage.create_new_keypair(keypair_name, public_key)
        self.assertTrue(self.keypair_homepage.check_keypair_existence_in_table(keypair_name))

        # Then the keypair is successfully created
        # And user should see the created keypair appear on the homepage
        self.assertTrue(self.keypair_homepage.check_keypair_existence_in_table(keypair_name))

        # The keypair is selected
	    # And the row of keypair is highlighted
        self.keypair_homepage.select_keypair_by_name(keypair_name)
        # When user click Actions button
        self.keypair_homepage.click_action()

        # Then a list of options dropped down, including "Delete Keypair"
        self.keypair_homepage.click_delete()
        # When user clicks "Delete"
        self.keypair_homepage.click_confirm_delete()

        # Then the keypair is deleted
	    # And user should see it disappear from the menu table
        self.assertFalse(self.keypair_homepage.check_keypair_existence_in_table(keypair_name))