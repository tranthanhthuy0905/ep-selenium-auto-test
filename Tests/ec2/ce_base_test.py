from Configs.local import EC2_KEYPAIR_API_CLIENT_URL
from Tests.base_test import BaseTest
from Configs import EC2_INSTANCE_API_CLIENT_URL

class CEBaseTest(BaseTest):
    def delete_CE_instance(self):
        try:
            url = EC2_INSTANCE_API_CLIENT_URL + "destroy"
            params = {
                "id": self.service_slug
            }
            self._call_request_delete(url, params)

            url = EC2_KEYPAIR_API_CLIENT_URL + self.keypair_name
            self._call_request_delete(url, params)
        except Exception as e:
            print("Can't delete CE instance", str(e))

