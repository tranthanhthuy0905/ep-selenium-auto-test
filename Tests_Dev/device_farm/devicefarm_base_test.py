from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tests_Dev.base_test import BaseTest
from Configs import DEVICE_FARM_BASE_URL, DEVICE_FARM_API_PROJECT, DEVICE_FARM_USER_TOKEN, DEVICE_FARM_API_SESSION
from Pages.device_farm.devicefarm_homepage import DEVICE_FARM_HomePage
from Pages.device_farm.devicefarm_create_project_page import DEVICE_FARM_CreateProjectPage
from Configs.TestData.DeviceFarmTestData import DEVICE_FARM_TestData

class DEVICE_FARM_BaseTest(BaseTest):
    def _call_api_create_project(self, project_name):
        try:
            url = DEVICE_FARM_API_PROJECT
            body = {
                "name": project_name
            }
            self._call_request_post(url, body, DEVICE_FARM_USER_TOKEN)
        except Exception as e:
            logging.error("Can't create device farm project;", str(e))

    def _call_api_get_info_project(self):
        try:
            url = DEVICE_FARM_API_PROJECT
            params = {}
            project_info = self._call_request_get(url, params, DEVICE_FARM_USER_TOKEN)
            print(project_info)
            return project_info
        except Exception as e:
            logging.error("Can't get device farm project;", str(e))    


    def _call_api_delete_project(self):
        project_info = self._call_api_get_info_project()
        project_id = project_info[0].get('_id')
        print('project_id', project_id)
        try:
            url = DEVICE_FARM_API_PROJECT + '/' + project_id
            params = {}
            self._call_request_delete(url, params, DEVICE_FARM_USER_TOKEN)
        except Exception as e:
            logging.error("Can't delete device farm project;", str(e))

    def create_df_project(self):
        self.df_homepage = DEVICE_FARM_HomePage(self.driver)
        self.df_homepage.click_create_project()
        self.df_create_project_page = DEVICE_FARM_CreateProjectPage(self.driver)
        project_name = self.df_create_project_page.fill_project_create_information()
        self.service_slug = project_name
        self.df_create_project_page.click_create_project_submit_button()
        self.driver.implicitly_wait(10)
        return project_name

    def _call_api_create_session(self, groupId, serial):
        try:
            url = DEVICE_FARM_API_SESSION
            body = {
                "groupId": groupId,
                "projectId": groupId,
                "serial": serial,
                "sessionName": DEVICE_FARM_TestData.SESSION_NAME
            }
            self._call_request_post(url, body, DEVICE_FARM_USER_TOKEN)
        except Exception as e:
            logging.error("Can't create device farm session;", str(e))

    def _call_api_stop_session(self, serial, sessionId):
        try:
            url = DEVICE_FARM_API_SESSION + '/' + serial
            params = {
                "sessionId": sessionId
            }
            self._call_request_delete(url, params, DEVICE_FARM_USER_TOKEN)
        except Exception as e:
            logging.error("Can't delete device farm session;", str(e))

    def _call_api_get_info_session(self, groupId):
        try:
            url = DEVICE_FARM_API_SESSION
            params = {
                "groupId": groupId
            }
            session_info = self._call_request_get(url, params, DEVICE_FARM_USER_TOKEN)
            print(session_info)
            return session_info
        except Exception as e:
            logging.error("Can't get device farm project;", str(e)) 

    def _call_api_delete_session(self, sessionId):
        try:
            url = DEVICE_FARM_API_SESSION + '/logs/' + sessionId
            params = {}
            self._call_request_delete(url, params, DEVICE_FARM_USER_TOKEN)
        except Exception as e:
            logging.error("Can't delete device farm session;", str(e))
        

