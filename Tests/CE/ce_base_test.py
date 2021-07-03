from Tests.base_test import BaseTest
from Configs import *

class CEBaseTest(BaseTest):
    def clear_test_instances(self):
        if hasattr(self, 'volume_id'):
            self.delete_CE_volume_by_id(self.volume_id)
            print("Volume has been deleted")
        if hasattr(self, 'instance_id'):
            self.remove_CE_sg_in_instance(self.instance_id)
            self.delete_CE_instance_by_id(self.instance_id)
            print("Instance has been deleted")
        if hasattr(self, 'keypair_name'):
            self.delete_CE_keypair_by_name(self.keypair_name)
            print("Keypair has been deleted")
        if hasattr(self, 'sg_id'):
            self.delete_CE_sg_by_id(self.sg_id)
            print("Security group has been deleted")


    def delete_CE_instance(self):
        try:
            url = CE_INSTANCE_API_CLIENT_URL + "destroy"
            params = {
                "id": self.service_slug
            }
            self._call_request_delete(url, params, CE_USER_TOKEN)

        except Exception as e:
            print("Can't delete CE instance", str(e))
    
    def change_CE_instance_status(self, instance_id, instance_status):
        try:
            url = CE_INSTANCE_API_CLIENT_URL + "changeStatus"
            jsonBody = {
                "id": instance_id,
                "status": instance_status
            }
            self._call_request_post(url, jsonBody, CE_USER_TOKEN)
        except Exception as e:
            print("Can't change CE instance status", str(e))

    def remove_CE_sg_in_instance(self, instance_id):
        try:
            url = CE_INSTANCE_API_CLIENT_URL
            jsonBody = {
                "id": instance_id,
                "data": ""
            }
            self._call_request_put(url, jsonBody, CE_USER_TOKEN)

        except Exception as e:
            print("Can't delete CE instance", str(e))

    def detach_CE_volume_by_id(self, volume_id):
        try:
            url = CE_VOLUME_API_CLIENT_URL + "detach"
            jsonBody = {
                "id": volume_id
            }
            self._call_request_post(url, jsonBody, CE_USER_TOKEN)

        except Exception as e:
            print("Can't delete CE instance", str(e))

    def delete_CE_instance_by_id(self, instance_id):
        try:
            url = CE_INSTANCE_API_CLIENT_URL + "destroy"
            params = {
                "id": instance_id
            }
            # self.remove_CE_sg_in_instance(instance_id)
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
            self.detach_CE_volume_by_id(volume_id)
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

