from Tests.base_test import BaseTest
from Configs import *

class CEBaseTest(BaseTest):
    def delete_CE_instance(self):
        try:
            url = CE_INSTANCE_API_CLIENT_URL + "destroy"
            params = {
                "id": self.service_slug
            }
            self._call_request_delete(url, params, CE_USER_TOKEN)

        except Exception as e:
            print("Can't delete CE instance", str(e))


    def delete_CE_volume_by_id(self, volume_id):
        try:
            url = CE_VOLUME_API_CLIENT_URL + "destroy"
            params = {
                "id": volume_id,
                "expunge" : True
            }
            self._call_request_delete(url, params, CE_USER_TOKEN)
        except Exception as e:
            print("Can't delete CE volume", str(e))

    def delete_CE_keypair_by_name(self, keypair_name):
        try:
            url = CE_KEYPAIR_API_CLIENT_URL + keypair_name
            self._call_request_delete(url, {}, CE_USER_TOKEN)
        except Exception as e:
            print("Can't delete CE keypair", str(e))

    def delete_CE_sg_by_id(self, sg_id):
        try:
            url = CE_SECURITY_GROUP_API_CLIENT_URL
            params = {
                "id": sg_id,
            }
            self._call_request_delete(url, params, CE_USER_TOKEN)
        except Exception as e:
            print("Can't delete CE security group", str(e))

