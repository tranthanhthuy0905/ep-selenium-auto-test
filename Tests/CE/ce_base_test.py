from Tests.base_test import BaseTest
from Configs import *

class CEBaseTest(BaseTest):
    def delete_CE_instance(self):
        try:
            url = CE_INSTANCE_API_CLIENT_URL + "destroy"
            params = {
                "id": self.service_slug
            }
            self._call_request_delete(url, params)

            url = CE_VOLUME_API_CLIENT_URL + "destroy"
            params = {
                "id": self.volume_id,
                "expunge" : True
            }
            self._call_request_delete(url, params)
            
            url = CE_KEYPAIR_API_CLIENT_URL + self.keypair_name
            self._call_request_delete(url, params)
        except Exception as e:
            print("Can't delete CE instance", str(e))

