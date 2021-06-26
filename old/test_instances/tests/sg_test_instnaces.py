import datetime

from selenium.webdriver.common.keys import Keys
from pprint import pprint

from Locators.locators import SecurityGroupHomeLocators
from Base.base import EPAudit
from Utils.clear_test_instances import delete_security_group


class AuditCreateSecurityGroup(EPAudit):
    def __init__(self, headless=True):
        super(AuditCreateSecurityGroup, self).__init__('security_groups', headless)

    def get_create_sec_group_button(self):
        pass


    def create_security_group(self):
        but = self.driver.find_element(*SecurityGroupHomeLocators.CREATE_BUTTON_X_PATH)
        but.click()
        self.add_report("access_sec_page", self.driver.current_url == SecurityGroupHomeLocators.CREATE_SEC_GROUP_URL)

        sec_group_name = SecurityGroupHomeLocators.SEC_AUTOTEST_NAME
        name_text_box = self.driver.find_element(*SecurityGroupHomeLocators.CREATE_SEC_GROUP_TEXTBOX_NAME_CSS)
        name_text_box.send_keys(Keys.COMMAND + "a" + Keys.DELETE)
        name_text_box.send_keys(sec_group_name)

        but_submit_create = self.driver.find_element(*SecurityGroupHomeLocators.SUBMIT_CREATE_BUTTON_X_PATH)
        but_submit_create.click()

        self.driver.get(SecurityGroupHomeLocators.SEC_GROUP_URL)
        self.add_report("sec_page_accessed", SecurityGroupHomeLocators.SEC_GROUP_URL in self.driver.current_url)

        self.create_security_group()
        self.add_report("sec_group_created", SecurityGroupHomeLocators.SEC_GROUP_URL_AFTER_CREATED in self.driver.current_url)

        self.add_report("successful_popup", self.is_element_exists(SecurityGroupHomeLocators.CREATE_SUCCESSFUL_POPUP_XPATH))

        collapse_text_box = self.driver.find_element(*SecurityGroupHomeLocators.COLLAPSE_TEXT_BOX_CLASS)

        self._created_sec_group_id = self.keep_trying(lambda: collapse_text_box.find_elements_by_tag_name('div')[2].text, unsatisfactory='')
        self._created_sec_group_name = collapse_text_box.find_elements_by_tag_name('div')[6].text


    def test_create_security_group(self):
        self.create_security_group()
        self.add_report('correct_sec_id', self._created_sec_group_id in self.driver.current_url)
        self.add_report('correct_sec_name', self._created_sec_group_name == SecurityGroupHomeLocators.SEC_AUTOTEST_NAME)

        self.driver.get(SecurityGroupHomeLocators.SEC_GROUP_URL)
        self.add_report('created_sec_exists_in_homepage', self.is_element_exists(
            SecurityGroupHomeLocators.SECURITY_GROUP_ITEM_HOME_XPATH,
                custom_params={"security_group_id": self._created_sec_group_id}
        ))

    def test_security_group_flow(self):
        try:
            self.test_create_security_group()
        except Exception as e:
            raise(e)
        finally:
            if self._created_sec_group_id:
                self.driver.quit()
                delete_security_group(self._created_sec_group_id)


    def send_alerts(self):
        pprint(self.report)

if __name__ == '__main__':
    now = datetime.datetime.now()
    audit = AuditCreateSecurityGroup(headless=True)
    audit.test_security_group_flow()
    audit.send_alerts()