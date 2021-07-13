from Tests_Dev.base_test import BaseTest
from Configs import *

class CDBaseTest(BaseTest):
    def clear_test_instances(self):
        if hasattr(self, 'domain_id'):
            self.delete_domain_by_id(self.domain_id)
            print("Domain has been deleted")

    def delete_domain_by_id(self, _domain_id):
        try:
            url = CUSTOM_DOMAIN_API_CLIENT_URL + _domain_id
            params = {}
            self._call_request_delete(url, params, CUSTOM_DOMAIN_USER_TOKEN)
        except Exception as e:
            print("Can't delete custom domain", str(e))
