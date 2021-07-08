'''
Scenario 1: Create Key pairs with Public Key
	Given a certain user
	When user wants to create a keypair
	Then user selects "Create keypair" on the top right corner
	And user can see a modal to fill in the information of the key pair to create
	When user enter all the information including "Name" and "Public key"
	And click the "OK" button
	Then the keypair is successfully created
	And user should see the created keypair appear on the homepage
'''

import time
from Pages.CE.keypair_page import CEKeypairPage
from Tests.CE.CE_Security_Group.sg_base_test import SGBaseTest
from Configs.TestData.CEKeypairTestData import CEKeypairTestData

class TestCreateKeyPairWithPublicKey(SGBaseTest):
    def test_create_keypair_with_public_key(self):

        # Given a certain user
        self.keypair_homepage = CEKeypairPage(self.driver, authenticate=True)

        # When user wants to create a keypair
	    # Then user selects "Create keypair" on the top right corner
        self.keypair_homepage.click_create_keypair()

        keypair_name = CEKeypairTestData.KEYPAIR_NAME

        # When user enter all the information including "Name" and "Public key"
        self.keypair_homepage.fill_keypair_info(keypair_name, CEKeypairTestData.VALID_PUBLIC_KEY_1 + str(time.time)[-5:])

        # And click the "OK" button
        self.keypair_homepage.click_create_keypair_submit_button()

        # Then the keypair is successfully created
        # And user should see the created keypair appear on the homepage
        self.assertTrue(self.keypair_homepage.check_keypair_existence_in_table(keypair_name))
