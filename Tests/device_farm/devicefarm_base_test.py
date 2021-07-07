from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Tests.base_test import BaseTest
from Configs import DEVICE_FARM_BASE_URL, DEVICE_FARM_API_PROJECT, DEVICE_FARM_USER_TOKEN
from Pages.device_farm.devicefarm_homepage import DEVICE_FARM_HomePage
from Pages.device_farm.devicefarm_create_project_page import DEVICE_FARM_CreateProjectPage

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
    def create_df_project(self):
        self.df_homepage = DEVICE_FARM_HomePage(self.driver)
        self.df_homepage.click_create_project()
        self.df_create_project_page = DEVICE_FARM_CreateProjectPage(self.driver)
        project_name = self.df_create_project_page.fill_project_create_information()
        self.service_slug = project_name
        self.df_create_project_page.click_create_project_submit_button()
        self.driver.implicitly_wait(10)
        # WebDriverWait(self.driver, 10).until(EC.url_to_be(S3_BUCKET_DETAILS_URL.format(bucket_name=bucket_name)))
        return project_name