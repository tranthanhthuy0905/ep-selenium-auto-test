'''
Scenario 4: Create Key Pairs with already existed public key
	Given a certain user and at least one keypair is created
	When user wants to create a keypair
	Then user selects "Create keypair" on the top right corner
	And user can see a modal to fill in the information of the key pair to create
	When the user fills in the "Name" box and enter an already created in public key _field
	And click the "OK" button
	Then user receives a warning
	And the keypair is not created
'''

import time
from Pages.CE.keypair_page import CEKeypairPage
from Tests.CE.CE_Security_Group.sg_base_test import SGBaseTest
from Configs.TestData.CEKeypairTestData import CEKeypairTestData

class TestCreateKeyPairDuplicatedInfo(SGBaseTest):
    def test_create_keypair_duplicated_public_key(self):
        # Given a certain user and at least one keypair is created
        self.keypair_homepage = CEKeypairPage(self.driver, authenticate=True)
        keypair_name = CEKeypairTestData.KEYPAIR_NAME
        self.keypair_name = keypair_name
        public_key = CEKeypairTestData.VALID_PUBLIC_KEY_1 + str(time.time)[-5:]
        self.keypair_homepage.create_new_keypair(keypair_name, public_key)
        self.assertTrue(self.keypair_homepage.check_keypair_existence_in_table(keypair_name))

        # Then user selects "Create keypair" on the top right corner
	    # And user can see a modal to fill in the information of the key pair to create
	    # When the user fills in the "Name" box and enter an already created in public key _field
	    # And click the "OK" button

        keypair_name_2 = CEKeypairTestData.gen_new_keypair_name()
        self.keypair_homepage.create_new_keypair(keypair_name_2, public_key)

        # Then user receives a warning
        self.assertTrue(self.keypair_homepage.check_alert_public_key_existence())

        # And the keypair is not created
        self.assertFalse(self.keypair_homepage.check_keypair_existence_in_table(keypair_name_2))

    def test_create_keypair_duplicated_name(self):
        # Given a certain user and at least one keypair is created
        self.keypair_homepage = CEKeypairPage(self.driver, authenticate=True)
        keypair_name = CEKeypairTestData.KEYPAIR_NAME
        self.keypair_name = keypair_name
        public_key = CEKeypairTestData.VALID_PUBLIC_KEY_1 + str(time.time)[-5:]
        self.keypair_homepage.create_new_keypair(keypair_name, public_key)
        self.assertTrue(self.keypair_homepage.check_keypair_existence_in_table(keypair_name))

        # Then user selects "Create keypair" on the top right corner
        # And user can see a modal to fill in the information of the key pair to create
        # When the user fills in the "Name" box and enter an already created in public key _field
        # And click the "OK" button

        public_key_2 = CEKeypairTestData.VALID_PUBLIC_KEY_1 + str(time.time)[-5:]
        self.keypair_homepage.create_new_keypair(keypair_name, public_key_2)

        # Then user receives a warning
        self.assertTrue(self.keypair_homepage.check_alert_public_key_existence())

        # And the keypair is not created
        self.assertFalse(self.keypair_homepage.check_keypair_existence_in_table(keypair_name))
