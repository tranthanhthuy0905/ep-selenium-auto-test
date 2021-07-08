
'''
Scenario 3: Create Key Pairs with incorrect format public key
	Given a certain user
	When user wants to create a keypair
	Then user selects "Create keypair" on the top right corner
	And user can see a modal to fill in the information of the key pair to create
	When the user fills in the "Name" box and enter "abcd" in public key _field
	And click the "OK" button
	Then user receives a warning
	And the keypair is not created
'''

from Pages.CE.keypair_page import CEKeypairPage
from Tests.CE.CE_Security_Group.sg_base_test import SGBaseTest
from Configs.TestData.CEKeypairTestData import CEKeypairTestData

class TestCreateKeyPairInvalidPublicKey(SGBaseTest):
	def test_create_keypair_with_invalid_public_key(self):
		self.keypair_homepage = CEKeypairPage(self.driver, authenticate=True)
		self.keypair_homepage.click_create_keypair()
		keypair_name = CEKeypairTestData.KEYPAIR_NAME
		self.keypair_homepage.fill_keypair_info(keypair_name, CEKeypairTestData.INVALID_PUBLIC_KEY_01)
		self.keypair_homepage.click_create_keypair_submit_button()
		
		self.assertTrue(
			self.keypair_homepage.check_alert_invalid_key_existence()
		)

		self.assertFalse(self.keypair_homepage.check_keypair_existence_in_table(keypair_name),
						 "The keypair should not have been created !!!!")