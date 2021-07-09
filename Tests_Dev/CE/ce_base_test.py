from Configs.TestData.CEInstanceTestData import CEInstanceTestData
from Pages.CE.launch_instances_wizard_page import ConfigureInstanceWizardPage, ReviewLaunchWizardPage
from Pages.CE.instances_page import CEInstancesPage
from Pages.CE.homepage import CEHomePage
from Tests_Dev.base_test import BaseTest
from Configs import *

class CEBaseTest(BaseTest):
    def clear_test_instances(self):
        if hasattr(self, 'volume_id'):
            self.delete_CE_volume_by_id(self.volume_id)
            print("Volume has been deleted")

        if hasattr(self, 'instance_id'):
            if hasattr(self, 'sg_id') or hasattr(self, 'list_sg_id'):
                self.remove_CE_sg_in_instance(self.instance_id)
            self.delete_CE_instance_by_id(self.instance_id)
            print("Instance has been deleted")

        if hasattr(self, 'keypair_name'):
            self.delete_CE_keypair_by_name(self.keypair_name)
            print("Keypair has been deleted")

        if hasattr(self, 'sg_id'):
            self.delete_CE_sg_by_id(self.sg_id)
            print("Security group has been deleted")

        if hasattr(self, 'snapshot_id'):
            self.delete_CE_snapshot_by_id(self.snapshot_id)
            print("Snapshot volume has been deleted")
            
        if hasattr(self, 'list_sg_id'):
            for sg_id in self.list_sg_id:
                self.delete_CE_sg_by_id(sg_id)
            print("Security groups have been deleted")
        


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
                "expunge" : 'true'
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
            url = CE_SG_API_CLIENT_URL
            params = {
                "id": sg_id,
            }
            self._call_request_delete(url, params, CE_USER_TOKEN)
        except Exception as e:
            print("Can't delete CE security group", str(e))


    def delete_CE_snapshot_by_id(self, snapshot_id):
        try:
            url = CE_SNAPSHOT_API_CLIENT_URL
            params = {
                "id": snapshot_id,
            }
            self._call_request_delete(url, params, CE_USER_TOKEN)
        except Exception as e:
            print("Can't delete CE snapshot volume", str(e))


    def passing_first_two_step(self):
        self.CE_homepage = CEHomePage(self.driver)
        self.CE_homepage.access_instances_page()

        # When user selects "Instances => Instances" on left side menu
        self.instances_page = CEInstancesPage(self.driver)

        # Passing step 1 (Choose MI) and step 2 (Instance Type)
        self.instances_page.choose_MI_N_Instance_Type()
        self.configure_instance_wizard = ConfigureInstanceWizardPage(self.driver)
        # set instance name
        instance_name = CEInstanceTestData.gen_instance_name()
        self.configure_instance_wizard.fill_instance_name(instance_name)
        return instance_name

    def create_simple_instance(self):
        instance_name = self.passing_first_two_step()
        self.review_launch_wizard = ReviewLaunchWizardPage(self.driver)
        self.review_launch_wizard.click_review_and_launch_btn()
        self.review_launch_wizard.apply_default_password()
        # Launch instance
        self.review_launch_wizard.click_launch_instance()

        self.instances_page.check_if_instance_launched_successfully()
        return instance_name


