from selenium.webdriver.common.by import By

import random


class ElementConf:
    pass


class EC2BaseLocators(ElementConf):
    EC2_URL = "https://console.engineering.vng.vn/ec2/network/security-groups"
    AUTOTEST_USER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MDlkYzFiNmY4ZjUxNWY0MmIzZjJmZTYiLCJpZCI6IjYwOWRjMWI2ZjhmNTE1ZjQyYjNmMmZlNiIsInN1YiI6IjYwOWRjMWI2ZjhmNTE1ZjQyYjNmMmZlNiIsIm5hbWUiOiJzZWxlbml1bSIsInNldHRpbmdzIjp7ImxheW91dFRoZW1lIjoic2xhdGVEYXJrMSIsInRpbWVab25lIjoiQXNpYS9Ib19DaGlfTWluaCJ9LCJ1c2VySW5mbyI6eyJidXNpbmVzc1Bob25lcyI6WyIwMzkzNjExODY2Il0sImVtcGxveWVlSWQiOiJWRy05OTk5OSIsImRpc3BsYXlOYW1lIjoiU2VsZW5pdW0iLCJkZXBhcnRtZW50IjoiUiZEIiwiam9iVGl0bGUiOiJTZW5pb3IgVGVzdGVyIiwibWFpbCI6InRlc3RAdm5nLmNvbS52biIsIm1vYmlsZVBob25lIjoiKCs4NCkgMDM5MzYxMTg2NiJ9LCJyb2xlcyI6WyJVU0VSIiwiQURNSU4iXSwicmlnaHQiOlsiVEVTVCJdLCJ1c2VyIjoic2VsZW5pdW0iLCJzdGF0dXMiOiJBQ1RJVkUiLCJpYXQiOjE2MjA5NTE2NjZ9.MiWBU2a-f_-C1BK9yHPKD3rmiA0FG3ABNT_z7YBzcko"

class SecurityGroupHomeLocators(EC2BaseLocators):
    SEC_AUTOTEST_NAME = f'quanlh2-secgroup-autotest-VM-{random.randint(100000000,9999999999)}'

    SEC_GROUP_URL = "https://console.engineering.vng.vn/ec2/network/security-groups"
    CREATE_SEC_GROUP_URL = "https://console.engineering.vng.vn/ec2/network/security-groups/create-security-group"
    SEC_GROUP_URL_AFTER_CREATED = "https://console.engineering.vng.vn/ec2/network/security-groups/"

    CREATE_SEC_GROUP_TEXTBOX_NAME_CSS = (By.CSS_SELECTOR, "input.ant-input")

    CREATE_BUTTON_X_PATH = (By.XPATH, '//span[text()=" Create Security Group"]')
    SUBMIT_CREATE_BUTTON_X_PATH = (By.XPATH, '//span[text()="Create Security Group"]')
    CREATE_SUCCESSFUL_POPUP_XPATH = (By.XPATH, "//class[text()='Created security group successfully']")

    COLLAPSE_TEXT_BOX_CLASS = (By.CLASS_NAME, "ant-collapse-content-box")
    SECURITY_GROUP_ITEM_HOME_XPATH = (By.XPATH, '//tr[@data-row-key="{security_group_id}"]')